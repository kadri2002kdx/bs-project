const express = require('express');
const router = express.Router();
const plantController = require('../controllers/plantController');

// الحصول على جميع النباتات
router.get('/', plantController.getAllPlants);

// الحصول على نبات محدد
router.get('/:id', plantController.getPlantById);

// إنشاء نبات جديد
router.post('/', plantController.createPlant);

// تحديث نبات
router.put('/:id', plantController.updatePlant);

// حذف نبات
router.delete('/:id', plantController.deletePlant);

// الحصول على النباتات حسب نوع التربة
router.get('/soil/:soilId', plantController.getPlantsBySoil);

module.exports = router;