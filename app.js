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
            fontSrc: ["'self'", "fonts.gstatic.com", "cdnjs.cloudflare.com", "data:", "file:"],
            imgSrc: ["'self'", "data:", "blob:"],
            connectSrc: ["'self'", "https://stunning-sprite-197909.netlify.app"] // رابط Frontend الجديد على Netlify
        },
    },
    crossOriginEmbedderPolicy: false
}));

// CORS مع السماح للـ Frontend فقط
app.use(cors({
    origin: [
        'https://stunning-sprite-197909.netlify.app', // الرابط الجديد
        'https://stirring-cactus-373c6c.netlify.app', // الرابط القديم للتوافق
        'http://localhost:3000' // للتطوير المحلي
    ],
    credentials: true
}));

app.use(compression());
app.use(morgan('combined'));
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ extended: true, limit: '50mb' }));

/* ===============================
   Frontend (الملفات الثابتة)
================================ */
app.use(express.static(path.join(__dirname, 'frontend')));

/* ===============================
   Health check endpoint (لمنع نوم السيرفر)
================================ */
app.get("/health", (req, res) => res.send("OK"));

/* ===============================
   API Routes (مسارات البرمجة)
================================ */
app.use('/api', apiRoutes);

/* ===============================
   Frontend Fallback (الحل المستقر)
================================ */
app.use((req, res, next) => {
    if (req.url.startsWith('/api')) return next();
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
