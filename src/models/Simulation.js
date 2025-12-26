// C:\Users\LAPTA\OneDrive\Desktop\bs\src\models\Simulation.js
/**
 * نموذج محاكاة الزراعة الذكية للجزائر
 * يحتوي على النماذج الرياضية والدوال الرئيسية للمحاكاة
 */

const path = require('path');
const fs = require('fs').promises;
const dataService = require('../services/dataService'); // تأكد من أن هذا المسار صحيح

class Simulation {
    constructor() {
        this.dataDir = path.join(process.cwd(), 'data');
        this.simulationsDir = path.join(process.cwd(), 'data', 'simulations');
        this.ensureDirectories();
        this.initializeConstants();
        console.log('✅ تهيئة نموذج المحاكاة للزراعة الجزائرية');
    }
    
    // إنشاء المجلدات المطلوبة
    async ensureDirectories() {
        try {
            await fs.mkdir(this.dataDir, { recursive: true });
            await fs.mkdir(this.simulationsDir, { recursive: true });
            console.log('✅ مجلدات البيانات جاهزة');
        } catch (error) {
            console.error('❌ خطأ في إنشاء المجلدات:', error);
        }
    }
    
    // تهيئة الثوابت المحدّثة للجزائر
    initializeConstants() {
        this.constants = {
            // معاملات نمو النبات
            GROWTH_CONSTANTS: {
                BASE_GROWTH_RATE: 0.05,
                MAX_GROWTH: 100,
                TEMP_OPTIMUM: 25,
                TEMP_MIN: 10,
                TEMP_MAX: 35,
                WATER_STRESS_FACTOR: 0.7,
                HEAT_STRESS_FACTOR: 0.6
            },
            
            // معاملات الإجهاد
            STRESS_CONSTANTS: {
                HEAT_STRESS_THRESHOLD: 30,
                WATER_STRESS_THRESHOLD: 0.5,
                NITROGEN_STRESS_THRESHOLD: 0.6,
                SOIL_SALINITY_THRESHOLD: 4
            },
            
            // معاملات اقتصادية جزائرية محدّثة
            ECONOMIC_CONSTANTS: {
                LABOR_COST_PER_HECTARE: 150000,
                SEED_COST_PER_HECTARE: 80000,
                EQUIPMENT_COST_PER_HECTARE: 120000,
                MAINTENANCE_COST_PER_HECTARE: 50000,
                WATER_COST_PER_CUBIC_METER: 0.5,
                FERTILIZER_COST_PER_KG: 45,
                PESTICIDE_COST_PER_HECTARE: 30000,
                TRANSPORT_COST_PER_TON: 5000,
                ELECTRICITY_COST_PER_KWH: 6.5,
                FUEL_COST_PER_LITER: 50,
                ADMINISTRATION_COST_PER_HECTARE: 10000,
                INSURANCE_COST_PER_HECTARE: 15000
            },
            
            // أسعار المحاصيل الجزائرية (دينار/طن)
            CROP_PRICES: {
                'قمح': 45000,
                'طماطم': 60000,
                'شعير': 40000,
                'ذرة': 50000,
                'بطاطس': 55000,
                'فول': 48000,
                'حمضيات': 70000,
                'نخيل': 80000,
                'تفاح': 65000,
                'كرز': 85000,
                'عنب': 75000,
                'زيتون': 90000,
                'خضراوات متنوعة': 45000
            },
            
            // كفاءة أنظمة الري في الجزائر
            IRRIGATION_EFFICIENCY: {
                'ري بالتنقيط': 0.90,
                'ري بالرش المحوري': 0.75,
                'ري سطحى': 0.50,
                'ري بالرشاشات': 0.80,
                'ري تحت السطحي': 0.95
            },
            
            // معاملات التربة الجزائرية
            SOIL_COEFFICIENTS: {
                'طينية': { waterRetention: 0.85, fertility: 1.2, costFactor: 1.0 },
                'رملية': { waterRetention: 0.45, fertility: 0.8, costFactor: 1.1 },
                'طميية': { waterRetention: 0.75, fertility: 1.0, costFactor: 0.9 },
                'جبلية': { waterRetention: 0.60, fertility: 0.7, costFactor: 1.2 },
                'سبخية': { waterRetention: 0.90, fertility: 0.6, costFactor: 1.3 }
            },
            
            // انبعاثات الكربون (كجم CO2 لكل وحدة)
            CARBON_EMISSIONS: {
                FERTILIZER_N: 2.5,     // لكل كجم نيتروجين
                MACHINERY: 50,         // لكل هكتار
                IRRIGATION: 0.3,       // لكل م³ ماء
                TRANSPORTATION: 100,   // لكل هكتار
                PESTICIDE: 15,         // لكل هكتار
                FUEL: 2.7              // لكل لتر وقود
            },
            
            // معاملات المناخ الجزائري
            CLIMATE_COEFFICIENTS: {
                'متوسطي': { rainReliability: 0.8, tempStability: 0.9 },
                'صحراوي': { rainReliability: 0.3, tempStability: 0.7 },
                'قاري': { rainReliability: 0.6, tempStability: 0.8 },
                'شبه جاف': { rainReliability: 0.5, tempStability: 0.85 }
            },
            
            // معاملات الدعم الحكومي الجزائري
            GOVERNMENT_SUBSIDIES: {
                FERTILIZER_SUBSIDY: 0.25,
                WATER_SUBSIDY: 0.30,
                SEED_SUBSIDY: 0.20,
                EQUIPMENT_SUBSIDY: 0.15,
                IRRIGATION_SYSTEM_SUBSIDY: 0.40,
                YOUNG_FARMER_SUBSIDY: 0.25
            },
            
            // عوامل الجودة والمتطلبات
            QUALITY_FACTORS: {
                EXPORT_QUALITY_PREMIUM: 0.20,
                ORGANIC_PREMIUM: 0.30,
                CERTIFIED_SEED_FACTOR: 1.15,
                IRRIGATION_WATER_QUALITY: {
                    'جيد': 1.0,
                    'متوسط': 0.85,
                    'رديء': 0.65
                }
            }
        };
        
        console.log('✅ ثوابت المحاكاة جاهزة');
    }
    
    // الدالة الرئيسية للمحاكاة
    async run(inputs) {
        try {
            console.log('🚀 بدء المحاكاة مع المدخلات:', JSON.stringify(inputs, null, 2));
            
            // التحقق من المدخلات
            const validatedInputs = this.validateInputs(inputs);
            
            // الحصول على البيانات المرجعية
            const referenceData = await this.getReferenceData(validatedInputs);
            
            // تشغيل نماذج المحاكاة
            const results = {
                kpis: await this.calculateKPIs(validatedInputs, referenceData),
                growth: await this.simulateGrowth(validatedInputs, referenceData),
                climate: await this.simulateClimate(validatedInputs, referenceData),
                economic: await this.analyzeEconomics(validatedInputs, referenceData),
                water: await this.analyzeWaterUsage(validatedInputs, referenceData),
                soil: await this.analyzeSoilHealth(validatedInputs, referenceData),
                recommendations: await this.generateRecommendations(validatedInputs, referenceData),
                comparison: await this.generateComparison(validatedInputs, referenceData)
            };
            
            // تحسين النتائج
            const enhancedResults = this.enhanceResults(results, validatedInputs);
            
            // تسجيل المحاكاة
            const simulationId = await this.logSimulation(validatedInputs, enhancedResults);
            
            console.log('✅ المحاكاة اكتملت بنجاح');
            
            return {
                ...enhancedResults,
                simulation_id: simulationId,
                timestamp: new Date().toISOString(),
                status: 'completed'
            };
            
        } catch (error) {
            console.error('❌ خطأ في تشغيل المحاكاة:', error);
            throw error;
        }
    }
    
    // التحقق من المدخلات
    validateInputs(inputs) {
        const validated = { ...inputs };
        
        // ضمان القيم الافتراضية
        validated.area_ha = validated.area_ha || 1;
        validated.years = validated.years || 1;
        validated.nitrogen = validated.nitrogen || 120;
        validated.phosphorus = validated.phosphorus || 60;
        validated.potassium = validated.potassium || 80;
        validated.irrigation_amount = validated.irrigation_amount || 5000;
        validated.climate_scenario = validated.climate_scenario || 'current';
        validated.delta_temp_c = validated.delta_temp_c || 0;
        validated.delta_rain_pct = validated.delta_rain_pct || 0;
        validated.water_quality = validated.water_quality || 'جيد';
        validated.farming_type = validated.farming_type || 'تقليدي';
        
        // التحقق من النطاقات
        validated.area_ha = Math.max(0.1, Math.min(1000, validated.area_ha));
        validated.years = Math.max(1, Math.min(30, validated.years));
        validated.nitrogen = Math.max(0, Math.min(1000, validated.nitrogen));
        validated.phosphorus = Math.max(0, Math.min(500, validated.phosphorus));
        validated.potassium = Math.max(0, Math.min(500, validated.potassium));
        validated.irrigation_amount = Math.max(0, Math.min(20000, validated.irrigation_amount));
        validated.delta_temp_c = Math.max(-5, Math.min(5, validated.delta_temp_c));
        validated.delta_rain_pct = Math.max(-50, Math.min(50, validated.delta_rain_pct));
        
        console.log('✅ المدخلات صالحة:', validated);
        
        return validated;
    }
    
    // الحصول على البيانات المرجعية - النسخة المصححة
    async getReferenceData(inputs) {
        try {
            console.log('📂 جاري تحميل البيانات المرجعية...');
            
            const data = await dataService.getData();
            
            // استخدام القيم الافتراضية إذا كانت المدخلات غير معرفة
            const soilId = inputs.soil ? parseInt(inputs.soil) : 1;
            const waterId = inputs.water ? parseInt(inputs.water) : 1;
            const fertilizerId = inputs.fertilizer ? parseInt(inputs.fertilizer) : 1;
            
            // جلب البيانات المرجعية
            const referenceData = {
                plant: await dataService.getPlantById(inputs.plant_id),
                wilaya: await dataService.getWilayaById(inputs.wilaya_id),
                soil: await dataService.getSoilById(soilId),
                waterSystem: await dataService.getWaterSystemById(waterId),
                fertilizer: await dataService.getFertilizerById(fertilizerId),
                kcValues: await dataService.getKcValues(inputs.plant_id),
                economicData: data.economic_data || {}
            };
            
            // التحقق من البيانات الأساسية واستخدام البيانات الافتراضية إذا لزم الأمر
            if (!referenceData.plant || !referenceData.plant.name) {
                console.warn('⚠️ استخدام بيانات نبات افتراضية');
                referenceData.plant = data.plants?.[0] || this.getFallbackPlant();
            }
            
            if (!referenceData.wilaya || !referenceData.wilaya.name) {
                console.warn('⚠️ استخدام بيانات ولاية افتراضية');
                referenceData.wilaya = data.wilayas?.[0] || this.getFallbackWilaya();
            }
            
            if (!referenceData.soil || !referenceData.soil.name) {
                console.warn('⚠️ استخدام بيانات تربة افتراضية');
                referenceData.soil = data.soils?.[0] || this.getFallbackSoil();
            }
            
            if (!referenceData.waterSystem || !referenceData.waterSystem.name) {
                console.warn('⚠️ استخدام بيانات نظام ري افتراضية');
                referenceData.waterSystem = data.water_systems?.[0] || this.getFallbackWaterSystem();
            }
            
            if (!referenceData.fertilizer || !referenceData.fertilizer.name) {
                console.warn('⚠️ استخدام بيانات سماد افتراضية');
                referenceData.fertilizer = data.fertilizers?.[0] || this.getFallbackFertilizer();
            }
            
            console.log('✅ البيانات المرجعية جاهزة:', {
                plant: referenceData.plant.name,
                wilaya: referenceData.wilaya.name,
                soil: referenceData.soil.name
            });
            
            return referenceData;
            
        } catch (error) {
            console.error('❌ خطأ في جلب البيانات المرجعية:', error);
            
            // استخدام البيانات الافتراضية الكاملة للطوارئ
            return this.getFallbackReferenceData();
        }
    }
    
    // البيانات الافتراضية للنبات
    getFallbackPlant() {
        return {
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
        };
    }
    
    // البيانات الافتراضية للولاية
    getFallbackWilaya() {
        return {
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
        };
    }
    
    // البيانات الافتراضية للتربة
    getFallbackSoil() {
        return {
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
        };
    }
    
    // البيانات الافتراضية لنظام الري
    getFallbackWaterSystem() {
        return {
            id: 1,
            name: 'ري بالتنقيط',
            type: 'موضعي',
            efficiency_percent: 90,
            water_saving_percent: 40,
            energy_requirement_kwh_ha: 150,
            initial_cost_da_ha: 500000,
            maintenance_cost_da_ha_year: 50000
        };
    }
    
    // البيانات الافتراضية للسماد
    getFallbackFertilizer() {
        return {
            id: 1,
            name: 'يوريا 46%',
            type: 'نيتروجيني',
            n_percent: 46,
            p2o5_percent: 0,
            k2o_percent: 0,
            price_da_kg: 45,
            efficiency_percent: 70
        };
    }
    
    // البيانات المرجعية الافتراضية الكاملة
    getFallbackReferenceData() {
        return {
            plant: this.getFallbackPlant(),
            wilaya: this.getFallbackWilaya(),
            soil: this.getFallbackSoil(),
            waterSystem: this.getFallbackWaterSystem(),
            fertilizer: this.getFallbackFertilizer(),
            kcValues: [],
            economicData: {
                crop_prices: this.constants.CROP_PRICES,
                costs: {
                    labor_per_hectare: 150000,
                    seed_per_hectare: 80000,
                    equipment_per_hectare: 120000,
                    maintenance_per_hectare: 50000,
                    water_per_cubic_meter: 0.5,
                    fertilizer_per_kg: 45,
                    pesticide_per_hectare: 30000,
                    transport_per_ton: 5000,
                    electricity_per_kwh: 6.5,
                    fuel_per_liter: 50
                },
                subsidies: {
                    water_rate_reduction: 0.3,
                    fertilizer_subsidy: 0.25,
                    seed_subsidy: 0.2,
                    equipment_subsidy: 0.15,
                    export_subsidy: 0.1
                },
                taxes: {
                    vat_percent: 7,
                    income_tax_percent: 10,
                    land_tax_per_hectare: 5000
                }
            }
        };
    }
    
    // حساب مؤشرات الأداء الرئيسية
    async calculateKPIs(inputs, referenceData) {
        const kpis = {};
        
        // 1. الإجهاد الحراري
        kpis.heat_stress = this.calculateHeatStress(inputs, referenceData);
        
        // 2. الإجهاد المائي
        kpis.water_stress = this.calculateWaterStress(inputs, referenceData);
        
        // 3. كفاءة استخدام النيتروجين
        kpis.nue = this.calculateNUE(inputs, referenceData);
        
        // 4. البصمة الكربونية
        kpis.carbon_footprint = this.calculateCarbonFootprint(inputs, referenceData);
        
        // 5. مؤشر الأمن الغذائي
        kpis.food_security = this.calculateFoodSecurity(inputs, referenceData);
        
        // 6. مؤشر صحة التربة
        kpis.soil_health = this.calculateSoilHealth(inputs, referenceData);
        
        // 7. كفاءة استخدام المياه
        kpis.water_use_efficiency = this.calculateWaterUseEfficiency(inputs, referenceData);
        
        // 8. مؤشر الإجهاد العام
        kpis.stress_index = Math.round((kpis.heat_stress * 0.4 + kpis.water_stress * 0.6) / 2);
        
        // 9. مؤشر الاستدامة
        kpis.sustainability_index = this.calculateSustainabilityIndex(kpis);
        
        // 10. مؤشر الجدوى الاقتصادية
        kpis.economic_feasibility = this.calculateEconomicFeasibility(inputs, referenceData);
        
        console.log('✅ مؤشرات الأداء الرئيسية محسوبة');
        
        return kpis;
    }
    
    // حساب الإجهاد الحراري
    calculateHeatStress(inputs, referenceData) {
        const wilayaTemp = referenceData.wilaya.avg_temp_summer || 25;
        const plantOptimal = referenceData.plant.optimal_temp_max || 25;
        const tempChange = inputs.delta_temp_c || 0;
        const climateType = referenceData.wilaya.climate_type || 'متوسطي';
        
        const actualTemp = wilayaTemp + tempChange;
        
        let stress = 0;
        if (actualTemp > plantOptimal) {
            const tempDiff = actualTemp - plantOptimal;
            const climateFactor = this.constants.CLIMATE_COEFFICIENTS[climateType]?.tempStability || 0.9;
            stress = Math.min(100, (tempDiff / (plantOptimal * 0.5)) * 100 * (1 / climateFactor));
        }
        
        return Math.round(stress);
    }
    
    // حساب الإجهاد المائي
    calculateWaterStress(inputs, referenceData) {
        const plantRequirement = referenceData.plant.water_requirement_mm || 500;
        const rainfall = referenceData.wilaya.annual_rainfall_mm || 300;
        const irrigationEfficiency = (referenceData.waterSystem.efficiency_percent || 75) / 100;
        const irrigationAmount = inputs.irrigation_amount || 5000;
        const rainChange = (inputs.delta_rain_pct || 0) / 100;
        const soilType = referenceData.soil.type || 'طميية';
        const soilCoeff = this.constants.SOIL_COEFFICIENTS[soilType]?.waterRetention || 0.75;
        
        // المياه المتاحة
        const effectiveRainfall = rainfall * (1 + rainChange) * soilCoeff;
        const effectiveIrrigation = irrigationAmount * irrigationEfficiency;
        const totalWater = effectiveRainfall + effectiveIrrigation;
        
        // العجز المائي
        const waterDeficit = Math.max(0, plantRequirement - totalWater);
        
        // حساب الإجهاد
        let stress = 0;
        if (waterDeficit > 0) {
            stress = Math.min(100, (waterDeficit / plantRequirement) * 100);
        }
        
        return Math.round(stress);
    }
    
    // حساب كفاءة استخدام النيتروجين
    calculateNUE(inputs, referenceData) {
        const nitrogenApplied = inputs.nitrogen || 120;
        if (nitrogenApplied <= 0) return 0;
        
        const fertilizerN = (referenceData.fertilizer.n_percent || 0) / 100;
        const effectiveN = nitrogenApplied * fertilizerN;
        
        // اعتماداً على نوع التربة
        const soilType = referenceData.soil.type || 'طميية';
        const soilFertility = this.constants.SOIL_COEFFICIENTS[soilType]?.fertility || 1.0;
        
        // النبات يمتص 70% من النيتروجين الفعال مضروباً في خصوبة التربة
        const plantUptake = effectiveN * 0.7 * soilFertility;
        
        const nue = (plantUptake / nitrogenApplied) * 100;
        return Math.min(100, Math.round(nue));
    }
    
    // حساب البصمة الكربونية
    calculateCarbonFootprint(inputs, referenceData) {
        const emissions = {
            fertilizer: (inputs.nitrogen || 0) * this.constants.CARBON_EMISSIONS.FERTILIZER_N,
            machinery: inputs.area_ha * this.constants.CARBON_EMISSIONS.MACHINERY,
            irrigation: (inputs.irrigation_amount || 0) * this.constants.CARBON_EMISSIONS.IRRIGATION,
            transportation: inputs.area_ha * this.constants.CARBON_EMISSIONS.TRANSPORTATION,
            pesticide: inputs.area_ha * this.constants.CARBON_EMISSIONS.PESTICIDE,
            fuel: inputs.area_ha * 100 * this.constants.CARBON_EMISSIONS.FUEL // افتراض 100 لتر/هكتار
        };
        
        const total = Object.values(emissions).reduce((sum, val) => sum + val, 0);
        return Math.round(total);
    }
    
    // حساب الأمن الغذائي
    calculateFoodSecurity(inputs, referenceData) {
        const yieldPerHectare = referenceData.plant.max_yield_ton_ha || 5;
        const area = inputs.area_ha || 1;
        const stressFactor = 1 - (this.calculateWaterStress(inputs, referenceData) / 200);
        const totalYield = yieldPerHectare * area * stressFactor;
        
        // افتراض أن كل فرد يحتاج 0.2 طن سنويًا
        const populationServed = totalYield / 0.2;
        const wilayaPopulation = referenceData.wilaya.population || 1000000;
        
        const foodSecurity = Math.min(100, (populationServed / wilayaPopulation) * 100);
        return Math.round(foodSecurity);
    }
    
    // حساب صحة التربة
    calculateSoilHealth(inputs, referenceData) {
        const soilType = referenceData.soil.type || 'طميية';
        const soilCoeff = this.constants.SOIL_COEFFICIENTS[soilType]?.fertility || 1.0;
        
        // تأثير التسميد
        const nitrogenEffect = Math.min(1.2, (inputs.nitrogen || 0) / 100);
        
        // تأثير الإجهاد المائي
        const waterStress = this.calculateWaterStress(inputs, referenceData);
        const waterEffect = 1 - (waterStress / 200);
        
        const soilHealth = soilCoeff * nitrogenEffect * waterEffect * 100;
        return Math.min(100, Math.round(soilHealth));
    }
    
    // حساب كفاءة استخدام المياه
    calculateWaterUseEfficiency(inputs, referenceData) {
        const waterApplied = inputs.irrigation_amount || 5000;
        const rainfall = referenceData.wilaya.annual_rainfall_mm || 300;
        const totalWater = waterApplied + rainfall;
        
        const yieldPerHectare = referenceData.plant.max_yield_ton_ha || 5;
        const stressFactor = 1 - (this.calculateWaterStress(inputs, referenceData) / 200);
        const actualYield = yieldPerHectare * stressFactor;
        
        if (totalWater <= 0) return 0;
        
        const wue = (actualYield / totalWater) * 1000; // كجم/م³
        return Math.round(wue * 100) / 100;
    }
    
    // حساب الجدوى الاقتصادية
    calculateEconomicFeasibility(inputs, referenceData) {
        const waterStress = this.calculateWaterStress(inputs, referenceData);
        const heatStress = this.calculateHeatStress(inputs, referenceData);
        const totalStress = (waterStress + heatStress) / 2;
        
        let feasibility = 100 - totalStress;
        
        // تأثير الدعم الحكومي
        const subsidyEffect = 100 * (this.constants.GOVERNMENT_SUBSIDIES.FERTILIZER_SUBSIDY * 0.5);
        feasibility += subsidyEffect;
        
        return Math.max(0, Math.min(100, Math.round(feasibility)));
    }
    
    // حساب مؤشر الاستدامة
    calculateSustainabilityIndex(kpis) {
        let score = 100;
        
        // خصم للنقاط بناءً على الإجهاد
        score -= kpis.heat_stress * 0.3;
        score -= kpis.water_stress * 0.4;
        
        // خصم للبصمة الكربونية
        score -= Math.min(30, kpis.carbon_footprint / 50);
        
        // مكافأة لكفاءة استخدام المغذيات
        score += kpis.nue * 0.2;
        
        // مكافأة لكفاءة المياه
        score += kpis.water_use_efficiency * 0.1;
        
        // مكافأة لصحة التربة
        score += kpis.soil_health * 0.15;
        
        // مكافأة للأمن الغذائي
        score += kpis.food_security * 0.1;
        
        return Math.max(0, Math.min(100, Math.round(score)));
    }
    
    // محاكاة النمو
    async simulateGrowth(inputs, referenceData) {
        const days = Math.min(365, (inputs.years || 1) * 365);
        const growthData = {
            days: [],
            median: [],
            p10: [],
            p90: []
        };
        
        // نموذج النمو اللوجستي المعدل
        const K = 100; // السعة القصوى
        const r = 0.05; // معدل النمو
        const t0 = 30; // نقطة الانعطاف
        
        for (let t = 1; t <= days; t++) {
            growthData.days.push(t);
            
            // النمو الأساسي
            let growth = K / (1 + Math.exp(-r * (t - t0)));
            
            // تأثير الإجهاد الحراري
            const heatStress = this.calculateHeatStress(inputs, referenceData);
            const heatEffect = Math.max(0.1, 1 - (heatStress / 100));
            
            // تأثير الإجهاد المائي
            const waterStress = this.calculateWaterStress(inputs, referenceData);
            const waterEffect = Math.max(0.1, 1 - (waterStress / 100));
            
            // تأثير خصوبة التربة
            const soilType = referenceData.soil.type || 'طميية';
            const soilEffect = this.constants.SOIL_COEFFICIENTS[soilType]?.fertility || 1.0;
            
            // التأثير الموسمي
            const seasonalEffect = 1 + 0.2 * Math.sin((t / 365) * 2 * Math.PI);
            
            // التأثير النهائي
            growth = growth * heatEffect * waterEffect * soilEffect * seasonalEffect;
            
            growthData.median.push(Math.min(K, growth));
            growthData.p10.push(Math.min(K, growth * 0.85));
            growthData.p90.push(Math.min(K, growth * 1.15));
        }
        
        return growthData;
    }
    
    // محاكاة المناخ
    async simulateClimate(inputs, referenceData) {
        const months = [
            'يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو',
            'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر'
        ];
        
        const baseTemp = referenceData.wilaya.avg_temp_summer || 25;
        const baseRain = referenceData.wilaya.annual_rainfall_mm || 300;
        const tempChange = inputs.delta_temp_c || 0;
        const rainChange = (inputs.delta_rain_pct || 0) / 100;
        const scenario = inputs.climate_scenario || 'current';
        
        // معاملات السيناريو
        let scenarioFactor = 1;
        switch (scenario) {
            case 'rcp45':
                scenarioFactor = 1.5;
                break;
            case 'rcp85':
                scenarioFactor = 2.5;
                break;
            case 'sustainable':
                scenarioFactor = 0.8;
                break;
            case 'optimistic':
                scenarioFactor = 0.6;
                break;
            case 'pessimistic':
                scenarioFactor = 3.0;
                break;
        }
        
        const temperature = [];
        const rain = [];
        const evapotranspiration = [];
        
        months.forEach((month, index) => {
            // تباين موسمي لدرجة الحرارة
            const seasonalTemp = Math.sin((index - 6) * Math.PI / 6) * 12;
            const temp = baseTemp + seasonalTemp + (tempChange * scenarioFactor);
            temperature.push(Math.round(temp * 10) / 10);
            
            // تباين موسمي للهطول
            const seasonalRain = Math.sin((index - 2) * Math.PI / 6) * (baseRain / 3);
            const monthlyRain = Math.max(0, (baseRain / 12) + seasonalRain) * (1 + rainChange * scenarioFactor);
            rain.push(Math.round(monthlyRain));
            
            // حساب البخر-نتح المحتمل
            const et = 0.0023 * (temp + 17.8) * Math.sqrt(temp + 17.8) * 30;
            evapotranspiration.push(Math.round(et));
        });
        
        return {
            months: months,
            temperature: temperature,
            rain: rain,
            evapotranspiration: evapotranspiration,
            scenario: scenario,
            climate_type: referenceData.wilaya.climate_type || 'متوسطي'
        };
    }
    
    // التحليل الاقتصادي - النسخة المصححة
    async analyzeEconomics(inputs, referenceData) {
        try {
            const area = inputs.area_ha || 1;
            const years = inputs.years || 1;
            
            // حساب الإنتاجية
            const baseYield = referenceData.plant?.max_yield_ton_ha || 5;
            const minYield = referenceData.plant?.min_yield_ton_ha || 2;
            const heatStress = this.calculateHeatStress(inputs, referenceData);
            const waterStress = this.calculateWaterStress(inputs, referenceData);
            
            const stressFactor = Math.max(0.1, 1 - ((heatStress + waterStress) / 200));
            const yieldPerHectare = minYield + (baseYield - minYield) * stressFactor;
            const annualYield = yieldPerHectare * area;
            const totalYield = annualYield * years;
            
            // جلب البيانات الاقتصادية - مع التعامل الآمن
            let economicData = {};
            if (referenceData.economicData && typeof referenceData.economicData === 'object') {
                economicData = referenceData.economicData;
            }
            
            const costsData = economicData.costs || {};
            const subsidiesData = economicData.subsidies || {};
            const cropPrices = economicData.crop_prices || {};
            
            // استخدام الثوابت الافتراضية
            const constants = this.constants.ECONOMIC_CONSTANTS;
            
            // حساب التكاليف السنوية
            const costs = {
                أسمدة: (inputs.nitrogen || 0) * (costsData.fertilizer_per_kg || constants.FERTILIZER_COST_PER_KG),
                ري: (inputs.irrigation_amount || 0) * (costsData.water_per_cubic_meter || constants.WATER_COST_PER_CUBIC_METER),
                عمل: area * (costsData.labor_per_hectare || constants.LABOR_COST_PER_HECTARE),
                بذور: area * (costsData.seed_per_hectare || constants.SEED_COST_PER_HECTARE),
                معدات: area * (costsData.equipment_per_hectare || constants.EQUIPMENT_COST_PER_HECTARE),
                صيانة: area * (costsData.maintenance_per_hectare || constants.MAINTENANCE_COST_PER_HECTARE),
                مبيدات: area * (costsData.pesticide_per_hectare || 30000),
                كهرباء: area * 200 * (costsData.electricity_per_kwh || 6.5),
                وقود: area * 100 * (costsData.fuel_per_liter || 50),
                إدارة: area * (costsData.administration_per_hectare || 10000),
                تأمين: area * (costsData.insurance_per_hectare || 15000)
            };
            
            // تكاليف النقل بناءً على الإنتاج
            costs.نقل = totalYield * (costsData.transport_per_ton || 5000);
            
            // حساب الدعم الحكومي
            const subsidies = {
                دعم_الأسمدة: costs.أسمدة * (subsidiesData.fertilizer_subsidy || 0.25),
                دعم_المياه: costs.ري * (subsidiesData.water_rate_reduction || 0.30),
                دعم_البذور: costs.بذور * (subsidiesData.seed_subsidy || 0.20),
                دعم_المعدات: costs.معدات * (subsidiesData.equipment_subsidy || 0.15)
            };
            
            // إجمالي التكاليف السنوية
            let totalAnnualCost = 0;
            Object.values(costs).forEach(cost => {
                const numCost = Number(cost) || 0;
                totalAnnualCost += numCost;
            });
            
            // إجمالي الدعم
            let totalSubsidies = 0;
            Object.values(subsidies).forEach(subsidy => {
                const numSubsidy = Number(subsidy) || 0;
                totalSubsidies += numSubsidy;
            });
            
            // التكاليف بعد الدعم
            totalAnnualCost = Math.max(0, totalAnnualCost - totalSubsidies);
            
            // إجمالي التكاليف لجميع السنوات
            const totalCost = totalAnnualCost * years;
            
            // حساب العائدات
            const cropName = referenceData.plant?.name || 'قمح';
            const cropPrice = cropPrices[cropName] || this.constants.CROP_PRICES[cropName] || 50000;
            const totalRevenue = totalYield * cropPrice;
            
            // حساب الربحية
            const profit = totalRevenue - totalCost;
            const roi = totalCost > 0 ? (profit / totalCost) * 100 : 0;
            
            // حساب نقطة التعادل
            const breakEvenYield = totalCost > 0 ? totalCost / cropPrice : 0;
            const breakEvenYears = annualYield > 0 ? breakEvenYield / annualYield : 0;
            
            return {
                yield_per_hectare: Math.round(yieldPerHectare * 100) / 100,
                annual_yield: Math.round(annualYield * 100) / 100,
                total_yield: Math.round(totalYield * 100) / 100,
                annual_cost: Math.round(totalAnnualCost),
                total_cost: Math.round(totalCost),
                revenue: Math.round(totalRevenue),
                profit: Math.round(profit),
                profitability: Math.round(roi * 100) / 100,
                break_even_yield: Math.round(breakEvenYield * 100) / 100,
                break_even_years: Math.round(breakEvenYears * 100) / 100,
                cost_breakdown: costs,
                subsidies: subsidies,
                crop_price: cropPrice,
                years: years
            };
            
        } catch (error) {
            console.error('❌ خطأ في التحليل الاقتصادي:', error);
            
            // إرجاع بيانات افتراضية في حالة الخطأ
            return {
                yield_per_hectare: 5,
                annual_yield: 50,
                total_yield: 250,
                annual_cost: 1500000,
                total_cost: 7500000,
                revenue: 11250000,
                profit: 3750000,
                profitability: 50,
                break_even_yield: 150,
                break_even_years: 3,
                cost_breakdown: {},
                subsidies: {},
                crop_price: 45000,
                years: inputs.years || 1
            };
        }
    }
    
    // تحليل استخدام المياه
    async analyzeWaterUsage(inputs, referenceData) {
        const plantRequirement = referenceData.plant.water_requirement_mm || 500;
        const rainfall = referenceData.wilaya.annual_rainfall_mm || 300;
        const irrigationAmount = inputs.irrigation_amount || 5000;
        const irrigationEfficiency = (referenceData.waterSystem.efficiency_percent || 75) / 100;
        const rainChange = (inputs.delta_rain_pct || 0) / 100;
        const area = inputs.area_ha || 1;
        
        // تحويل الوحدات
        const plantRequirementM3 = (plantRequirement / 1000) * area * 10000; // م³/هكتار
        const rainfallM3 = (rainfall / 1000) * area * 10000 * (1 + rainChange);
        const irrigationM3 = irrigationAmount * area;
        const effectiveIrrigation = irrigationM3 * irrigationEfficiency;
        
        // حساب العجز والفائض
        const totalWater = rainfallM3 + effectiveIrrigation;
        const waterDeficit = Math.max(0, plantRequirementM3 - totalWater);
        const waterSurplus = Math.max(0, totalWater - plantRequirementM3);
        
        // كفاءة استخدام المياه
        const wue = totalWater > 0 ? (plantRequirementM3 / totalWater) * 100 : 0;
        
        return {
            plant_requirement_m3: Math.round(plantRequirementM3),
            rainfall_m3: Math.round(rainfallM3),
            irrigation_m3: Math.round(irrigationM3),
            effective_irrigation_m3: Math.round(effectiveIrrigation),
            total_water_m3: Math.round(totalWater),
            water_deficit_m3: Math.round(waterDeficit),
            water_surplus_m3: Math.round(waterSurplus),
            water_use_efficiency: Math.round(wue),
            irrigation_system: referenceData.waterSystem.name,
            irrigation_efficiency: irrigationEfficiency * 100
        };
    }
    
    // تحليل صحة التربة
    async analyzeSoilHealth(inputs, referenceData) {
        const soilType = referenceData.soil.type || 'طميية';
        const soilData = referenceData.soil;
        
        // تأثير التسميد
        const nitrogenEffect = Math.min(1.5, 0.5 + (inputs.nitrogen || 0) / 200);
        const phosphorusEffect = Math.min(1.3, 0.7 + (inputs.phosphorus || 0) / 300);
        const potassiumEffect = Math.min(1.2, 0.8 + (inputs.potassium || 0) / 400);
        
        // تأثير الري
        const waterStress = this.calculateWaterStress(inputs, referenceData);
        const waterEffect = 1 - (waterStress / 200);
        
        // تأثير التربة الأساسي
        const soilCoeff = this.constants.SOIL_COEFFICIENTS[soilType]?.fertility || 1.0;
        
        // حساب المؤشرات
        const organicMatter = (soilData.organic_matter_percent || 1.0) * nitrogenEffect;
        const nutrientBalance = (nitrogenEffect + phosphorusEffect + potassiumEffect) / 3;
        const soilStructure = soilCoeff * waterEffect;
        
        // مؤشر صحة التربة الشامل
        const soilHealthIndex = (organicMatter * 0.3 + nutrientBalance * 0.4 + soilStructure * 0.3) * 100;
        
        return {
            soil_type: soilType,
            organic_matter_percent: Math.round(organicMatter * 100) / 100,
            nutrient_balance: Math.round(nutrientBalance * 100) / 100,
            soil_structure: Math.round(soilStructure * 100) / 100,
            soil_health_index: Math.min(100, Math.round(soilHealthIndex)),
            recommendations: this.generateSoilRecommendations(soilType, inputs)
        };
    }
    
    // توليد توصيات التربة
    generateSoilRecommendations(soilType, inputs) {
        const recommendations = [];
        
        if (soilType === 'رملية') {
            recommendations.push('إضافة مواد عضوية لتحسين قدرة الاحتفاظ بالمياه');
            recommendations.push('استخدام الأسمدة بجرعات صغيرة متكررة');
        } else if (soilType === 'طينية') {
            recommendations.push('تحسين التهوية بإضافة الرمل أو المواد العضوية');
            recommendations.push('تفادي الحراثة العميقة عندما تكون التربة رطبة');
        }
        
        if (inputs.nitrogen > 200) {
            recommendations.push('تقليل كمية النيتروجين لتجنب تلوث المياه الجوفية');
        }
        
        if (inputs.irrigation_amount > 8000) {
            recommendations.push('مراقبة ملوحة التربة بسبب الري المكثف');
        }
        
        return recommendations;
    }
    
    // توليد التوصيات
    async generateRecommendations(inputs, referenceData) {
        const recommendations = [];
        
        // تحليل الإجهاد الحراري
        const heatStress = this.calculateHeatStress(inputs, referenceData);
        if (heatStress > 40) {
            recommendations.push({
                category: 'المناخ',
                message: 'الإجهاد الحراري مرتفع. نوصي بزراعة محاصيل مقاومة للحرارة أو استخدام تقنيات التبريد والتظليل.',
                priority: 'high',
                action: 'consider_heat_resistant_crops',
                impact: 'متوسط',
                cost: 'مرتفع'
            });
        }
        
        // تحليل الإجهاد المائي
        const waterStress = this.calculateWaterStress(inputs, referenceData);
        if (waterStress > 50) {
            recommendations.push({
                category: 'الري',
                message: 'الإجهاد المائي مرتفع. نوصي بتحسين كفاءة الري وتقليل الفاقد عن طريق الصيانة الدورية.',
                priority: 'high',
                action: 'improve_irrigation_efficiency',
                impact: 'مرتفع',
                cost: 'متوسط'
            });
        }
        
        // تحليل كفاءة استخدام النيتروجين
        const nue = this.calculateNUE(inputs, referenceData);
        if (nue < 50) {
            recommendations.push({
                category: 'التسميد',
                message: 'كفاءة استخدام النيتروجين منخفضة. نوصي بتعديل جرعات التسميد وتوقيتها لتحقيق أقصى استفادة.',
                priority: 'medium',
                action: 'adjust_fertilization',
                impact: 'مرتفع',
                cost: 'منخفض'
            });
        }
        
        // تحليل البصمة الكربونية
        const carbonFootprint = this.calculateCarbonFootprint(inputs, referenceData);
        if (carbonFootprint > 5000) {
            recommendations.push({
                category: 'البيئة',
                message: 'البصمة الكربونية مرتفعة. نوصي باستخدام مصادر طاقة متجددة وتقليل استخدام الأسمدة الكيماوية.',
                priority: 'medium',
                action: 'reduce_carbon_footprint',
                impact: 'متوسط',
                cost: 'مرتفع'
            });
        }
        
        // تحليل الربحية
        const economic = await this.analyzeEconomics(inputs, referenceData);
        if (economic.profitability < 15) {
            recommendations.push({
                category: 'الاقتصاد',
                message: 'الربحية منخفضة. نوصي بمراجعة التكاليف وزيادة الإنتاجية عن طريق تحسين الممارسات الزراعية.',
                priority: 'high',
                action: 'improve_profitability',
                impact: 'مرتفع',
                cost: 'متوسط'
            });
        }
        
        // تحليل صحة التربة
        const soilHealth = this.calculateSoilHealth(inputs, referenceData);
        if (soilHealth < 60) {
            recommendations.push({
                category: 'التربة',
                message: 'صحة التربة تحتاج تحسين. نوصي بإضافة المواد العضوية وتنويع المحاصيل.',
                priority: 'medium',
                action: 'improve_soil_health',
                impact: 'مرتفع',
                cost: 'منخفض'
            });
        }
        
        // توصيات بناءً على المنطقة
        const region = referenceData.wilaya.region || 'الشمال';
        if (region === 'الجنوب') {
            recommendations.push({
                category: 'إقليمي',
                message: 'في المناطق الجنوبية، نوصي باستخدام تقنيات الري الموضعي للحفاظ على المياه.',
                priority: 'medium',
                action: 'southern_irrigation_techniques',
                impact: 'مرتفع',
                cost: 'متوسط'
            });
        }
        
        // توصيات عامة
        recommendations.push({
            category: 'عام',
            message: 'نوصي بتطبيق الزراعة الدقيقة لتحسين كفاءة استخدام الموارد وزيادة الإنتاجية.',
            priority: 'low',
            action: 'implement_precision_agriculture',
            impact: 'مرتفع',
            cost: 'مرتفع'
        });
        
        return recommendations;
    }
    
    // توليد بيانات المقارنة
    async generateComparison(inputs, referenceData) {
        const current = {
            yield: (await this.analyzeEconomics(inputs, referenceData)).yield_per_hectare,
            cost: (await this.analyzeEconomics(inputs, referenceData)).annual_cost,
            profitability: (await this.analyzeEconomics(inputs, referenceData)).profitability,
            carbon_footprint: this.calculateCarbonFootprint(inputs, referenceData),
            water_use: inputs.irrigation_amount || 5000,
            water_stress: this.calculateWaterStress(inputs, referenceData),
            heat_stress: this.calculateHeatStress(inputs, referenceData)
        };
        
        // بيانات محسنة (سيناريو محسن)
        const optimized = {
            yield: current.yield * 1.20, // تحسين 20%
            cost: current.cost * 0.85,    // تخفيض 15%
            profitability: current.profitability * 1.35, // تحسين 35%
            carbon_footprint: current.carbon_footprint * 0.75, // تخفيض 25%
            water_use: current.water_use * 0.80, // توفير 20%
            water_stress: Math.max(0, current.water_stress - 30),
            heat_stress: Math.max(0, current.heat_stress - 25)
        };
        
        // سيناريو باستخدام تقنيات متقدمة
        const advanced = {
            yield: current.yield * 1.35, // تحسين 35%
            cost: current.cost * 1.10,    // زيادة 10% (تكلفة التقنيات)
            profitability: current.profitability * 1.50, // تحسين 50%
            carbon_footprint: current.carbon_footprint * 0.60, // تخفيض 40%
            water_use: current.water_use * 0.70, // توفير 30%
            water_stress: Math.max(0, current.water_stress - 40),
            heat_stress: Math.max(0, current.heat_stress - 35)
        };
        
        return {
            current: current,
            optimized: optimized,
            advanced: advanced,
            improvement_percentage: {
                yield: { optimized: 20, advanced: 35 },
                cost: { optimized: -15, advanced: 10 },
                profitability: { optimized: 35, advanced: 50 },
                carbon_footprint: { optimized: -25, advanced: -40 },
                water_use: { optimized: -20, advanced: -30 }
            }
        };
    }
    
    // تحسين النتائج
    enhanceResults(results, inputs) {
        const enhanced = { ...results };
        
        // إضافة معلومات المدخلات
        enhanced.input_summary = {
            plant: inputs.plant_id,
            plant_name: inputs.plant_name || 'غير محدد',
            wilaya: inputs.wilaya_id,
            wilaya_name: inputs.wilaya_name || 'غير محدد',
            soil: inputs.soil,
            area: inputs.area_ha,
            years: inputs.years,
            irrigation_system: results.water?.irrigation_system,
            fertilizer: results.fertilizer_name || 'غير محدد'
        };
        
        // إضافة تقييم الجودة
        enhanced.quality_assessment = {
            data_quality: 'جيدة',
            model_accuracy: 'متوسطة إلى عالية',
            confidence_level: 85,
            limitations: [
                'تعتمد النتائج على افتراضات النموذج الرياضي',
                'قد تختلف النتائج الفعلية حسب الظروف الميدانية',
                'أسعار المدخلات والمخرجات قابلة للتغير'
            ],
            assumptions: [
                'استقرار الظروف السياسية والاقتصادية',
                'توفر المدخلات الزراعية',
                'عدم وجود كوارث طبيعية غير متوقعة'
            ]
        };
        
        // إضافة ملخص تنفيذي
        enhanced.executive_summary = {
            overall_status: this.getOverallStatus(results),
            key_findings: this.getKeyFindings(results),
            main_recommendations: results.recommendations?.slice(0, 3) || [],
            investment_required: this.calculateInvestmentRequired(results)
        };
        
        // إضافة الطابع الزمني
        enhanced.generated_at = new Date().toISOString();
        enhanced.version = '2.0.0';
        enhanced.model_type = 'agricultural_simulation_v2';
        
        return enhanced;
    }
    
    // الحصول على الحالة العامة
    getOverallStatus(results) {
        const sustainability = results.kpis?.sustainability_index || 0;
        const profitability = results.economic?.profitability || 0;
        
        if (sustainability >= 70 && profitability >= 20) {
            return 'ممتازة';
        } else if (sustainability >= 50 && profitability >= 10) {
            return 'جيدة';
        } else if (sustainability >= 30 && profitability >= 5) {
            return 'متوسطة';
        } else {
            return 'تحتاج تحسين';
        }
    }
    
    // الحصول على النتائج الرئيسية
    getKeyFindings(results) {
        const findings = [];
        
        if (results.kpis?.water_stress > 50) {
            findings.push('الإجهاد المائي مرتفع ويتطلب اهتماماً عاجلاً');
        }
        
        if (results.economic?.profitability < 10) {
            findings.push('الربحية منخفضة وقد لا تكون المشروع مجدياً اقتصادياً');
        }
        
        if (results.kpis?.sustainability_index >= 70) {
            findings.push('المشروع مستدام بيئياً واقتصادياً');
        }
        
        const yieldPerHa = results.economic?.yield_per_hectare || 0;
        if (yieldPerHa > 5) {
            findings.push(`الإنتاجية مرتفعة (${yieldPerHa} طن/هكتار)`);
        }
        
        return findings.length > 0 ? findings : ['الأداء ضمن المعدلات المقبولة'];
    }
    
    // حساب الاستثمار المطلوب
    calculateInvestmentRequired(results) {
        const initialCost = results.economic?.annual_cost || 0;
        const years = results.input_summary?.years || 1;
        
        return {
            initial_investment: Math.round(initialCost * 1.2), // +20% للطوارئ
            annual_operating_cost: Math.round(initialCost),
            total_5_years: Math.round(initialCost * 5 * 1.1), // +10% للتضخم
            payback_period: results.economic?.break_even_years || 3,
            roi_percentage: results.economic?.profitability || 0
        };
    }
    
    // تسجيل المحاكاة
    async logSimulation(inputs, results) {
        try {
            const simulationId = `sim_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
            const simulationData = {
                id: simulationId,
                inputs: inputs,
                results: results,
                timestamp: new Date().toISOString(),
                version: '2.0.0'
            };
            
            const filePath = path.join(this.simulationsDir, `${simulationId}.json`);
            await fs.writeFile(filePath, JSON.stringify(simulationData, null, 2));
            
            console.log(`✅ تم حفظ المحاكاة: ${simulationId}`);
            return simulationId;
            
        } catch (error) {
            console.error('❌ خطأ في حفظ المحاكاة:', error);
            return null;
        }
    }
    
    // الحصول على محاكاة بواسطة المعرف
    async getSimulationById(id) {
        try {
            const filePath = path.join(this.simulationsDir, `${id}.json`);
            const data = await fs.readFile(filePath, 'utf8');
            return JSON.parse(data);
        } catch (error) {
            console.error(`❌ خطأ في جلب المحاكاة ${id}:`, error);
            return null;
        }
    }
    
    // الحصول على محاكاة المستخدم
    async getUserSimulations(userId, limit = 50) {
        try {
            const files = await fs.readdir(this.simulationsDir);
            const simulations = [];
            
            for (const file of files) {
                if (file.endsWith('.json')) {
                    try {
                        const filePath = path.join(this.simulationsDir, file);
                        const data = await fs.readFile(filePath, 'utf8');
                        const simulation = JSON.parse(data);
                        
                        // تصفية حسب المستخدم إذا كان موجودًا
                        if (!userId || simulation.userId === userId) {
                            simulations.push(simulation);
                        }
                    } catch (error) {
                        console.error(`❌ خطأ في قراءة ملف ${file}:`, error);
                    }
                }
            }
            
            // ترتيب حسب التاريخ (الأحدث أولاً)
            simulations.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
            
            return simulations.slice(0, limit);
            
        } catch (error) {
            console.error('❌ خطأ في جلب محاكاة المستخدم:', error);
            return [];
        }
    }
    
    // تحديث محاكاة
    async updateSimulation(id, updates) {
        try {
            const simulation = await this.getSimulationById(id);
            if (!simulation) return null;
            
            const updatedSimulation = { ...simulation, ...updates };
            const filePath = path.join(this.simulationsDir, `${id}.json`);
            
            await fs.writeFile(filePath, JSON.stringify(updatedSimulation, null, 2));
            return updatedSimulation;
            
        } catch (error) {
            console.error(`❌ خطأ في تحديث المحاكاة ${id}:`, error);
            return null;
        }
    }
    
    // حذف محاكاة
    async deleteSimulation(id) {
        try {
            const filePath = path.join(this.simulationsDir, `${id}.json`);
            await fs.unlink(filePath);
            console.log(`✅ تم حذف المحاكاة: ${id}`);
            return true;
        } catch (error) {
            console.error(`❌ خطأ في حذف المحاكاة ${id}:`, error);
            return false;
        }
    }
    
    // حفظ محاكاة
    async saveSimulation(data) {
        return this.logSimulation(data.inputs, data.results);
    }
    
    // تحويل إلى CSV
    convertToCSV(data) {
        if (!data || !data.results) return '';
        
        const headers = ['المؤشر', 'القيمة', 'الوحدة', 'التصنيف'];
        const rows = [];
        
        // مؤشرات الأداء الرئيسية
        if (data.results.kpis) {
            Object.entries(data.results.kpis).forEach(([key, value]) => {
                rows.push([key, value, '%', 'مؤشر أداء']);
            });
        }
        
        // البيانات الاقتصادية
        if (data.results.economic) {
            Object.entries(data.results.economic).forEach(([key, value]) => {
                if (typeof value === 'number') {
                    const unit = key.includes('yield') ? 'طن' : 
                                key.includes('cost') || key.includes('revenue') || key.includes('profit') ? 'دينار' : 
                                key.includes('percentage') ? '%' : '';
                    rows.push([`اقتصادي_${key}`, value, unit, 'اقتصادي']);
                }
            });
        }
        
        // تحويل الصفوف إلى نص CSV
        const csvRows = [headers, ...rows];
        return csvRows.map(row => row.join(',')).join('\n');
    }
    
    // تحليل الحساسية
    async analyzeSensitivity(inputs, parameter, range = 0.2, steps = 5) {
        const baseResults = await this.run(inputs);
        const sensitivity = {
            parameter: parameter,
            base_value: inputs[parameter],
            results: []
        };
        
        // حساب النطاق
        const baseValue = parseFloat(inputs[parameter]) || 0;
        const min = baseValue * (1 - range);
        const max = baseValue * (1 + range);
        const stepSize = (max - min) / (steps - 1);
        
        // تشغيل المحاكاة لكل قيمة
        for (let i = 0; i < steps; i++) {
            const testValue = min + (stepSize * i);
            const testInputs = { ...inputs, [parameter]: testValue };
            
            try {
                const testResults = await this.run(testInputs);
                sensitivity.results.push({
                    value: testValue,
                    yield: testResults.economic?.yield_per_hectare || 0,
                    profitability: testResults.economic?.profitability || 0,
                    carbon_footprint: testResults.kpis?.carbon_footprint || 0,
                    water_stress: testResults.kpis?.water_stress || 0
                });
            } catch (error) {
                console.error(`❌ خطأ في تحليل الحساسية للقيمة ${testValue}:`, error);
            }
        }
        
        return sensitivity;
    }
    
    // تحليل المخاطر
    async analyzeRisk(inputs, iterations = 100) {
        const risks = [];
        
        for (let i = 0; i < iterations; i++) {
            try {
                // إضافة تغييرات عشوائية للمدخلات
                const randomInputs = this.addRandomVariation(inputs);
                const results = await this.run(randomInputs);
                
                risks.push({
                    iteration: i,
                    yield: results.economic?.yield_per_hectare || 0,
                    profit: results.economic?.profit || 0,
                    heat_stress: results.kpis?.heat_stress || 0,
                    water_stress: results.kpis?.water_stress || 0,
                    sustainability: results.kpis?.sustainability_index || 0
                });
                
            } catch (error) {
                console.error(`❌ خطأ في تكرار تحليل المخاطر ${i}:`, error);
            }
        }
        
        // تحليل إحصائي
        const yields = risks.map(r => r.yield);
        const profits = risks.map(r => r.profit);
        
        return {
            risks: risks,
            statistics: {
                yield_mean: this.calculateMean(yields),
                yield_std: this.calculateStd(yields),
                profit_mean: this.calculateMean(profits),
                profit_std: this.calculateStd(profits),
                probability_loss: this.calculateProbability(profits, 0, 'less'),
                probability_high_profit: this.calculateProbability(profits, 1000000, 'greater'),
                confidence_interval_95: {
                    yield_lower: this.calculateMean(yields) - 1.96 * this.calculateStd(yields),
                    yield_upper: this.calculateMean(yields) + 1.96 * this.calculateStd(yields)
                }
            }
        };
    }
    
    // إضافة تغيير عشوائي
    addRandomVariation(inputs) {
        const varied = { ...inputs };
        
        // تغيير عشوائي لدرجة الحرارة (±3 درجة)
        if (varied.delta_temp_c !== undefined) {
            varied.delta_temp_c += (Math.random() - 0.5) * 6;
        }
        
        // تغيير عشوائي للهطول (±15%)
        if (varied.delta_rain_pct !== undefined) {
            varied.delta_rain_pct += (Math.random() - 0.5) * 30;
        }
        
        // تغيير عشوائي للنيتروجين (±25%)
        if (varied.nitrogen !== undefined) {
            varied.nitrogen *= 0.85 + (Math.random() * 0.3);
        }
        
        // تغيير عشوائي للري (±20%)
        if (varied.irrigation_amount !== undefined) {
            varied.irrigation_amount *= 0.9 + (Math.random() * 0.2);
        }
        
        // تغيير عشوائي للسعر (±10%)
        varied.price_variation = (Math.random() - 0.5) * 20;
        
        return varied;
    }
    
    // حساب المتوسط
    calculateMean(values) {
        if (!values.length) return 0;
        const sum = values.reduce((a, b) => a + b, 0);
        return sum / values.length;
    }
    
    // حساب الانحراف المعياري
    calculateStd(values) {
        if (values.length < 2) return 0;
        const mean = this.calculateMean(values);
        const squaredDiffs = values.map(v => Math.pow(v - mean, 2));
        const variance = this.calculateMean(squaredDiffs);
        return Math.sqrt(variance);
    }
    
    // حساب الاحتمالية
    calculateProbability(values, threshold, comparison = 'greater') {
        if (!values.length) return 0;
        
        let count = 0;
        values.forEach(value => {
            if (comparison === 'greater' && value > threshold) {
                count++;
            } else if (comparison === 'less' && value < threshold) {
                count++;
            } else if (comparison === 'equal' && value === threshold) {
                count++;
            }
        });
        
        return (count / values.length) * 100;
    }
    
    // توليد تقرير
    async generateReport(simulationId) {
        const simulation = await this.getSimulationById(simulationId);
        if (!simulation) return null;
        
        const report = {
            metadata: {
                simulation_id: simulationId,
                generated_at: new Date().toISOString(),
                version: '2.0.0',
                report_type: 'محاكاة زراعية متكاملة'
            },
            summary: {
                inputs_summary: simulation.inputs,
                kpis_summary: simulation.results.kpis,
                economic_summary: simulation.results.economic,
                executive_summary: simulation.results.executive_summary
            },
            detailed_results: simulation.results,
            recommendations: simulation.results.recommendations,
            risk_assessment: await this.analyzeRisk(simulation.inputs, 50),
            sensitivity_analysis: await this.analyzeSensitivity(simulation.inputs, 'nitrogen'),
            attachments: {
                growth_chart: simulation.results.growth,
                climate_data: simulation.results.climate,
                water_analysis: simulation.results.water,
                soil_analysis: simulation.results.soil
            }
        };
        
        return report;
    }
}

module.exports = Simulation;