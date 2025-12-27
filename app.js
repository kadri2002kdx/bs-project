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
            fontSrc: ["'self'", "fonts.gstatic.com", "cdnjs.cloudflare.com", "data:"],
            imgSrc: ["'self'", "data:", "blob:"],
            connectSrc: ["'self'", "https://stunning-sprite-197909.netlify.app"] // رابط Netlify الجديد
        },
    },
    crossOriginEmbedderPolicy: false
}));

// CORS - السماح للروابط المطلوبة فقط
app.use(cors({
    origin: [
        'https://stunning-sprite-197909.netlify.app', // الرابط الجديد
        'https://stirring-cactus-373c6c.netlify.app', // الرابط القديم
        'http://localhost:3000', // للتطوير المحلي
        'http://localhost:5173'  // للتطوير المحلي مع Vite
    ],
    credentials: true,
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
}));

app.use(compression());
app.use(morgan('combined'));
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ extended: true, limit: '50mb' }));

/* ===============================
   Frontend (الملفات الثابتة)
================================ */
// استخدم المسار الأصلي 'frontend' إذا كان موجوداً، وإلا فاستخدم 'public'
app.use(express.static(path.join(__dirname, 'frontend')));
app.use(express.static(path.join(__dirname, 'public')));

/* ===============================
   Health check endpoint (لمنع نوم السيرفر)
================================ */
app.get("/health", (req, res) => {
    res.status(200).json({ 
        status: "OK", 
        timestamp: new Date().toISOString(),
        uptime: process.uptime()
    });
});

/* ===============================
   API Routes (مسارات البرمجة)
================================ */
app.use('/api', apiRoutes);

/* ===============================
   Frontend Fallback (الحل المستقر)
================================ */
// هذا المسار يجب أن يكون في النهاية ليعمل كـ catch-all
app.use((req, res, next) => {
    // إذا كان الطلب يبدأ بـ /api، نتركه يمر ليظهر خطأ 404 الخاص بالـ API
    if (req.url.startsWith('/api')) {
        return next();
    }
    // حاول أولاً في مجلد frontend
    res.sendFile(path.join(__dirname, 'frontend', 'index.html'), (err) => {
        // إذا لم يوجد في frontend، حاول في public
        if (err) {
            res.sendFile(path.join(__dirname, 'public', 'index.html'), (err2) => {
                // إذا لم يوجد في أي منهما، أرسل رسالة خطأ
                if (err2) {
                    res.status(404).send('الصفحة غير موجودة');
                }
            });
        }
    });
});

/* ===============================
   Error Handler (معالج الأخطاء)
================================ */
app.use((err, req, res, next) => {
    console.error('❌ خطأ في الخادم:', err);
    res.status(err.status || 500).json({
        success: false,
        message: err.message || 'حدث خطأ داخلي في الخادم',
        timestamp: new Date().toISOString()
    });
});

module.exports = app;
