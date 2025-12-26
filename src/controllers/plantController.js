const Plant = require('../models/Plant');

const plantModel = new Plant();

exports.getAllPlants = async (req, res) => {
  try {
    const plants = await plantModel.findAll();
    res.json({
      success: true,
      count: plants.length,
      data: plants
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'خطأ في جلب البيانات',
      error: error.message
    });
  }
};

exports.getPlantById = async (req, res) => {
  try {
    const plant = await plantModel.findById(req.params.id);
    
    if (!plant) {
      return res.status(404).json({
        success: false,
        message: 'النبات غير موجود'
      });
    }
    
    res.json({
      success: true,
      data: plant
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'خطأ في جلب النبات',
      error: error.message
    });
  }
};

exports.createPlant = async (req, res) => {
  try {
    const newPlant = await plantModel.create(req.body);
    
    res.status(201).json({
      success: true,
      message: 'تم إنشاء النبات بنجاح',
      data: newPlant
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'خطأ في إنشاء النبات',
      error: error.message
    });
  }
};

exports.updatePlant = async (req, res) => {
  try {
    const updatedPlant = await plantModel.update(req.params.id, req.body);
    
    if (!updatedPlant) {
      return res.status(404).json({
        success: false,
        message: 'النبات غير موجود'
      });
    }
    
    res.json({
      success: true,
      message: 'تم تحديث النبات بنجاح',
      data: updatedPlant
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'خطأ في تحديث النبات',
      error: error.message
    });
  }
};

exports.deletePlant = async (req, res) => {
  try {
    const deleted = await plantModel.delete(req.params.id);
    
    if (!deleted) {
      return res.status(404).json({
        success: false,
        message: 'النبات غير موجود'
      });
    }
    
    res.json({
      success: true,
      message: 'تم حذف النبات بنجاح'
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'خطأ في حذف النبات',
      error: error.message
    });
  }
};

exports.getPlantsBySoil = async (req, res) => {
  try {
    const plants = await plantModel.findBySoilType(req.params.soilId);
    
    res.json({
      success: true,
      count: plants.length,
      data: plants
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'خطأ في جلب النباتات حسب نوع التربة',
      error: error.message
    });
  }
};