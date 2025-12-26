// src/routes/simulationRoutes.js
const express = require('express');
const router = express.Router();
const simulationController = require('../controllers/simulationController');

// جميع مسارات المحاكاة
router.get('/health', simulationController.health);
router.post('/simulate', simulationController.runSimulation);
router.get('/simulations/:id', simulationController.getSimulationById);
router.get('/simulations', simulationController.getUserSimulations);
router.post('/sensitivity', simulationController.analyzeSensitivity);
router.get('/report/:id', simulationController.generateReport);
router.post('/compare', simulationController.compareScenarios);
router.delete('/simulations/:id', simulationController.deleteSimulation);
router.get('/statistics', simulationController.getStatistics);

// مسارات البيانات المرجعية
router.get('/plants', async (req, res) => {
    try {
        const dataService = require('../../../services/dataService');
        const plants = await dataService.loadJSON('plants.json');
        res.json({ success: true, data: plants });
    } catch (error) {
        res.status(500).json({ success: false, message: error.message });
    }
});

router.get('/wilayas', async (req, res) => {
    try {
        const dataService = require('../../services/dataService');
        const wilayas = await dataService.loadJSON('wilayas.json');
        res.json({ success: true, data: wilayas });
    } catch (error) {
        res.status(500).json({ success: false, message: error.message });
    }
});

router.get('/soils', async (req, res) => {
    try {
        const dataService = require('../../services/dataService');
        const soils = await dataService.loadJSON('soils.json');
        res.json({ success: true, data: soils });
    } catch (error) {
        res.status(500).json({ success: false, message: error.message });
    }
});

router.get('/water-systems', async (req, res) => {
    try {
        const dataService = require('../../services/dataService');
        const waterSystems = await dataService.loadJSON('water_systems.json');
        res.json({ success: true, data: waterSystems });
    } catch (error) {
        res.status(500).json({ success: false, message: error.message });
    }
});

router.get('/fertilizers', async (req, res) => {
    try {
        const dataService = require('../../services/dataService');
        const fertilizers = await dataService.loadJSON('fertilizers.json');
        res.json({ success: true, data: fertilizers });
    } catch (error) {
        res.status(500).json({ success: false, message: error.message });
    }
});

module.exports = router;