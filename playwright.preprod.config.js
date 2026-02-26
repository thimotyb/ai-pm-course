const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests/preprod',
  timeout: 60_000,
  expect: {
    timeout: 10_000
  },
  fullyParallel: false,
  workers: 1,
  use: {
    baseURL: 'http://127.0.0.1:4173',
    headless: true
  },
  webServer: {
    command: 'bash scripts/prepare_dist.sh && cd dist && python3 -m http.server 4173 >/dev/null 2>&1',
    port: 4173,
    reuseExistingServer: true,
    timeout: 120_000
  }
});
