// src/services/dataService.js
const path = require('path');
const fs = require('fs').promises;

class DataService {
    constructor() {
        this.dataDir = path.join(process.cwd(), 'data');
        this.cache = {};
        console.log('تهيئة خدمة البيانات...');
        
        // تعريف البيانات الافتراضية هنا لتجنب استدعاءات متكررة
        this.defaults = this.createDefaultData();
    }

    // إنشاء البيانات الافتراضية مرة واحدة في البداية
    createDefaultData() {
        return {
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
                    population: 2500000
                }
            ],
            'soils.json': [
                {
                    id: 1,
                    name: 'تربة طينية',
                    type: 'طينية',
                    water_holding_capacity_mm_m: 180
                }
            ],
            'water_systems.json': [
                {
                    id: 1,
                    name: 'ري بالتنقيط',
                    efficiency_percent: 90
                }
            ],
            'fertilizers.json': [
                {
                    id: 1,
                    name: 'يوريا 46%',
                    n_percent: 46
                }
            ],
            'kc_values.json': [],
            'economic_data.json': {
                "crop_prices": {
                    "قمح": 45000
                },
                "costs": {
                    "labor_per_hectare": 150000,
                    "fertilizer_per_kg": 45
                }
            }
        };
    }

    async loadJSON(fileName) {
        // استخدام الكاش لتحسين الأداء
        if (this.cache[fileName]) {
            return this.cache[fileName];
        }
        
        try {
            const filePath = path.join(this.dataDir, fileName);
            const data = await fs.readFile(filePath, 'utf8');
            const parsedData = JSON.parse(data);
            
            // تخزين في الكاش
            this.cache[fileName] = parsedData;
            
            console.log(`✅ تم تحميل ${fileName} بنجاح`);
            return parsedData;
            
        } catch (error) {
            console.error(`❌ خطأ في تحميل ${fileName}:`, error.message);
            
            // إرجاع بيانات افتراضية للطوارئ
            return this.getDefaultData(fileName);
        }
    }

    // استخدام البيانات الافتراضية المخزنة مسبقًا
    getDefaultData(fileName) {
        console.log(`⚠️ استخدام البيانات الافتراضية لـ ${fileName}`);
        return this.defaults[fileName] || [];
    }

    async getData() {
        try {
            console.log('📂 جاري تحميل جميع البيانات المرجعية...');
            
            const [
                plants,
                wilayas,
                soils,
                water_systems,
                fertilizers,
                kc_values,
                economic_data
            ] = await Promise.all([
                this.loadJSON('plants.json'),
                this.loadJSON('wilayas.json'),
                this.loadJSON('soils.json'),
                this.loadJSON('water_systems.json'),
                this.loadJSON('fertilizers.json'),
                this.loadJSON('kc_values.json'),
                this.loadJSON('economic_data.json')
            ]);
            
            console.log('✅ تم تحميل جميع البيانات بنجاح');
            
            return {
                plants,
                wilayas,
                soils,
                water_systems,
                fertilizers,
                kc_values,
                economic_data
            };
            
        } catch (error) {
            console.error('❌ خطأ في جلب جميع البيانات:', error.message);
            return this.getAllDefaultData();
        }
    }

    getAllDefaultData() {
        return {
            plants: this.defaults['plants.json'] || [],
            wilayas: this.defaults['wilayas.json'] || [],
            soils: this.defaults['soils.json'] || [],
            water_systems: this.defaults['water_systems.json'] || [],
            fertilizers: this.defaults['fertilizers.json'] || [],
            kc_values: this.defaults['kc_values.json'] || [],
            economic_data: this.defaults['economic_data.json'] || {}
        };
    }

    async getPlantById(id) {
        const plants = await this.loadJSON('plants.json');
        const plant = plants.find(p => p.id === parseInt(id));
        
        if (!plant) {
            return this.defaults['plants.json'][0];
        }
        
        return plant;
    }

    async getWilayaById(id) {
        const wilayas = await this.loadJSON('wilayas.json');
        const wilaya = wilayas.find(w => w.id === parseInt(id));
        
        if (!wilaya) {
            return this.defaults['wilayas.json'][0];
        }
        
        return wilaya;
    }

    async getSoilById(id) {
        const soils = await this.loadJSON('soils.json');
        const soil = soils.find(s => s.id === parseInt(id));
        
        if (!soil) {
            return this.defaults['soils.json'][0];
        }
        
        return soil;
    }

    async getWaterSystemById(id) {
        const waterSystems = await this.loadJSON('water_systems.json');
        const waterSystem = waterSystems.find(ws => ws.id === parseInt(id));
        
        if (!waterSystem) {
            return this.defaults['water_systems.json'][0];
        }
        
        return waterSystem;
    }

    async getFertilizerById(id) {
        const fertilizers = await this.loadJSON('fertilizers.json');
        const fertilizer = fertilizers.find(f => f.id === parseInt(id));
        
        if (!fertilizer) {
            return this.defaults['fertilizers.json'][0];
        }
        
        return fertilizer;
    }

    async getKcValues(plantId) {
        const kcValues = await this.loadJSON('kc_values.json');
        return kcValues.filter(kc => kc.plant_id === parseInt(plantId));
    }

    async initialize() {
        console.log('🔧 تهيئة خدمة البيانات...');
        await this.getData();
        console.log('✅ اكتملت تهيئة خدمة البيانات');
    }
}

// إنشاء وتصدير نسخة واحدة من الخدمة (Singleton)
const dataService = new DataService();

// تهيئة الخدمة عند التحميل
dataService.initialize().catch(console.error);

module.exports = dataService;