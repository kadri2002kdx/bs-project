// app.js
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const compression = require('compression');
const path = require('path');

const apiRoutes = require('./src/routes');

const app = express();

/* ===============================
   Middlewares (إعدادات الحماية والبيانات)
================================ */
app.use(helmet({
    contentSecurityPolicy: {
        directives: {
            defaultSrc: ["'self'"],
            scriptSrc: ["'self'", "'unsafe-inline'", "cdn.jsdelivr.net", "cdnjs.cloudflare.com"],
            styleSrc: ["'self'", "'unsafe-inline'", "cdn.jsdelivr.net", "fonts.googleapis.com", "cdnjs.cloudflare.com"],
            fontSrc: ["'self'", "fonts.gstatic.com", "cdnjs.cloudflare.com", "data:", "file:"], // تمت إضافة "file:" هنا
            imgSrc: ["'self'", "data:", "blob:"],
            connectSrc: ["'self'"]
        },
    },
    crossOriginEmbedderPolicy: false
}));

app.use(cors());
app.use(compression());
app.use(morgan('combined'));
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ extended: true, limit: '50mb' }));

/* ===============================
   Frontend (الملفات الثابتة)
================================ */
app.use(express.static(path.join(__dirname, 'frontend')));

/* ===============================
   API Routes (مسارات البرمجة)
================================ */
app.use('/api', apiRoutes);

/* ===============================
   Frontend Fallback (الحل المستقر)
================================ */
// بدلاً من استخدام رموز مثل * أو (.*)، سنستخدم middleware عام 
// يوضع في نهاية المسارات للتعامل مع أي طلب ليس API
app.use((req, res, next) => {
    // إذا كان الطلب يبدأ بـ /api، نتركه يمر ليظهر خطأ 404 الخاص بالـ API
    if (req.url.startsWith('/api')) {
        return next();
    }
    // أي طلب آخر (صفحات HTML)، أرسل ملف index.html
    res.sendFile(path.join(__dirname, 'frontend', 'index.html'));
});

/* ===============================
   Error Handler (معالج الأخطاء)
================================ */
app.use((err, req, res, next) => {
    console.error('❌ خطأ في الخادم:', err);
    res.status(err.status || 500).json({
        success: false,
        message: err.message || 'حدث خطأ داخلي في الخادم'
    });
});

module.exports = app;