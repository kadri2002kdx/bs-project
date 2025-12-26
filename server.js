// server.js
const app = require('./app');
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`🚀 خادم المحاكاة الزراعية يعمل على المنفذ ${PORT}`);
    console.log(`🌱 المتصفح: http://localhost:${PORT}`);
});