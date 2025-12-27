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
            connectSrc: ["'self'", "https://stunning-sprite-197909.netlify.app"] // رابط Netlify الجديد
        },
    },
    crossOriginEmbedderPolicy: false
}));

// CORS مع السماح للـ Frontend الجديد على Netlify
app.use(cors({
    origin: [
        'https://stunning-sprite-197909.netlify.app', // الرابط الجديد
        'http://localhost:3000', // للتطوير المحلي
        'http://localhost:5173', // للتطوير المحلي مع Vite
        'https://stirring-cactus-373c6c.netlify.app' // الرابط القديم للتوافق
    ],
    credentials: true,
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    allowedHeaders: ['Content-Type', 'Authorization']
}));

app.use(compression());
app.use(morgan('combined'));
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ extended: true, limit: '50mb' }));

/* ===============================
   Frontend (الملفات الثابتة)
================================ */
// تعديل المسار إذا كانت الملفات في مجلد مختلف
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
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
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
