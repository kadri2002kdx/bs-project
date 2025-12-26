// server_simple.js
const express = require('express');
const app = express();
const PORT = 3000;

// دالة dataService مبسطة
const createDataService = () => {
    console.log('تهيئة خدمة البيانات...');
    return {
        loadJSON: async () => [],
        getPlantById: async () => ({ id: 1, name: 'قمح' }),
        getWilayaById: async () => ({ id: 1, name: 'الجزائر' }),
        getData: async () => ({})
    };
};

// دالة simulation مبسطة
const createSimulation = () => {
    console.log('تهيئة نموذج المحاكاة...');
    return {
        run: async () => ({
            simulation_id: 'sim_test',
            timestamp: new Date().toISOString(),
            kpis: { sustainability_index: 75 },
            economic: { profitability: 20 }
        })
    };
};

const dataService = createDataService();
const simulation = createSimulation();

// المسارات
app.use(express.json());

app.get('/', (req, res) => {
    res.json({
        success: true,
        message: 'نظام المحاكاة الزراعية الجزائرية',
        version: '1.0.0'
    });
});

app.post('/api/simulate', async (req, res) => {
    try {
        const result = await simulation.run(req.body);
        res.json({
            success: true,
            ...result
        });
    } catch (error) {
        res.status(500).json({
            success: false,
            message: error.message
        });
    }
});

app.listen(PORT, () => {
    console.log(`🚀 الخادم يعمل على http://localhost:${PORT}`);
});