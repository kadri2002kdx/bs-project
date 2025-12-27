// server.js
const app = require('./app');
const PORT = process.env.PORT || 3000;

// استمع على جميع الواجهات
const server = app.listen(PORT, '0.0.0.0', () => {
    console.log(`🚀 خادم المحاكاة الزراعية يعمل على المنفذ ${PORT}`);
    console.log(`🌱 الواجهة المحلية: http://localhost:${PORT}`);
    console.log(`🌐 الرابط الخارجي: https://bs-project-zi1d.onrender.com`);
    console.log(`🔗 متصل مع Frontend: https://stunning-sprite-197909.netlify.app`);
});

// معالجة إغلاق السيرڤر بشكل أنيق
process.on('SIGTERM', () => {
    console.log('SIGTERM received, shutting down gracefully');
    server.close(() => {
        console.log('Process terminated');
    });
});

// كشف وإغلاق التوصيلات المعلقة
server.timeout = 120000; // 120 ثانية
server.keepAliveTimeout = 65000; // 65 ثانية
