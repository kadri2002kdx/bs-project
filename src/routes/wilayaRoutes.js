const express = require('express');
const router = express.Router();
const wilayaController = require('../controllers/wilayaController');

// الحصول على جميع الولايات
router.get('/', wilayaController.getAllWilayas);

// الحصول على ولاية محددة
router.get('/:id', wilayaController.getWilayaById);

module.exports = router;