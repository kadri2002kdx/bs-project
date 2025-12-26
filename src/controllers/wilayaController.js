const Wilaya = require('../models/Wilaya');

const wilayaModel = new Wilaya();

exports.getAllWilayas = async (req, res) => {
  try {
    const wilayas = await wilayaModel.findAll();
    res.json({
      success: true,
      count: wilayas.length,
      data: wilayas
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'خطأ في جلب البيانات',
      error: error.message
    });
  }
};

exports.getWilayaById = async (req, res) => {
  try {
    const wilaya = await wilayaModel.findById(req.params.id);
    
    if (!wilaya) {
      return res.status(404).json({
        success: false,
        message: 'الولاية غير موجودة'
      });
    }
    
    res.json({
      success: true,
      data: wilaya
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'خطأ في جلب الولاية',
      error: error.message
    });
  }
};