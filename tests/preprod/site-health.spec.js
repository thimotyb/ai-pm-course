const fs = require('fs');
const path = require('path');
const { test, expect } = require('@playwright/test');

function listHtmlPages() {
  const distDir = path.resolve(__dirname, '..', '..', 'dist');
  return fs
    .readdirSync(distDir, { withFileTypes: true })
    .filter((entry) => entry.isFile() && entry.name.endsWith('.html'))
    .map((entry) => entry.name)
    .sort();
}

test('Nessuna immagine rotta nelle pagine pubblicate', async ({ page, request }) => {
  const pages = listHtmlPages();
  expect(pages.length).toBeGreaterThan(0);

  for (const fileName of pages) {
    await page.goto(`/${fileName}`, { waitUntil: 'networkidle' });

    const imageData = await page.$$eval('img', (imgs) =>
      imgs.map((img) => ({
        src: img.getAttribute('src') || '',
        complete: img.complete,
        naturalWidth: img.naturalWidth
      }))
    );

    for (const [index, img] of imageData.entries()) {
      expect(img.complete, `${fileName}: img #${index + 1} non completa il caricamento`).toBeTruthy();
      expect(img.naturalWidth, `${fileName}: img #${index + 1} ha larghezza naturale nulla`).toBeGreaterThan(0);
    }

    const uniqueSrc = [...new Set(imageData.map((img) => img.src).filter(Boolean))];
    for (const src of uniqueSrc) {
      if (src.startsWith('data:') || src.startsWith('blob:')) {
        continue;
      }
      const absoluteUrl = new URL(src, page.url()).toString();
      const response = await request.get(absoluteUrl);
      expect(
        response.ok(),
        `${fileName}: risorsa immagine non disponibile (${src}) -> status ${response.status()}`
      ).toBeTruthy();
    }
  }
});

test('Le immagini dei moduli hanno sfondo bianco esplicito', async ({ page }) => {
  const pages = listHtmlPages().filter((name) => /^module-\d+\.html$/.test(name));
  expect(pages.length).toBeGreaterThan(0);

  for (const fileName of pages) {
    await page.goto(`/${fileName}`, { waitUntil: 'networkidle' });

    const nonWhite = await page.$$eval('.module-image img', (imgs) =>
      imgs
        .map((img, index) => {
          const bg = window.getComputedStyle(img).backgroundColor;
          return { index: index + 1, backgroundColor: bg };
        })
        .filter(
          (item) =>
            item.backgroundColor !== 'rgb(255, 255, 255)' &&
            item.backgroundColor !== 'rgba(255, 255, 255, 1)'
        )
    );

    expect(nonWhite, `${fileName}: immagini senza sfondo bianco`).toEqual([]);
  }
});
