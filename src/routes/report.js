const express = require('express');
const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const router = express.Router();
// POST /api/report - إنشاء تقرير PDF
router.post('/report', async (req, res) => {
  try {
    console.log('📄 بدء إنشاء التقرير PDF...');
    
    const { html, filename = 'تقرير_المحاكاة.pdf' } = req.body;

    if (!html) {
      return res.status(400).json({ 
        success: false, 
        message: 'محتوى HTML مطلوب' 
      });
    }

    // تكوين Puppeteer
    const browser = await puppeteer.launch({
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const page = await browser.newPage();

    // تحميل الخط العربي (إذا كان موجوداً)
    try {
      const fontPath = path.join(__dirname, '../../fonts/Amiri-Regular.ttf');
      if (fs.existsSync(fontPath)) {
        console.log('📝 جاري تحميل الخط العربي...');
        await page.addStyleTag({
          content: `
            @font-face {
              font-family: 'Amiri';
              src: url('file://${fontPath.replace(/\\/g, '/')}');
              font-weight: normal;
              font-style: normal;
            }
            * {
              font-family: 'Amiri', serif !important;
            }
          `
        });
      }
    } catch (fontErr) {
      console.log('⚠️ لم يتم تحميل الخط، استخدام الخطوط الافتراضية');
    }

    // تعيين المحتوى
    await page.setContent(html, { 
      waitUntil: ['networkidle0', 'load', 'domcontentloaded'] 
    });

    // تحديد مسار لحفظ PDF مؤقت
    const tempDir = path.join(__dirname, '../../temp');
    if (!fs.existsSync(tempDir)) {
      fs.mkdirSync(tempDir, { recursive: true });
    }
    
    const pdfPath = path.join(tempDir, `report_${Date.now()}.pdf`);

    // إنشاء PDF
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: '<div></div>',
      footerTemplate: `
        <div style="width:100%; text-align:center; font-size:10px; font-family:'Amiri', serif; direction:rtl;">
          الصفحة <span class="pageNumber"></span> من <span class="totalPages"></span> | EcoPlant DZ
        </div>
      `,
      margin: {
        top: '30mm',
        bottom: '30mm',
        left: '20mm',
        right: '20mm'
      }
    });

    await browser.close();
    console.log(`✅ تم إنشاء PDF في: ${pdfPath}`);

    // إرسال الملف للعميل
    res.download(pdfPath, filename, (err) => {
      if (err) {
        console.error('❌ خطأ في إرسال الملف:', err);
      }
      // حذف الملف المؤقت بعد الإرسال
      setTimeout(() => {
        if (fs.existsSync(pdfPath)) {
          fs.unlinkSync(pdfPath);
          console.log('🗑️ تم حذف الملف المؤقت');
        }
      }, 5000);
    });

  } catch (err) {
    console.error('❌ خطأ في إنشاء PDF:', err);
    res.status(500).json({ 
      success: false, 
      message: 'فشل إنشاء PDF: ' + err.message 
    });
  }
});

// GET /api/report/test - لاختبار PDF
router.get('/report/test', async (req, res) => {
  try {
    const browser = await puppeteer.launch({
      headless: 'new'
    });
    
    const page = await browser.newPage();
    await page.setContent(`
      <html dir="rtl">
        <head>
          <meta charset="UTF-8">
          <style>
            body { font-family: 'Amiri', serif; padding: 40px; }
            h1 { color: #1b5e20; text-align: center; }
            p { font-size: 18px; line-height: 1.8; }
          </style>
        </head>
        <body>
          <h1>✅ اختبار PDF العربي</h1>
          <p>هذا نص اختباري باللغة العربية لفحص دعم الخطوط.</p>
          <p>إذا ظهر النص العربي صحيحاً، فهذا يعني أن النظام يعمل بشكل ممتاز!</p>
        </body>
      </html>
    `);
    
    const pdf = await page.pdf({ format: 'A4' });
    await browser.close();
    
    res.setHeader('Content-Type', 'application/pdf');
    res.setHeader('Content-Disposition', 'attachment; filename=test.pdf');
    res.send(pdf);
    
  } catch (err) {
    console.error(err);
    res.status(500).send('فشل اختبار PDF');
  }
});

module.exports = router;