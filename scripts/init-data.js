const fs = require('fs').promises;
const path = require('path');

async function initializeData() {
    try {
        const dataDir = path.join(__dirname, '..', 'data');
        
        // إنشاء مجلد البيانات إذا لم يكن موجوداً
        await fs.mkdir(dataDir, { recursive: true });
        
        console.log('✅ تم إنشاء مجلد البيانات');
        
        // التحقق من وجود الملفات
        const requiredFiles = [
            'plants.json',
            'wilayas.json',
            'soils.json',
            'water_systems.json',
            'fertilizers.json',
            'kc_values.json',
            'economic_data.json'
        ];
        
        for (const file of requiredFiles) {
            const filePath = path.join(dataDir, file);
            try {
                await fs.access(filePath);
                console.log(`✅ ${file} موجود`);
            } catch (error) {
                console.warn(`⚠️ ${file} غير موجود - سيتم إنشاء ملف افتراضي`);
                
                // إنشاء بيانات افتراضية
                const defaultData = {
                    'plants.json': [
                        {
                            id: 1,
                            name: 'قمح',
                            scientific_name: 'Triticum aestivum',
                            water_requirement_mm: 450,
                            max_yield_ton_ha: 6.5,
                            min_yield_ton_ha: 2.5,
                            optimal_temp_min: 15,
                            optimal_temp_max: 25,
                            growth_cycle_days: 120,
                            harvest_index: 0.4,
                            nutrient_requirements: {
                                nitrogen_kg_ha: 150,
                                phosphorus_kg_ha: 60,
                                potassium_kg_ha: 80
                            }
                        }
                    ],
                    'wilayas.json': [
                        {
                            id: 1,
                            name: 'الجزائر',
                            code: 16,
                            region: 'الشمال',
                            climate_type: 'متوسطي',
                            avg_temp_summer: 28,
                            avg_temp_winter: 12,
                            annual_rainfall_mm: 650,
                            soil_types: ['طيني', 'طميي'],
                            agricultural_zones: ['سهول متيجة', 'هضاب'],
                            main_crops: ['قمح', 'شعير', 'طماطم', 'حمضيات'],
                            population: 2500000,
                            water_resources: ['سد حمرا', 'المياه الجوفية']
                        }
                    ],
                    'soils.json': [
                        {
                            id: 1,
                            name: 'تربة طينية',
                            type: 'طينية',
                            water_holding_capacity_mm_m: 180,
                            infiltration_rate_mm_h: 5,
                            field_capacity_percent: 35,
                            wilting_point_percent: 15,
                            ph_range: '6.0-7.5',
                            organic_matter_percent: 2.5,
                            nitrogen_content_percent: 0.15
                        }
                    ],
                    'water_systems.json': [
                        {
                            id: 1,
                            name: 'ري بالتنقيط',
                            type: 'موضعي',
                            efficiency_percent: 90,
                            water_saving_percent: 40,
                            energy_requirement_kwh_ha: 150,
                            initial_cost_da_ha: 500000,
                            maintenance_cost_da_ha_year: 50000
                        }
                    ],
                    'fertilizers.json': [
                        {
                            id: 1,
                            name: 'يوريا 46%',
                            type: 'نيتروجيني',
                            n_percent: 46,
                            p2o5_percent: 0,
                            k2o_percent: 0,
                            price_da_kg: 45,
                            efficiency_percent: 70
                        }
                    ],
                    'kc_values.json': [
                        {
                            plant_id: 1,
                            plant_name: 'قمح',
                            total_water_requirement_mm: 450
                        }
                    ],
                    'economic_data.json': {
                        crop_prices: { 'قمح': 45000 },
                        costs: { labor_per_hectare: 150000 },
                        subsidies: {},
                        taxes: {}
                    }
                };
                
                if (defaultData[file]) {
                    await fs.writeFile(filePath, JSON.stringify(defaultData[file], null, 2));
                    console.log(`✅ تم إنشاء ${file}`);
                }
            }
        }
        
        console.log('🎉 تم تهيئة البيانات بنجاح!');
        
    } catch (error) {
        console.error('❌ خطأ في تهيئة البيانات:', error);
    }
}

// تشغيل التهيئة إذا تم تنفيذ الملف مباشرة
if (require.main === module) {
    initializeData();
}

module.exports = initializeData;