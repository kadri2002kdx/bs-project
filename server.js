// server.js
const app = require('./app');
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`🚀 خادم المحاكاة الزراعية يعمل على المنفذ ${PORT}`);
    console.log(`🌱 المتصفح: http://localhost:${PORT}`);
    console.log(`🌐 رابط API للفرونت إند: https://bs-project-zi1d.onrender.com`);
    console.log(`🔗 متصل مع: https://stunning-sprite-197909.netlify.app`);
});
