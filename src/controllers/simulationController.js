/**
 * متحكم المحاكاة الزراعية المتكاملة
 * يستخدم نموذج المحاكاة المتقدم
 */

const DataService = require('../services/dataService');
const Simulation = require('../models/Simulation');

// إنشاء نسخة واحدة من نموذج المحاكاة
const simulation = new Simulation();

// تعريف الدوال المساعدة أولاً لتكون متاحة للاستخدام
function generateSensitivityRecommendations(sensitivity, parameter) {
    const recommendations = [];
    const results = sensitivity.results;
    
    if (results.length < 2) {
        return recommendations;
    }
    
    // حساب التدرج
    const startYield = results[0].yield;
    const endYield = results[results.length - 1].yield;
    const gradient = (endYield - startYield) / (results.length - 1);
    
    if (Math.abs(gradient) < 0.1) {
        recommendations.push(`المعامل ${parameter} ليس حساساً للتغيير ضمن النطاق المدروس`);
    } else if (gradient > 0.5) {
        recommendations.push(`المعامل ${parameter} حساس جداً. زيادة قليلة تؤدي إلى تحسن كبير في الإنتاجية`);
    } else if (gradient < -0.5) {
        recommendations.push(`المعامل ${parameter} حساس سلبياً. الزيادة تؤدي إلى انخفاض الإنتاجية`);
    }
    
    // العثور على القيمة المثلى
    const optimal = results.reduce((max, r) => r.profitability > max.profitability ? r : max, results[0]);
    recommendations.push(`القيمة المثلى المقترحة لـ ${parameter}: ${optimal.value.toFixed(2)}`);
    
    return recommendations;
}

function analyzeComparison(results) {
    const validResults = results.filter(r => !r.error && r.kpis && r.economic);
    
    if (validResults.length === 0) {
        return {
            best_scenario: null,
            recommendations: ['لا توجد نتائج صالحة للمقارنة']
        };
    }
    
    // العثور على أفضل سيناريو بناءً على الربحية والاستدامة
    let bestScenario = validResults[0];
    let bestScore = (validResults[0].economic.profitability * 0.6) + (validResults[0].kpis.sustainability_index * 0.4);
    
    for (let i = 1; i < validResults.length; i++) {
        const score = (validResults[i].economic.profitability * 0.6) + (validResults[i].kpis.sustainability_index * 0.4);
        if (score > bestScore) {
            bestScenario = validResults[i];
            bestScore = score;
        }
    }
    
    // توليد توصيات
    const recommendations = [];
    recommendations.push(`أفضل سيناريو: ${bestScenario.scenario_name} (نتيجة: ${bestScore.toFixed(1)})`);
    
    // مقارنة الربحية
    const profitabilityRanking = [...validResults].sort((a, b) => b.economic.profitability - a.economic.profitability);
    if (profitabilityRanking.length > 1) {
        recommendations.push(`أعلى ربحية: ${profitabilityRanking[0].scenario_name} (${profitabilityRanking[0].economic.profitability}%)`);
    }
    
    // مقارنة الاستدامة
    const sustainabilityRanking = [...validResults].sort((a, b) => b.kpis.sustainability_index - a.kpis.sustainability_index);
    if (sustainabilityRanking.length > 1) {
        recommendations.push(`أعلى استدامة: ${sustainabilityRanking[0].scenario_name} (${sustainabilityRanking[0].kpis.sustainability_index}%)`);
    }
    
    return {
        best_scenario: bestScenario,
        profitability_ranking: profitabilityRanking.map(r => ({
            scenario: r.scenario_name,
            profitability: r.economic.profitability
        })),
        sustainability_ranking: sustainabilityRanking.map(r => ({
            scenario: r.scenario_name,
            sustainability: r.kpis.sustainability_index
        })),
        recommendations: recommendations
    };
}

function getMostCommonValue(simulations, field) {
    const counts = {};
    simulations.forEach(sim => {
        const value = sim.inputs ? sim.inputs[field] : undefined;
        if (value !== undefined) {
            counts[value] = (counts[value] || 0) + 1;
        }
    });
    
    let maxCount = 0;
    let mostCommon = null;
    
    Object.entries(counts).forEach(([value, count]) => {
        if (count > maxCount) {
            maxCount = count;
            mostCommon = value;
        }
    });
    
    return mostCommon;
}

function calculateTrends(simulations) {
    if (simulations.length < 2) {
        return { profitability: 'ثابت', sustainability: 'ثابت' };
    }
    
    // ترتيب حسب التاريخ
    const sortedSimulations = [...simulations].sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));
    
    // تقسيم إلى مجموعتين: القديم والجديد
    const midpoint = Math.floor(sortedSimulations.length / 2);
    const oldSimulations = sortedSimulations.slice(0, midpoint);
    const newSimulations = sortedSimulations.slice(midpoint);
    
    // حساب المتوسطات
    const oldAvgProfit = oldSimulations.reduce((sum, s) => sum + (s.results && s.results.economic ? s.results.economic.profitability : 0), 0) / oldSimulations.length;
    const newAvgProfit = newSimulations.reduce((sum, s) => sum + (s.results && s.results.economic ? s.results.economic.profitability : 0), 0) / newSimulations.length;
    
    const oldAvgSustain = oldSimulations.reduce((sum, s) => sum + (s.results && s.results.kpis ? s.results.kpis.sustainability_index : 0), 0) / oldSimulations.length;
    const newAvgSustain = newSimulations.reduce((sum, s) => sum + (s.results && s.results.kpis ? s.results.kpis.sustainability_index : 0), 0) / newSimulations.length;
    
    // تحديد الاتجاه
    const getTrend = function(oldVal, newVal) {
        const change = newVal - oldVal;
        if (change > 5) return 'تصاعدي قوي';
        if (change > 2) return 'تصاعدي';
        if (change > -2) return 'ثابت';
        if (change > -5) return 'تنازلي';
        return 'تنازلي قوي';
    };
    
    return {
        profitability: getTrend(oldAvgProfit, newAvgProfit),
        sustainability: getTrend(oldAvgSustain, newAvgSustain),
        change_percentage: {
            profitability: ((newAvgProfit - oldAvgProfit) / (oldAvgProfit || 1) * 100).toFixed(1),
            sustainability: ((newAvgSustain - oldAvgSustain) / (oldAvgSustain || 1) * 100).toFixed(1)
        }
    };
}

// الآن نبدأ بتعريف دوال exports الرئيسية
exports.health = (req, res) => {
    res.json({
        success: true,
        status: 'خدمة المحاكاة الزراعية الجزائرية تعمل بشكل صحيح',
        version: '2.0.0',
        timestamp: new Date().toISOString(),
        features: [
            'محاكاة متكاملة للزراعة',
            'تحليل اقتصادي مفصّل',
            'تقييم استدامة',
            'توصيات ذكية',
            'تحليل المخاطر'
        ]
    });
};

exports.runSimulation = async (req, res) => {
    try {
        console.log('📥 استلام طلب محاكاة جديد');
        
        const {
            plant_id,
            wilaya_id,
            soil,
            water,
            fertilizer,
            area_ha,
            nitrogen,
            phosphorus,
            potassium,
            years,
            delta_temp_c = 0,
            delta_rain_pct = 0,
            climate_scenario = 'current',
            irrigation_amount = 5000,
            water_quality = 'جيد',
            farming_type = 'تقليدي',
            user_id,
            scenario_name
        } = req.body;

        // التحقق من المدخلات الأساسية
        if (!plant_id || !wilaya_id || !area_ha) {
            return res.status(400).json({
                success: false,
                message: 'البيانات الأساسية مطلوبة: معرف النبات، معرف الولاية، المساحة',
                required_fields: ['plant_id', 'wilaya_id', 'area_ha'],
                received: req.body
            });
        }

        // تجميع مدخلات المحاكاة
        const simulationInputs = {
            plant_id: parseInt(plant_id),
            wilaya_id: parseInt(wilaya_id),
            soil: parseInt(soil) || 1,
            water: parseInt(water) || 1,
            fertilizer: parseInt(fertilizer) || 1,
            area_ha: parseFloat(area_ha),
            nitrogen: parseFloat(nitrogen) || 120,
            phosphorus: parseFloat(phosphorus) || 60,
            potassium: parseFloat(potassium) || 80,
            years: parseInt(years) || 1,
            delta_temp_c: parseFloat(delta_temp_c),
            delta_rain_pct: parseFloat(delta_rain_pct),
            climate_scenario: climate_scenario,
            irrigation_amount: parseFloat(irrigation_amount),
            water_quality: water_quality,
            farming_type: farming_type,
            user_id: user_id,
            scenario_name: scenario_name || 'محاكاة رئيسية'
        };

        console.log('🔍 مدخلات المحاكاة:', JSON.stringify(simulationInputs, null, 2));

        // التحقق من صحة المدخلات
        if (simulationInputs.area_ha <= 0) {
            return res.status(400).json({
                success: false,
                message: 'المساحة يجب أن تكون أكبر من صفر'
            });
        }

        if (simulationInputs.years <= 0 || simulationInputs.years > 30) {
            return res.status(400).json({
                success: false,
                message: 'عدد السنوات يجب أن يكون بين 1 و 30 سنة'
            });
        }

        // التحقق من وجود البيانات المرجعية
        try {
            const plant = await DataService.getPlantById(plant_id);
            const wilaya = await DataService.getWilayaById(wilaya_id);
            
            if (!plant) {
                return res.status(404).json({
                    success: false,
                    message: `النبات بالمعرف ${plant_id} غير موجود`
                });
            }
            
            if (!wilaya) {
                return res.status(404).json({
                    success: false,
                    message: `الولاية بالمعرف ${wilaya_id} غير موجودة`
                });
            }
            
            // إضافة أسماء للمدخلات
            simulationInputs.plant_name = plant.name;
            simulationInputs.wilaya_name = wilaya.name;
            
        } catch (error) {
            console.error('❌ خطأ في جلب البيانات المرجعية:', error);
        }

        // تشغيل المحاكاة
        console.log('🚀 بدء تشغيل المحاكاة...');
        const startTime = Date.now();
        
        const results = await simulation.run(simulationInputs);
        
        const endTime = Date.now();
        const duration = (endTime - startTime) / 1000;
        
        console.log(`✅ اكتملت المحاكاة في ${duration} ثانية`);

        // إعداد الاستجابة
        const response = {
            success: true,
            message: 'تمت المحاكاة بنجاح',
            simulation_id: results.simulation_id,
            duration_seconds: duration,
            timestamp: results.timestamp,
            summary: {
                plant: simulationInputs.plant_name,
                wilaya: simulationInputs.wilaya_name,
                area: simulationInputs.area_ha + ' هكتار',
                years: simulationInputs.years + ' سنة',
                overall_status: results.executive_summary ? results.executive_summary.overall_status : 'غير محدد'
            },
            kpis_summary: {
                sustainability_index: results.kpis ? results.kpis.sustainability_index : 0,
                profitability: results.economic ? results.economic.profitability : 0,
                water_stress: results.kpis ? results.kpis.water_stress : 0,
                heat_stress: results.kpis ? results.kpis.heat_stress : 0
            },
            economic_summary: {
                annual_yield: results.economic ? results.economic.annual_yield : 0,
                annual_cost: results.economic ? results.economic.annual_cost : 0,
                annual_profit: results.economic && results.economic.profit ? results.economic.profit / simulationInputs.years : 0,
                break_even_years: results.economic ? results.economic.break_even_years : 0
            },
            recommendations_count: results.recommendations ? results.recommendations.length : 0,
            full_results: results
        };

        res.json(response);

    } catch (error) {
        console.error('❌ خطأ في المحاكاة:', error);
        res.status(500).json({
            success: false,
            message: 'حدث خطأ أثناء المحاكاة',
            error: process.env.NODE_ENV === 'development' ? error.message : 'خطأ داخلي في الخادم',
            stack: process.env.NODE_ENV === 'development' ? error.stack : undefined
        });
    }
};

exports.getSimulationById = async (req, res) => {
    try {
        const { id } = req.params;
        
        if (!id) {
            return res.status(400).json({
                success: false,
                message: 'معرف المحاكاة مطلوب'
            });
        }

        console.log(`🔍 جلب المحاكاة: ${id}`);
        
        const simulationData = await simulation.getSimulationById(id);
        
        if (!simulationData) {
            return res.status(404).json({
                success: false,
                message: 'المحاكاة غير موجودة'
            });
        }

        // إعداد استجابة مختصرة
        const response = {
            success: true,
            simulation: {
                id: simulationData.id,
                timestamp: simulationData.timestamp,
                inputs: simulationData.inputs,
                summary: {
                    kpis: simulationData.results.kpis,
                    economic: simulationData.results.economic,
                    executive_summary: simulationData.results.executive_summary
                },
                recommendations: simulationData.results.recommendations,
                quality_assessment: simulationData.results.quality_assessment
            }
        };

        res.json(response);
        
    } catch (error) {
        console.error('❌ خطأ في جلب المحاكاة:', error);
        res.status(500).json({
            success: false,
            message: 'حدث خطأ في جلب المحاكاة'
        });
    }
};

exports.getUserSimulations = async (req, res) => {
    try {
        const { userId } = req.query;
        const limit = parseInt(req.query.limit) || 20;
        const page = parseInt(req.query.page) || 1;
        
        console.log(`🔍 جلب محاكاة للمستخدم: ${userId || 'جميع المستخدمين'}`);
        
        const allSimulations = await simulation.getUserSimulations(userId, 1000);
        
        // التقسيم إلى صفحات
        const startIndex = (page - 1) * limit;
        const endIndex = page * limit;
        const paginatedSimulations = allSimulations.slice(startIndex, endIndex);
        
        // إنشاء ملخص لكل محاكاة
        const simulationsSummary = paginatedSimulations.map(sim => ({
            id: sim.id,
            timestamp: sim.timestamp,
            plant: sim.inputs.plant_name || `النبات ${sim.inputs.plant_id}`,
            wilaya: sim.inputs.wilaya_name || `الولاية ${sim.inputs.wilaya_id}`,
            area: sim.inputs.area_ha + ' هكتار',
            years: sim.inputs.years + ' سنة',
            profitability: sim.results.economic ? sim.results.economic.profitability : 0,
            sustainability: sim.results.kpis ? sim.results.kpis.sustainability_index : 0,
            status: sim.results.executive_summary ? sim.results.executive_summary.overall_status : 'غير محدد'
        }));
        
        const response = {
            success: true,
            total_count: allSimulations.length,
            page: page,
            limit: limit,
            total_pages: Math.ceil(allSimulations.length / limit),
            simulations: simulationsSummary,
            metadata: {
                user_filter: userId || 'none',
                date_range: allSimulations.length > 0 ? {
                    oldest: allSimulations[allSimulations.length - 1].timestamp,
                    newest: allSimulations[0].timestamp
                } : null
            }
        };

        res.json(response);
        
    } catch (error) {
        console.error('❌ خطأ في جلب محاكاة المستخدم:', error);
        res.status(500).json({
            success: false,
            message: 'حدث خطأ في جلب المحاكاة'
        });
    }
};

exports.analyzeSensitivity = async (req, res) => {
    try {
        const parameter = req.query.parameter || 'nitrogen';
        const range = parseFloat(req.query.range) || 0.2;
        const steps = parseInt(req.query.steps) || 5;
        const inputs = req.body;
        
        if (!inputs) {
            return res.status(400).json({
                success: false,
                message: 'مدخلات المحاكاة مطلوبة لتحليل الحساسية'
            });
        }

        console.log(`📊 تحليل حساسية للمعامل: ${parameter}`);
        
        const sensitivity = await simulation.analyzeSensitivity(
            inputs, 
            parameter, 
            range, 
            steps
        );
        
        // تحليل النتائج
        const yieldChanges = sensitivity.results.map(r => r.yield);
        const profitChanges = sensitivity.results.map(r => r.profitability);
        
        const analysis = {
            most_sensitive: Math.max(...yieldChanges) - Math.min(...yieldChanges) > 2 ? 'نعم' : 'لا',
            optimal_value: sensitivity.results.reduce((max, r) => r.profitability > max.profitability ? r : max, sensitivity.results[0]).value,
            risk_level: (Math.max(...yieldChanges) - Math.min(...yieldChanges)) > 5 ? 'مرتفع' : 'منخفض'
        };
        
        res.json({
            success: true,
            parameter: parameter,
            base_value: sensitivity.base_value,
            range_percentage: range * 100,
            steps: steps,
            sensitivity: sensitivity,
            analysis: analysis,
            recommendations: generateSensitivityRecommendations(sensitivity, parameter)
        });
        
    } catch (error) {
        console.error('❌ خطأ في تحليل الحساسية:', error);
        res.status(500).json({
            success: false,
            message: 'حدث خطأ في تحليل الحساسية'
        });
    }
};

exports.generateReport = async (req, res) => {
    try {
        const { id } = req.params;
        const format = req.query.format || 'json';
        
        if (!id) {
            return res.status(400).json({
                success: false,
                message: 'معرف المحاكاة مطلوب'
            });
        }

        console.log(`📄 توليد تقرير للمحاكاة: ${id}`);
        
        const report = await simulation.generateReport(id);
        
        if (!report) {
            return res.status(404).json({
                success: false,
                message: 'لا يمكن إنشاء تقرير لهذه المحاكاة'
            });
        }

        // إرسال التقرير حسب التنسيق المطلوب
        if (format === 'csv') {
            const csvData = simulation.convertToCSV(report);
            
            res.setHeader('Content-Type', 'text/csv');
            res.setHeader('Content-Disposition', `attachment; filename=report_${id}.csv`);
            res.send(csvData);
            
        } else if (format === 'pdf') {
            // في الإصدارات المستقبلية يمكن إضافة توليد PDF
            res.json({
                success: true,
                message: 'توليد PDF غير متوفر حالياً، سيتم إضافته في تحديثات قادمة',
                report: report
            });
            
        } else {
            // إرجاع JSON افتراضياً
            res.json({
                success: true,
                report: report,
                available_formats: ['json', 'csv'],
                metadata: {
                    generated_at: new Date().toISOString(),
                    simulation_id: id,
                    report_length: JSON.stringify(report).length
                }
            });
        }
        
    } catch (error) {
        console.error('❌ خطأ في إنشاء التقرير:', error);
        res.status(500).json({
            success: false,
            message: 'حدث خطأ في إنشاء التقرير'
        });
    }
};

exports.compareScenarios = async (req, res) => {
    try {
        const { scenarios } = req.body;
        
        if (!scenarios || !Array.isArray(scenarios) || scenarios.length < 2) {
            return res.status(400).json({
                success: false,
                message: 'يجب إرسال مصفوفة تحتوي على سيناريوهين على الأقل للمقارنة'
            });
        }

        console.log(`🔍 مقارنة ${scenarios.length} سيناريو`);
        
        const results = [];
        const startTime = Date.now();
        
        // تشغيل جميع السيناريوهات
        for (let i = 0; i < scenarios.length; i++) {
            try {
                const scenario = scenarios[i];
                // الحل: استخدام متغير منفصل لتجنب template literal متداخل
                const scenarioDisplayName = scenario.name || `سيناريو ${i + 1}`;
                console.log(`🚀 تشغيل السيناريو ${i + 1}: ${scenarioDisplayName}`);
                
                const result = await simulation.run(scenario);
                results.push({
                    scenario_id: i + 1,
                    scenario_name: scenarioDisplayName,
                    simulation_id: result.simulation_id,
                    kpis: result.kpis,
                    economic: result.economic,
                    summary: result.executive_summary
                });
                
            } catch (error) {
                console.error(`❌ خطأ في السيناريو ${i + 1}:`, error);
                results.push({
                    scenario_id: i + 1,
                    scenario_name: scenarios[i].name || `سيناريو ${i + 1}`,
                    error: error.message,
                    status: 'فشل'
                });
            }
        }
        
        const endTime = Date.now();
        const duration = (endTime - startTime) / 1000;
        
        // تحليل المقارنة
        const comparison = analyzeComparison(results);
        
        res.json({
            success: true,
            comparison: {
                scenarios_count: scenarios.length,
                successful_scenarios: results.filter(r => !r.error).length,
                duration_seconds: duration,
                results: results,
                analysis: comparison,
                best_scenario: comparison.best_scenario,
                recommendations: comparison.recommendations
            }
        });
        
    } catch (error) {
        console.error('❌ خطأ في مقارنة السيناريوهات:', error);
        res.status(500).json({
            success: false,
            message: 'حدث خطأ في مقارنة السيناريوهات'
        });
    }
};

exports.deleteSimulation = async (req, res) => {
    try {
        const { id } = req.params;
        
        if (!id) {
            return res.status(400).json({
                success: false,
                message: 'معرف المحاكاة مطلوب'
            });
        }

        console.log(`🗑️ حذف المحاكاة: ${id}`);
        
        const success = await simulation.deleteSimulation(id);
        
        if (!success) {
            return res.status(404).json({
                success: false,
                message: 'لم يتم العثور على المحاكاة'
            });
        }

        res.json({
            success: true,
            message: 'تم حذف المحاكاة بنجاح',
            simulation_id: id
        });
        
    } catch (error) {
        console.error('❌ خطأ في حذف المحاكاة:', error);
        res.status(500).json({
            success: false,
            message: 'حدث خطأ في حذف المحاكاة'
        });
    }
};

exports.getStatistics = async (req, res) => {
    try {
        const period = req.query.period || 'all';
        
        console.log(`📈 جلب إحصائيات الفترة: ${period}`);
        
        const allSimulations = await simulation.getUserSimulations(null, 10000);
        
        // تصفية حسب الفترة
        let filteredSimulations = allSimulations;
        const now = new Date();
        
        if (period === 'day') {
            const yesterday = new Date(now - 24 * 60 * 60 * 1000);
            filteredSimulations = allSimulations.filter(s => new Date(s.timestamp) > yesterday);
        } else if (period === 'week') {
            const lastWeek = new Date(now - 7 * 24 * 60 * 60 * 1000);
            filteredSimulations = allSimulations.filter(s => new Date(s.timestamp) > lastWeek);
        } else if (period === 'month') {
            const lastMonth = new Date(now - 30 * 24 * 60 * 60 * 1000);
            filteredSimulations = allSimulations.filter(s => new Date(s.timestamp) > lastMonth);
        }
        
        // حساب الإحصائيات
        const statistics = {
            total_simulations: filteredSimulations.length,
            successful_simulations: filteredSimulations.filter(s => s.results && s.results.kpis).length,
            average_profitability: 0,
            average_sustainability: 0,
            most_common_plant: getMostCommonValue(filteredSimulations, 'plant_id'),
            most_common_wilaya: getMostCommonValue(filteredSimulations, 'wilaya_id'),
            performance_distribution: {
                excellent: filteredSimulations.filter(s => s.results && s.results.executive_summary && s.results.executive_summary.overall_status === 'ممتازة').length,
                good: filteredSimulations.filter(s => s.results && s.results.executive_summary && s.results.executive_summary.overall_status === 'جيدة').length,
                average: filteredSimulations.filter(s => s.results && s.results.executive_summary && s.results.executive_summary.overall_status === 'متوسطة').length,
                needs_improvement: filteredSimulations.filter(s => s.results && s.results.executive_summary && s.results.executive_summary.overall_status === 'تحتاج تحسين').length
            },
            trends: calculateTrends(filteredSimulations)
        };
        
        // حساب المتوسطات
        const validSimulations = filteredSimulations.filter(s => s.results && s.results.kpis && s.results.economic);
        if (validSimulations.length > 0) {
            statistics.average_profitability = validSimulations.reduce((sum, s) => sum + (s.results.economic.profitability || 0), 0) / validSimulations.length;
            statistics.average_sustainability = validSimulations.reduce((sum, s) => sum + (s.results.kpis.sustainability_index || 0), 0) / validSimulations.length;
        }
        
        res.json({
            success: true,
            period: period,
            statistics: statistics,
            metadata: {
                calculated_at: new Date().toISOString(),
                data_points: filteredSimulations.length
            }
        });
        
    } catch (error) {
        console.error('❌ خطأ في جلب الإحصائيات:', error);
        res.status(500).json({
            success: false,
            message: 'حدث خطأ في جلب الإحصائيات'
        });
    }
};

// أضف هذه الدوال المساعدة للبيانات المرجعية
exports.getPlants = async (req, res) => {
    try {
        const plants = await DataService.loadJSON('plants.json');
        res.json({ success: true, data: plants });
    } catch (error) {
        console.error('❌ خطأ في جلب النباتات:', error);
        res.status(500).json({ 
            success: false, 
            message: 'خطأ في جلب النباتات',
            error: error.message 
        });
    }
};

exports.getWilayas = async (req, res) => {
    try {
        const wilayas = await DataService.loadJSON('wilayas.json');
        res.json({ success: true, data: wilayas });
    } catch (error) {
        console.error('❌ خطأ في جلب الولايات:', error);
        res.status(500).json({ 
            success: false, 
            message: 'خطأ في جلب الولايات',
            error: error.message 
        });
    }
};

exports.getSoils = async (req, res) => {
    try {
        const soils = await DataService.loadJSON('soils.json');
        res.json({ success: true, data: soils });
    } catch (error) {
        console.error('❌ خطأ في جلب التربة:', error);
        res.status(500).json({ 
            success: false, 
            message: 'خطأ في جلب التربة',
            error: error.message 
        });
    }
};

exports.getWaterSystems = async (req, res) => {
    try {
        const waterSystems = await DataService.loadJSON('water_systems.json');
        res.json({ success: true, data: waterSystems });
    } catch (error) {
        console.error('❌ خطأ في جلب أنظمة الري:', error);
        res.status(500).json({ 
            success: false, 
            message: 'خطأ في جلب أنظمة الري',
            error: error.message 
        });
    }
};

exports.getFertilizers = async (req, res) => {
    try {
        const fertilizers = await DataService.loadJSON('fertilizers.json');
        res.json({ success: true, data: fertilizers });
    } catch (error) {
        console.error('❌ خطأ في جلب الأسمدة:', error);
        res.status(500).json({ 
            success: false, 
            message: 'خطأ في جلب الأسمدة',
            error: error.message 
        });
    }
};

exports.getEconomicData = async (req, res) => {
    try {
        const economicData = await DataService.loadJSON('economic_data.json');
        res.json({ success: true, data: economicData });
    } catch (error) {
        console.error('❌ خطأ في جلب البيانات الاقتصادية:', error);
        res.status(500).json({ 
            success: false, 
            message: 'خطأ في جلب البيانات الاقتصادية',
            error: error.message 
        });
    }
};

// تصدير الدوال المساعدة
exports.generateSensitivityRecommendations = generateSensitivityRecommendations;
exports.analyzeComparison = analyzeComparison;
exports.getMostCommonValue = getMostCommonValue;
exports.calculateTrends = calculateTrends;