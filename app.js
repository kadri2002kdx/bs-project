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
// إعدادات Helmet مع CSP أكثر مرونة
app.use(helmet({
    contentSecurityPolicy: {
        directives: {
            defaultSrc: ["'self'"],
            scriptSrc: ["'self'", "'unsafe-inline'", "cdn.jsdelivr.net", "cdnjs.cloudflare.com"],
            styleSrc: ["'self'", "'unsafe-inline'", "cdn.jsdelivr.net", "fonts.googleapis.com", "cdnjs.cloudflare.com"],
            fontSrc: ["'self'", "fonts.gstatic.com", "cdnjs.cloudflare.com", "data:"],
            imgSrc: ["'self'", "data:", "blob:"],
            connectSrc: ["'self'", "https://stunning-sprite-197909.netlify.app", "https://bs-project-zi1d.onrender.com"]
        },
    },
    crossOriginEmbedderPolicy: false,
    crossOriginResourcePolicy: { policy: "cross-origin" }
}));

// CORS: السماح بجميع المصادر أو تحديد المصادر المسموح بها
app.use(cors({
    origin: function(origin, callback) {
        // السماح بطلبات بدون أصل (مثل Postman) أو من المصادر المسموح بها
        const allowedOrigins = [
            'https://stunning-sprite-197909.netlify.app',
            'https://stirring-cactus-373c6c.netlify.app',
            'http://localhost:3000',
            'http://localhost:5500',
            'http://127.0.0.1:5500'
        ];
        
        if (!origin || allowedOrigins.indexOf(origin) !== -1) {
            callback(null, true);
        } else {
            callback(new Error('Not allowed by CORS'));
        }
    },
    credentials: true,
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'],
    allowedHeaders: ['Content-Type', 'Authorization', 'X-Requested-With']
}));

// معالجة طلبات OPTIONS مسبقاً
app.options('*', cors());

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
app.get("/health", (req, res) => {
    res.status(200).json({ 
        status: "OK", 
        timestamp: new Date().toISOString(),
        uptime: process.uptime(),
        message: "Server is running",
        frontendUrl: "https://stunning-sprite-197909.netlify.app"
    });
});

/* ===============================
   API Routes (مسارات البرمجة)
================================ */
app.use('/api', apiRoutes);

/* ===============================
   Frontend Fallback (الحل المستقر)
================================ */
app.get('*', (req, res, next) => {
    if (req.url.startsWith('/api')) {
        return next();
    }
    res.sendFile(path.join(__dirname, 'frontend', 'index.html'));
});

/* ===============================
   Error Handler (معالج الأخطاء)
================================ */
app.use((err, req, res, next) => {
    console.error('❌ خطأ في الخادم:', err.message);
    res.status(err.status || 500).json({
        success: false,
        message: err.message || 'حدث خطأ داخلي في الخادم',
        timestamp: new Date().toISOString()
    });
});

module.exports = app;
