// ===============================
// app.js (Production Ready)
// Netlify (Frontend) + Render (Backend)
// ===============================

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const compression = require('compression');
const path = require('path');

const apiRoutes = require('./src/routes');

const app = express();

/* ===============================
   Security & Middlewares
================================ */
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: [
        "'self'",
        "'unsafe-inline'",
        "cdn.jsdelivr.net",
        "cdnjs.cloudflare.com"
      ],
      styleSrc: [
        "'self'",
        "'unsafe-inline'",
        "cdn.jsdelivr.net",
        "fonts.googleapis.com",
        "cdnjs.cloudflare.com"
      ],
      fontSrc: [
        "'self'",
        "fonts.gstatic.com",
        "cdnjs.cloudflare.com",
        "data:"
      ],
      imgSrc: [
        "'self'",
        "data:",
        "blob:"
      ],
      connectSrc: [
        "'self'",
        "https://bs-project-zi1d.onrender.com"
      ]
    }
  },
  crossOriginEmbedderPolicy: false,
  crossOriginResourcePolicy: { policy: "cross-origin" }
}));

/* ===============================
   CORS (مفتوح وآمن لحالة API عامة)
================================ */
app.use(cors({
  origin: '*',
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-Requested-With']
}));

app.options('*', cors());

/* ===============================
   Performance & Parsers
================================ */
app.use(compression());
app.use(morgan('combined'));
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ extended: true, limit: '50mb' }));

/* ===============================
   Frontend Static Files (اختياري)
================================ */
app.use(express.static(path.join(__dirname, 'frontend')));

/* ===============================
   Health Check (Render uptime)
================================ */
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'OK',
    message: 'Server is running',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

/* ===============================
   API Routes
================================ */
app.use('/api', apiRoutes);

/* ===============================
   SPA Fallback
================================ */
app.get('*', (req, res, next) => {
  if (req.originalUrl.startsWith('/api')) {
    return next();
  }
  res.sendFile(path.join(__dirname, 'frontend', 'index.html'));
});

/* ===============================
   Global Error Handler
================================ */
app.use((err, req, res, next) => {
  console.error('❌ Server Error:', err.stack);
  res.status(err.status || 500).json({
    success: false,
    message: err.message || 'Internal Server Error',
    timestamp: new Date().toISOString()
  });
});

module.exports = app;
