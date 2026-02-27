#!/usr/bin/env python3
import html
import re
from pathlib import Path

COURSE_MD = Path('course.md')
HOME_HTML = Path('index.html')


def parse_course(markdown: str):
    title = None
    modules = []
    labs_body = ''
    bibliography_body = ''
    home_note_body = ''

    title_match = re.search(r'^#\s+(.+)$', markdown, re.M)
    if title_match:
        title = title_match.group(1).strip()

    section_pattern = re.compile(r'^##\s+(.+?)\s*$', re.M)
    section_matches = list(section_pattern.finditer(markdown))

    section_bodies = {}
    for idx, match in enumerate(section_matches):
        section_name = match.group(1).strip().lower()
        start = match.end()
        end = section_matches[idx + 1].start() if idx + 1 < len(section_matches) else len(markdown)
        section_bodies[section_name] = markdown[start:end].strip('\n')

    labs_body = section_bodies.get('labs', '')
    bibliography_body = section_bodies.get('bibliografia', '')
    home_note_body = section_bodies.get('nota home', '')

    modules_region = markdown
    tail_starts = [
        match.start()
        for match in section_matches
        if match.group(1).strip().lower() in {'labs', 'bibliografia', 'nota home'}
    ]
    if tail_starts:
        modules_region = markdown[:min(tail_starts)]

    module_pattern = re.compile(r'^##\s+Modulo\s+(\d+)\s*:\s*(.+)$', re.M)
    matches = list(module_pattern.finditer(modules_region))

    for idx, match in enumerate(matches):
        num = int(match.group(1))
        module_title = match.group(2).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(modules_region)
        body = modules_region[start:end].strip('\n')
        modules.append({'number': num, 'title': module_title, 'body': body})

    return title, modules, labs_body, bibliography_body, home_note_body


def format_inline(text: str) -> str:
    escaped = html.escape(text)
    def _replace_link(match):
        label = match.group(1)
        href = html.unescape(match.group(2))
        safe_href = html.escape(href, quote=True)
        if href.startswith('http://') or href.startswith('https://'):
            return f'<a href="{safe_href}" target="_blank" rel="noopener noreferrer">{label}</a>'
        return f'<a href="{safe_href}">{label}</a>'

    escaped = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', _replace_link, escaped)
    escaped = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escaped)
    escaped = re.sub(r'\*(.+?)\*', r'<em>\1</em>', escaped)
    escaped = re.sub(r'`(.+?)`', r'<code>\1</code>', escaped)
    return escaped


def split_table_cells(row_line: str):
    cleaned = row_line.strip()
    if cleaned.startswith('|'):
        cleaned = cleaned[1:]
    if cleaned.endswith('|'):
        cleaned = cleaned[:-1]
    return [format_inline(cell.strip()) for cell in cleaned.split('|')]


def is_table_separator(row_line: str) -> bool:
    if '|' not in row_line:
        return False
    cells = split_table_cells(row_line)
    if not cells:
        return False
    return all(re.match(r'^:?-{3,}:?$', html.unescape(cell)) for cell in cells)


def body_to_html(body: str) -> str:
    lines = body.splitlines()
    out = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        if (
            '|' in line
            and i + 1 < len(lines)
            and is_table_separator(lines[i + 1].strip())
        ):
            header_cells = split_table_cells(line)
            i += 2

            rows = []
            while i < len(lines):
                current = lines[i].strip()
                if not current or '|' not in current:
                    break
                if is_table_separator(current):
                    i += 1
                    continue
                rows.append(split_table_cells(current))
                i += 1

            max_cols = len(header_cells)
            for row in rows:
                max_cols = max(max_cols, len(row))

            def normalize(cells):
                return cells + [''] * (max_cols - len(cells))

            thead = ''.join(f'<th>{cell}</th>' for cell in normalize(header_cells))
            tbody_rows = []
            for row in rows:
                tds = ''.join(f'<td>{cell}</td>' for cell in normalize(row))
                tbody_rows.append(f'<tr>{tds}</tr>')

            tbody = ''.join(tbody_rows)
            out.append(
                '<div class="table-wrap">'
                '<table class="content-table">'
                f'<thead><tr>{thead}</tr></thead>'
                f'<tbody>{tbody}</tbody>'
                '</table>'
                '</div>'
            )
            continue

        h3_match = re.match(r'^###\s+(.+)$', line)
        if h3_match:
            heading_text = h3_match.group(1).strip()
            heading_key = heading_text.lower()
            if heading_key in {
                'scheda rapida del modulo',
                'checklist dei concetti principali',
                'principali punti di fine sezione',
            }:
                i += 1
                block_lines = []
                seen_content = False
                while i < len(lines):
                    current_raw = lines[i]
                    current = current_raw.strip()
                    if re.match(r'^###\s+.+$', current) or re.match(r'^####\s+.+$', current):
                        break
                    if not current:
                        if seen_content:
                            break
                        i += 1
                        continue
                    seen_content = True
                    block_lines.append(current_raw)
                    i += 1

                card_html = body_to_html('\n'.join(block_lines).strip('\n'))
                card_class = 'quick-card' if heading_key == 'scheda rapida del modulo' else 'checklist-card'
                out.append(
                    f'<section class="{card_class}">'
                    f'<h3 class="module-subtitle">{format_inline(heading_text)}</h3>'
                    f'{card_html}'
                    '</section>'
                )
                continue

            out.append(f'<h3 class="module-subtitle">{format_inline(heading_text)}</h3>')
            i += 1
            continue

        h4_match = re.match(r'^####\s+(.+)$', line)
        if h4_match:
            out.append(f'<h4 class="module-subtitle-small">{format_inline(h4_match.group(1).strip())}</h4>')
            i += 1
            continue

        img_match = re.match(r'^!\[(.*?)\]\((.*?)\)$', line)
        if img_match:
            alt = format_inline(img_match.group(1).strip())
            src = html.escape(img_match.group(2).strip(), quote=True)
            caption_html = ''
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                caption_match = re.match(r'^\*(.*?)\*$', next_line)
                if caption_match:
                    caption = format_inline(caption_match.group(1).strip())
                    caption_html = (
                        '<figcaption class="figure-caption">'
                        f'{caption}'
                        '</figcaption>'
                    )
                    i += 1

            # Clickable images with zoomed class toggle
            out.append(
                '<figure class="module-image">'
                f'<img src="{src}" alt="{alt}" onclick="this.classList.toggle(\'zoomed\')">'
                f'{caption_html}'
                '</figure>'
            )
            i += 1
            continue

        if re.match(r'^\d+\.\s+.+$', line):
            items = []
            while i < len(lines):
                current = lines[i].strip()
                match = re.match(r'^\d+\.\s+(.+)$', current)
                if not match:
                    break
                items.append(format_inline(match.group(1).strip()))
                i += 1
            lis = ''.join(f'<li>{item}</li>' for item in items)
            out.append(f'<ol>{lis}</ol>')
            continue

        if line.startswith('- '):
            items = []
            while i < len(lines):
                current = lines[i].strip()
                if not current.startswith('- '):
                    break
                items.append(format_inline(current[2:].strip()))
                i += 1
            lis = ''.join(f'<li>{item}</li>' for item in items)
            out.append(f'<ul>{lis}</ul>')
            continue

        out.append(f'<p>{format_inline(line)}</p>')
        i += 1

    return '\n'.join(out)


def module_filename(module_number: int) -> str:
    return f'module-{module_number:02d}.html'


def first_teaser(body: str) -> str:
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith('###') or line.startswith('####'):
            continue
        if line.startswith('- ') or re.match(r'^\d+\.\s+', line):
            continue
        if re.match(r'^!\[', line):
            continue
        if len(line) > 190:
            return line[:187] + '...'
        return line
    return ''


STYLE = '''
:root {
  --bg-color: #000c1d;
  --card-bg: rgba(255, 255, 255, 0.05);
  --accent-primary: #ffcc00;
  --accent-secondary: #00d4ff;
  --text-color: #f0f0f0;
  --text-muted: #a0a0a0;
  --glass-border: rgba(255, 255, 255, 0.12);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
  font-family: 'Inter', sans-serif;
  background: radial-gradient(circle at top right, #001f3f, var(--bg-color));
  color: var(--text-color);
  line-height: 1.62;
  min-height: 100vh;
}

.container { max-width: 1080px; margin: 0 auto; padding: 34px 18px 50px; }

header { text-align: center; padding: 38px 0 24px; }

h1 {
  font-family: 'Outfit', sans-serif;
  font-size: 3rem;
  font-weight: 700;
  background: linear-gradient(to right, var(--accent-primary), #fff);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1.1;
}

.subtitle {
  font-size: 1rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 3px;
  margin-bottom: 10px;
}

.card {
  background: var(--card-bg);
  border: 1px solid var(--glass-border);
  border-radius: 20px;
  padding: 26px;
  box-shadow: 0 20px 36px rgba(0, 0, 0, 0.35);
}

.section-title {
  font-family: 'Outfit', sans-serif;
  color: var(--accent-secondary);
  font-size: 1.8rem;
  margin-bottom: 18px;
}

.agenda-list { list-style: none; display: grid; gap: 12px; }

.agenda-item {
  border: 1px solid var(--glass-border);
  border-radius: 12px;
  transition: transform 0.2s ease, border-color 0.2s ease, background 0.2s ease;
}

.agenda-item:hover {
  transform: translateY(-1px);
  border-color: var(--accent-secondary);
  background: rgba(255,255,255,0.03);
}

.agenda-link {
  display: flex;
  align-items: center;
  gap: 14px;
  text-decoration: none;
  color: inherit;
  padding: 14px 16px;
}

.agenda-number {
  font-family: 'Outfit', sans-serif;
  color: var(--accent-primary);
  font-size: 1.35rem;
  min-width: 42px;
}

.agenda-text { font-size: 1.1rem; font-weight: 600; }
.agenda-teaser { color: #cfd8e3; font-size: 0.95rem; margin-top: 4px; }

.module-nav,
.jump-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}

.nav-btn {
  text-decoration: none;
  color: var(--text-color);
  border: 1px solid var(--glass-border);
  border-radius: 999px;
  padding: 7px 12px;
  font-size: 0.9rem;
  transition: background 0.2s ease, border-color 0.2s ease;
}

.nav-btn:hover { background: rgba(255,255,255,0.06); border-color: var(--accent-secondary); }

.module-kicker {
  color: var(--accent-primary);
  font-size: 0.82rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 6px;
}

.module-title {
  font-family: 'Outfit', sans-serif;
  font-size: 2rem;
  color: var(--accent-secondary);
  margin-bottom: 18px;
  line-height: 1.2;
}

.module-subtitle {
  font-family: 'Outfit', sans-serif;
  font-size: 1.3rem;
  margin: 22px 0 10px;
}

.quick-card {
  margin: 10px 0 20px;
  padding: 14px 16px 8px;
  border: 1px solid rgba(255, 204, 0, 0.45);
  border-left: 5px solid var(--accent-primary);
  border-radius: 12px;
  background: linear-gradient(135deg, rgba(255, 204, 0, 0.12), rgba(0, 212, 255, 0.06));
}

.quick-card .module-subtitle {
  margin: 0 0 8px;
  color: #fff5cc;
}

.quick-card p,
.quick-card ul,
.quick-card ol {
  margin-top: 4px;
}

.checklist-card {
  margin: 22px 0 8px;
  padding: 14px 16px 8px;
  border: 1px solid rgba(0, 212, 255, 0.45);
  border-left: 5px solid var(--accent-secondary);
  border-radius: 12px;
  background: linear-gradient(135deg, rgba(0, 212, 255, 0.12), rgba(255, 204, 0, 0.05));
}

.checklist-card .module-subtitle {
  margin: 0 0 8px;
  color: #d8f8ff;
}

.checklist-card p,
.checklist-card ul,
.checklist-card ol {
  margin-top: 4px;
}

.module-subtitle-small {
  font-family: 'Outfit', sans-serif;
  font-size: 1.1rem;
  margin: 18px 0 8px;
  color: #d7ecff;
}

.module-content p { margin-bottom: 12px; color: #e2e7ec; }
.module-content ul,
.module-content ol { margin: 8px 0 14px 22px; }
.module-content li { margin-bottom: 6px; }
.module-content a { color: var(--accent-secondary); }

.table-wrap {
  margin: 12px 0 18px;
  overflow-x: auto;
}

.content-table {
  width: 100%;
  min-width: 680px;
  border-collapse: collapse;
  border: 1px solid var(--glass-border);
  border-radius: 12px;
  overflow: hidden;
}

.content-table th,
.content-table td {
  border: 1px solid var(--glass-border);
  padding: 10px 12px;
  text-align: left;
  vertical-align: top;
}

.content-table th {
  color: var(--accent-primary);
  background: rgba(255, 255, 255, 0.04);
  font-family: 'Outfit', sans-serif;
  font-weight: 600;
}

.content-table td {
  color: #e2e7ec;
}

.content-table tbody tr:nth-child(even) td {
  background: rgba(255, 255, 255, 0.02);
}

.module-image { margin: 24px 0; text-align: center; }
.module-image img {
  width: 100%;
  max-width: 820px;
  background: #ffffff;
  box-sizing: border-box;
  padding: 8px;
  border-radius: 12px;
  border: 1px solid var(--glass-border);
  display: block;
  margin: 0 auto;
  cursor: zoom-in;
  transition: transform 0.3s ease;
}

/* Lightbox/Zoom effect */
.module-image img.zoomed {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  max-width: none;
  object-fit: contain;
  z-index: 10000;
  background: #ffffff;
  margin: 0;
  padding: 20px;
  border: none;
  border-radius: 0;
  cursor: zoom-out;
}

.figure-caption {
  color: var(--text-muted);
  font-size: 0.9rem;
  margin-top: 8px;
  text-align: center;
}

.footer-nav { margin-top: 20px; }
.labs-section { margin-top: 28px; }
.site-footnote {
  margin: 14px 6px 4px;
  padding: 10px 12px;
  border-top: 1px solid var(--glass-border);
}
.site-footnote p {
  color: var(--text-muted);
  font-size: 0.86rem;
  line-height: 1.45;
  text-align: center;
}

.to-top-btn {
  position: fixed;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 999;
  border: 1px solid var(--glass-border);
  background: rgba(0, 18, 40, 0.85);
  color: var(--text-color);
  border-radius: 999px;
  padding: 10px 12px;
  font-size: 0.82rem;
  cursor: pointer;
  backdrop-filter: blur(4px);
  transition: background 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
}

.to-top-btn:hover {
  background: rgba(0, 28, 62, 0.95);
  border-color: var(--accent-secondary);
  transform: translateY(-50%) scale(1.03);
}

@media (max-width: 768px) {
  h1 { font-size: 2.25rem; }
  .module-title { font-size: 1.55rem; }
  .container { padding: 20px 14px 36px; }
  .card { padding: 18px; }
  .to-top-btn {
    top: auto;
    bottom: 14px;
    transform: none;
    right: 12px;
    font-size: 0.78rem;
    padding: 9px 10px;
  }
  .to-top-btn:hover {
    transform: scale(1.03);
  }
}
'''


def build_home_page(title: str, modules, labs_body: str, bibliography_body: str, home_note_body: str):
    agenda_items = []
    for module in modules:
        num = module['number']
        item_title = html.escape(module['title'])
        teaser = first_teaser(module['body'])
        teaser_html = f'<p class="agenda-teaser">{format_inline(teaser)}</p>' if teaser else ''
        agenda_items.append(
            '<li class="agenda-item">'
            f'<a class="agenda-link" href="{module_filename(num)}">'
            f'<span class="agenda-number">{num:02d}</span>'
            '<span>'
            f'<span class="agenda-text">{item_title}</span>'
            f'{teaser_html}'
            '</span>'
            '</a>'
            '</li>'
        )

    labs_section = ''
    if labs_body:
        labs_html = body_to_html(labs_body)
        labs_section = f'''
      <section class="card labs-section">
        <h2 class="section-title">Labs</h2>
        <section class="module-content">
{chr(10).join('          ' + ln for ln in labs_html.splitlines())}
        </section>
      </section>
'''

    bibliography_section = ''
    if bibliography_body:
        bibliography_html = body_to_html(bibliography_body)
        bibliography_section = f'''
      <section class="card">
        <h2 class="section-title">Bibliografia</h2>
        <section class="module-content">
{chr(10).join('          ' + ln for ln in bibliography_html.splitlines())}
        </section>
      </section>
'''

    home_note_html = ''
    if home_note_body:
        note_html = body_to_html(home_note_body)
        home_note_html = f'''
      <section class="site-footnote">
{chr(10).join('        ' + ln for ln in note_html.splitlines())}
      </section>
'''

    return f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Outfit:wght@300;500;700&display=swap" rel="stylesheet">
  <style>{STYLE}</style>
</head>
<body>
  <div class="container">
    <header>
      <p class="subtitle">Corso di Alta Formazione</p>
      <h1>{html.escape(title)}</h1>
    </header>

    <main>
      <section class="card">
        <h2 class="section-title">Indice Moduli</h2>
        <ul class="agenda-list">
          {''.join(agenda_items)}
        </ul>
      </section>
{labs_section}
{bibliography_section}
{home_note_html}
    </main>
  </div>
  <button class="to-top-btn" type="button" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">↑ Torna su</button>
</body>
</html>
'''


def build_module_page(course_title: str, modules, idx: int, labs_body: str):
    module = modules[idx]
    num = module['number']
    body_html = body_to_html(module['body'])

    prev_link = module_filename(modules[idx - 1]['number']) if idx > 0 else None
    next_link = module_filename(modules[idx + 1]['number']) if idx < len(modules) - 1 else None

    nav_links = ['<a class="nav-btn" href="index.html">Home</a>']
    if prev_link:
        nav_links.append(f'<a class="nav-btn" href="{prev_link}">Modulo Precedente</a>')
    if next_link:
        nav_links.append(f'<a class="nav-btn" href="{next_link}">Modulo Successivo</a>')

    jump_links = [
        f'<a class="nav-btn" href="{module_filename(m["number"])}">{m["number"]:02d} - {html.escape(m["title"])}</a>'
        for m in modules
    ]

    labs_section = ''
    if labs_body:
        labs_html = body_to_html(labs_body)
        labs_section = f'''
        <section class="module-content labs-section">
          <h3 class="module-subtitle">Labs</h3>
{chr(10).join('          ' + ln for ln in labs_html.splitlines())}
        </section>
'''

    return f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modulo {num:02d} - {html.escape(module['title'])}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Outfit:wght@300;500;700&display=swap" rel="stylesheet">
  <style>{STYLE}</style>
</head>
<body>
  <div class="container">
    <header>
      <p class="subtitle">{html.escape(course_title)}</p>
      <h1>Modulo {num:02d}</h1>
    </header>

    <main>
      <article class="card">
        <nav class="module-nav">{''.join(nav_links)}</nav>
        <nav class="jump-nav">{''.join(jump_links)}</nav>

        <p class="module-kicker">Modulo {num:02d}</p>
        <h2 class="module-title">{html.escape(module['title'])}</h2>

        <section class="module-content">
{chr(10).join('          ' + ln for ln in body_html.splitlines())}
        </section>

{labs_section}
        <nav class="module-nav footer-nav">{''.join(nav_links)}</nav>
      </article>
    </main>
  </div>
  <button class="to-top-btn" type="button" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">↑ Torna su</button>
</body>
</html>
'''


def regenerate():
    markdown = COURSE_MD.read_text(encoding='utf-8')
    title, modules, labs_body, bibliography_body, home_note_body = parse_course(markdown)
    if not title:
        raise SystemExit('Missing course title in course.md')
    if not modules:
        raise SystemExit('No modules found in course.md (expected headings like: ## Modulo 01: Titolo)')

    HOME_HTML.write_text(build_home_page(title, modules, labs_body, bibliography_body, home_note_body), encoding='utf-8')

    generated = ['index.html']
    for idx, module in enumerate(modules):
        out = Path(module_filename(module['number']))
        out.write_text(build_module_page(title, modules, idx, labs_body), encoding='utf-8')
        generated.append(out.name)

    print(f'Generated {len(generated)} HTML files from {COURSE_MD}:')
    for name in generated:
        print(f'- {name}')


if __name__ == '__main__':
    regenerate()
