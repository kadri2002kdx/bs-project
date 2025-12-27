const app = require('./app');
const PORT = process.env.PORT || 3000;

// استمع على جميع الواجهات (مهم للسحابة)
const server = app.listen(PORT, '0.0.0.0', () => {
    console.log('='.repeat(50));
    console.log(`🚀 خادم المحاكاة الزراعية يعمل على المنفذ ${PORT}`);
    console.log(`🌱 الواجهة المحلية: http://localhost:${PORT}`);
    console.log(`🌐 رابط Render: https://bs-project-zi1d.onrender.com`);
    console.log(`🔗 Frontend على Netlify: https://stunning-sprite-197909.netlify.app`);
    console.log('='.repeat(50));
    console.log('\n📊 مسارات API متاحة:');
    console.log(`   GET  /health          - التحقق من صحة السيرفر`);
    console.log(`   GET  /api/plants      - قائمة النباتات`);
    console.log(`   GET  /api/wilayas     - قائمة الولايات`);
    console.log(`   POST /api/simulate    - إجراء محاكاة`);
    console.log('='.repeat(50));
});

// إعداد مهلة لتفادي إغلاق التوصيلات السريعة
server.keepAliveTimeout = 60000;
server.headersTimeout = 65000;

// معالجة الإغلاق النظيف
process.on('SIGTERM', () => {
    console.log('🛑 تلقي إشارة إيقاف، إغلاق السيرفر بنظام...');
    server.close(() => {
        console.log('✅ تم إغلاق السيرفر');
        process.exit(0);
    });
});

process.on('uncaughtException', (err) => {
    console.error('💥 خطأ غير معالج:', err);
});

process.on('unhandledRejection', (reason, promise) => {
    console.error('⚠️ وعد مرفوض غير معالج:', reason);
});
