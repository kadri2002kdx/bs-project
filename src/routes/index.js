const express = require('express');
const router = express.Router();
const simulationController = require('../controllers/simulationController');
// استيراد route التقرير
const reportRoute = require('./report');

/* ===============================
   مسارات التقرير
================================ */
router.use('/', reportRoute);  // سيكون المسار النهائي: POST /api/report

/* ===============================
   الصفحة الرئيسية
================================ */
router.get('/', (req, res) => {
    res.json({
        success: true,
        message: 'مرحباً بكم في نظام المحاكاة الزراعية الجزائرية',
        version: '2.0.0',
        endpoints: {
            health: 'GET /health',
            simulate: 'POST /simulate',
            simulations: 'GET /simulations',
            simulationById: 'GET /simulations/:id',
            plants: 'GET /plants',
            wilayas: 'GET /wilayas',
            soils: 'GET /soils',
            waterSystems: 'GET /water-systems',
            fertilizers: 'GET /fertilizers',
            economicData: 'GET /economic-data',
            generateReport: 'POST /report'  // ⬅️ أضفنا هذا
        }
    });
});
/* ===============================
   فحص حالة الخدمة
================================ */
router.get('/health', simulationController.health);

/* ===============================
   البيانات المرجعية
================================ */
router.get('/plants', simulationController.getPlants);
router.get('/wilayas', simulationController.getWilayas);
router.get('/soils', simulationController.getSoils);
router.get('/water-systems', simulationController.getWaterSystems);
router.get('/fertilizers', simulationController.getFertilizers);
router.get('/economic-data', simulationController.getEconomicData);

/* ===============================
   المحاكاة
================================ */
router.post('/simulate', simulationController.runSimulation);
router.get('/simulations', simulationController.getUserSimulations);
router.get('/simulations/:id', simulationController.getSimulationById);
router.delete('/simulations/:id', simulationController.deleteSimulation);

/* ===============================
   التحليل والتقارير
================================ */
router.post('/sensitivity', simulationController.analyzeSensitivity);
router.post('/compare', simulationController.compareScenarios);
router.get('/report/:id', simulationController.generateReport);
router.get('/statistics', simulationController.getStatistics);

/* ===============================
   التوثيق
================================ */
router.get('/docs/postman', (req, res) => {
    res.json({
        success: true,
        message: 'مجموعة Postman',
        link: 'https://www.postman.com/'
    });
});

router.get('/docs/swagger', (req, res) => {
    res.json({
        success: true,
        message: 'توثيق Swagger',
        status: 'قيد التطوير'
    });
});

/* ===============================
   404 — بدون * وبدون app
================================ */
router.use((req, res) => {
    res.status(404).json({
        success: false,
        message: 'المسار غير موجود',
        path: req.originalUrl
    });
});

module.exports = router;
