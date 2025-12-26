import puppeteer from 'puppeteer';
import path from 'path';

export async function generatePdf(htmlContent, outputPath) {
  const browser = await puppeteer.launch({
    headless: 'new'
  });

  const page = await browser.newPage();

  // تحميل HTML مباشرة
  await page.setContent(htmlContent, {
    waitUntil: 'networkidle0'
  });

  // تحميل الخط العربي
  const fontPath = path.resolve('fonts/Amiri-Regular.ttf');

  await page.addStyleTag({
    content: `
      @font-face {
        font-family: 'Amiri';
        src: url('file://${fontPath}');
      }

      body {
        font-family: 'Amiri', serif;
        direction: rtl;
        text-align: right;
      }
    `
  });

  // إنشاء PDF A4
  await page.pdf({
    path: outputPath,
    format: 'A4',
    printBackground: true,
    margin: {
      top: '15mm',
      bottom: '15mm',
      left: '15mm',
      right: '15mm'
    }
  });

  await browser.close();
}
