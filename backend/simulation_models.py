import numpy as np
import random
from datetime import datetime, timedelta
from scipy import stats
import math

class AgriculturalSimulation:
    def __init__(self):
        # الثوابت الأساسية المعتمدة على نماذج علمية
        self.GROWTH_RATE_BASE = 0.05  # معدل النمو الأساسي
        self.TEMP_OPTIMAL_MIN = 20    # درجة الحرارة المثلى الدنيا
        self.TEMP_OPTIMAL_MAX = 30    # درجة الحرارة المثلى القصوى
        self.RAIN_OPTIMAL_MIN = 400   # كمية الهطول المثلى الدنيا (مم/سنة)
        self.RAIN_OPTIMAL_MAX = 800   # كمية الهطول المثلى القصوى (مم/سنة)
        
        # الثوابت المحسنة بالأساس العلمي من نماذج منظمة الأغذية والزراعة
        self.PHOTOSYNTHESIS_BASE_RATE = 0.08  # معدل البناء الضوئي الأساسي
        self.RESPIRATION_BASE_RATE = 0.03     # معدل التنفس الأساسي
        self.TEMP_OPTIMAL_RANGE = 5           # المدى المثالي لدرجة الحرارة (± درجات)
        
        # معاملات النمو حسب مراحل النمو (الإنبات، النمو الخضري، التزهير، النضج)
        self.GROWTH_STAGE_COEFFICIENTS = {
            'germination': {'temp': 1.2, 'water': 1.3, 'nutrient': 0.8},
            'vegetative': {'temp': 1.0, 'water': 1.0, 'nutrient': 1.0},
            'flowering': {'temp': 0.9, 'water': 1.1, 'nutrient': 1.2},
            'maturation': {'temp': 0.8, 'water': 0.9, 'nutrient': 1.1}
        }
        
    def run_simulation(self, plant, wilaya, soil_type, water_system, fertilizer, 
                     area, nitrogen, phosphorus, potassium, irrigation_amount, 
                     irrigation_frequency, water_quality, climate_scenario, years, 
                     temp_change, rain_change, co2_level, monte_carlo_runs, 
                     pest_pressure, tillage, planting_date=None, rotation_crops=None):
        """
        تشغيل المحاكاة الزراعية المتقدمة مع نماذج علمية محسنة
        """
        # التحقق من صحة المدخلات
        self._validate_inputs(plant, wilaya, soil_type, water_system, fertilizer,
                            area, nitrogen, phosphorus, potassium, irrigation_amount,
                            irrigation_frequency, water_quality, years, temp_change,
                            rain_change, co2_level, monte_carlo_runs, pest_pressure)
        
        # حساب معاملات النمو المحسنة
        temp_factor = self._calculate_temperature_factor_enhanced(
            wilaya['avg_temp'] + temp_change, 
            plant['optimal_temp_min'], 
            plant['optimal_temp_max'],
            wilaya.get('temp_amplitude', 10)  # سعة درجة الحرارة السنوية
        )
        
        rain_factor = self._calculate_rainfall_factor_enhanced(
            wilaya['avg_rainfall'] * (1 + rain_change/100), 
            plant['water_needs_min'], 
            plant['water_needs_max'],
            soil_type['drainage'],
            wilaya.get('rainfall_distribution', [1]*12)  # توزيع الهطول على أشهر السنة
        )
        
        soil_factor = self._calculate_soil_factor_enhanced(
            soil_type, 
            plant['suitable_soil_types'],
            plant.get('root_depth', 50)  # عمق الجذور الافتراضي
        )
        
        nutrient_factor = self._calculate_nutrient_factor_enhanced(
            nitrogen, phosphorus, potassium,
            plant['nitrogen_needs'], 
            plant['phosphorus_needs'], 
            plant['potassium_needs'],
            soil_type['ph'],
            soil_type['organic_matter'],
            soil_type.get('cation_exchange_capacity', 15)  # سعة التبادل الكاتيوني
        )
        
        water_factor = self._calculate_water_factor_enhanced(
            irrigation_amount, 
            irrigation_frequency, 
            water_quality,
            water_system['efficiency'],
            plant['water_needs_min'],
            plant['water_needs_max'],
            soil_type['drainage'],
            soil_type.get('water_holding_capacity', 0.3),  # قدرة الاحتفاظ بالماء
            wilaya.get('evapotranspiration', 5)  # البخر-نتح
        )
        
        # حساب مؤشرات الإجهاد المحسنة
        heat_stress = self._calculate_heat_stress_advanced(
            wilaya['avg_temp'] + temp_change, 
            plant['optimal_temp_min'], 
            plant['optimal_temp_max'],
            wilaya.get('max_temp', wilaya['avg_temp'] + 5) + temp_change,  # أقصى درجة حرارة
            wilaya.get('min_temp', wilaya['avg_temp'] - 5) + temp_change   # أدنى درجة حرارة
        )
        
        water_stress = self._calculate_water_stress_advanced(
            irrigation_amount, irrigation_frequency, water_quality,
            plant['water_needs_min'], plant['water_needs_max'],
            soil_type.get('water_holding_capacity', 0.3),
            wilaya.get('evapotranspiration', 5)
        )
        
        # حساب كفاءة استخدام المغذيات المحسنة
        nue = self._calculate_nue_advanced(
            nitrogen, phosphorus, potassium,
            plant['nitrogen_needs'], plant['phosphorus_needs'], plant['potassium_needs'],
            soil_type['ph'], soil_type['organic_matter'], soil_type.get('cation_exchange_capacity', 15),
            water_factor, temp_factor
        )
        
        # حساب البصمة الكربونية المحسنة
        carbon_footprint = self._calculate_carbon_footprint_advanced(
            fertilizer['carbon_footprint'], 
            nitrogen, phosphorus, potassium,
            water_system['energy_consumption'],
            irrigation_amount,
            tillage,
            area,
            soil_type['organic_matter'],
            plant.get('carbon_sequestration', 0)  # كمية الكربون التي يخزنها المحصول
        )
        
        # حساب الإنتاجية باستخدام نموذج منظمة الأغذية والزراعة المعدل
        base_yield = plant['base_yield']
        potential_yield = self._calculate_potential_yield_advanced(
            base_yield, temp_factor, rain_factor, soil_factor, 
            nutrient_factor, water_factor, co2_level,
            plant.get('photosynthesis_type', 'C3')  # نوع التمثيل الضوئي (C3, C4, CAM)
        )
        
        # تطبيق ضغط الآفات والعوامل الأخرى
        pest_factor = self._calculate_pest_factor(pest_pressure, plant.get('pest_resistance', 0.5))
        potential_yield *= pest_factor
        
        # تطبيق تأثير نوع الحراثة
        tillage_factor = self._get_tillage_factor_advanced(tillage, soil_type, plant.get('root_depth', 50))
        potential_yield *= tillage_factor
        
        # تطبيق تأثير الدورة الزراعية إذا وجدت
        if rotation_crops:
            rotation_factor = self._calculate_rotation_factor(rotation_crops, plant.get('family', 'Unknown'))
            potential_yield *= rotation_factor
        
        # حساب الإنتاجية النهائية مع محاكاة مونت كارلو لعدم اليقين
        yield_per_ha, yield_uncertainty = self._monte_carlo_yield_simulation_advanced(
            potential_yield, monte_carlo_runs, 
            temp_factor, rain_factor, soil_factor, nutrient_factor, water_factor,
            plant.get('yield_variability', 0.2)  # معامل التباين في الإنتاجية
        )
        
        total_yield = yield_per_ha * area
        
        # الحسابات الاقتصادية المحسنة
        cost_per_ha = self._calculate_cost_per_ha_advanced(
            nitrogen, phosphorus, potassium,
            fertilizer['cost_per_kg'],
            water_system['cost_per_cubic_meter'],
            irrigation_amount,
            tillage,
            area,
            plant,
            pest_pressure,
            soil_type.get('ph_correction_needed', False)  # هل يحتاج تصحيح درجة الحموضة
        )
        
        total_cost = cost_per_ha * area
        
        revenue_per_ha = yield_per_ha * plant['price_per_ton']
        total_revenue = revenue_per_ha * area
        
        profitability = ((revenue_per_ha - cost_per_ha) / cost_per_ha) * 100 if cost_per_ha > 0 else 0
        roi = profitability
        
        # مؤشر الأمن الغذائي المحسن
        food_security = self._calculate_food_security_index_advanced(
            yield_per_ha, plant['base_yield'], area, wilaya.get('region', 'Unknown'),
            plant.get('nutritional_value', 0.5)  # القيمة الغذائية للمحصول
        )
        
        # مؤشر الإجهاد الإجمالي المحسن
        stress_index = self._calculate_stress_index_advanced(
            heat_stress, water_stress, pest_pressure, 
            plant.get('stress_tolerance', 0.5)  # تحمل النبات للإجهاد
        )
        
        # حساب مخاطر المناخ
        climate_risk = self._calculate_climate_risk(
            wilaya, temp_change, rain_change, co2_level,
            plant.get('climate_vulnerability', 0.5)  # قابلية التأثر بالمناخ
        )
        
        # توليد البيانات المحسنة
        growth_data = self._generate_growth_data_advanced(
            base_yield, yield_per_ha, years, monte_carlo_runs,
            temp_factor, rain_factor, soil_factor, nutrient_factor, water_factor,
            planting_date or datetime.now(), plant.get('growth_duration', 120)  # مدة النمو
        )
        
        climate_data = self._generate_climate_data_advanced(
            wilaya, years, temp_change, rain_change, co2_level,
            climate_scenario  # سيناريو المناخ
        )
        
        costs_data = self._generate_costs_data_advanced(
            nitrogen, phosphorus, potassium,
            fertilizer['cost_per_kg'],
            water_system['cost_per_cubic_meter'],
            irrigation_amount,
            tillage,
            area,
            plant,
            pest_pressure,
            soil_type.get('ph_correction_needed', False)
        )
        
        comparison_data = self._generate_comparison_data_advanced(
            plant, wilaya, soil_type, water_system, fertilizer,
            area, nitrogen, phosphorus, potassium, irrigation_amount,
            climate_scenario, temp_change, rain_change, co2_level,
            tillage, planting_date
        )
        
        # التوصيات المحسنة مع رؤى قابلة للتنفيذ
        recommendations = self._generate_recommendations_advanced(
            heat_stress, water_stress, nue, profitability, 
            yield_per_ha/base_yield, soil_type, water_system, fertilizer,
            temp_change, rain_change, climate_risk, pest_pressure,
            plant, wilaya
        )
        
        # النتائج المحسنة مع نطاقات عدم اليقين
        results = {
            "kpis": {
                "heat_stress": round(heat_stress, 1),
                "water_stress": round(water_stress, 1),
                "nue": round(nue, 1),
                "carbon_footprint": round(carbon_footprint, 1),
                "food_security": round(food_security, 1),
                "yield": round(total_yield, 1),
                "yield_uncertainty": round(yield_uncertainty, 1),
                "stress_index": round(stress_index, 1),
                "climate_risk": round(climate_risk, 1),
                "water_use_efficiency": round(self._calculate_water_use_efficiency(
                    yield_per_ha, irrigation_amount, wilaya['avg_rainfall'] * (1 + rain_change/100)
                ), 1)
            },
            "economic": {
                "yield": round(total_yield, 1),
                "cost": round(total_cost, 1),
                "revenue": round(total_revenue, 1),
                "profitability": round(profitability, 1),
                "roi": round(roi, 1),
                "cost_breakdown": costs_data,
                "breakeven_yield": round(cost_per_ha / plant['price_per_ton'], 1),
                "breakeven_price": round(cost_per_ha / yield_per_ha, 1) if yield_per_ha > 0 else 0
            },
            "growth": growth_data,
            "climate": climate_data,
            "costs": costs_data,
            "comparison": comparison_data,
            "recommendations": recommendations,
            "input_parameters": {
                "plant": plant['name'],
                "wilaya": wilaya['name'],
                "soil_type": soil_type['name'],
                "water_system": water_system['name'],
                "fertilizer": fertilizer['name'],
                "area": area,
                "climate_scenario": climate_scenario,
                "simulation_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "planting_date": planting_date.strftime("%Y-%m-%d") if planting_date else "غير محدد"
            }
        }
        
        return results
    
    def _validate_inputs(self, plant, wilaya, soil_type, water_system, fertilizer,
                        area, nitrogen, phosphorus, potassium, irrigation_amount,
                        irrigation_frequency, water_quality, years, temp_change,
                        rain_change, co2_level, monte_carlo_runs, pest_pressure):
        """التحقق من صحة المدخلات وقيمها"""
        if area <= 0:
            raise ValueError("المساحة يجب أن تكون قيمة موجبة")
        
        if years <= 0 or years > 50:
            raise ValueError("عدد سنوات المحاكاة يجب أن يكون بين 1 و 50")
        
        if monte_carlo_runs <= 0 or monte_carlo_runs > 10000:
            raise ValueError("عدد مرات محاكاة مونت كارلو يجب أن يكون بين 1 و 10000")
        
        if pest_pressure < 0 or pest_pressure > 100:
            raise ValueError("ضغط الآفات يجب أن يكون بين 0 و 100")
        
        if co2_level < 300 or co2_level > 1000:
            raise ValueError("مستوى ثاني أكسيد الكربون يجب أن يكون بين 300 و 1000 جزء في المليون")
    
    def _calculate_temperature_factor_enhanced(self, current_temp, optimal_min, optimal_max, temp_amplitude):
        """
        معامل درجة الحرارة المحسن باستخدام دالة Gaussian مع مراعاة السعة الحرارية
        """
        optimal_mean = (optimal_min + optimal_max) / 2
        temperature_range = optimal_max - optimal_min
        
        if temperature_range == 0:
            return 1.0 if current_temp == optimal_mean else 0.0
        
        # حساب المعامل مع مراعاة السعة الحرارية
        amplitude_factor = 1.0 - min(0.3, temp_amplitude / 30)  # تقليل المعامل مع زيادة السعة
        
        # دالة Gaussian الاستجابة مع تعديل السعة
        exponent = -((current_temp - optimal_mean) / (temperature_range / 2)) ** 2
        base_factor = np.exp(exponent)
        
        return max(0.0, min(1.0, base_factor * amplitude_factor))
    
    def _calculate_rainfall_factor_enhanced(self, current_rainfall, min_needs, max_needs, drainage, rainfall_distribution):
        """
        معامل الهطول المحسن مع مراعاة توزيع الأمطار على أشهر السنة
        """
        # حساب معامل توزيع الأمطار (معامل انتظام الهطول)
        distribution_factor = self._calculate_rainfall_distribution_factor(rainfall_distribution)
        
        # ضبط الاحتياجات بناءً على تصريف التربة
        drainage_factor = {
            "عالي": 0.8,    # تربة رملية، احتفاظ أقل بالماء
            "متوسط": 1.0,   # تربة مزيجية
            "منخفض": 1.2,   # تربة طينية، احتفاظ أكبر بالماء
            "منخفض جداً": 1.4  # تربة طينية جداً
        }.get(drainage, 1.0)
        
        adjusted_min = min_needs * drainage_factor * distribution_factor
        adjusted_max = max_needs * drainage_factor * distribution_factor
        
        if current_rainfall < adjusted_min:
            return max(0.1, current_rainfall / adjusted_min)
        elif current_rainfall > adjusted_max:
            excess = current_rainfall - adjusted_max
            return max(0.3, 1 - (excess / (adjusted_max * 2)))  # عقوبة أقل للزيادة
        else:
            return 1.0
    
    def _calculate_rainfall_distribution_factor(self, rainfall_distribution):
        """
        حساب معامل انتظام توزيع الأمطار على أشهر السنة
        """
        if not rainfall_distribution or len(rainfall_distribution) != 12:
            return 1.0  # قيمة افتراضية إذا لم يتم توفير التوزيع
        
        # حساب معامل التباين (كلما قل التباين زاد الانتظام)
        cv = np.std(rainfall_distribution) / np.mean(rainfall_distribution) if np.mean(rainfall_distribution) > 0 else 1
        
        # تحويل معامل التباين إلى معامل انتظام (0-1)
        return max(0.3, min(1.0, 1 - min(0.7, cv)))
    
    def _calculate_soil_factor_enhanced(self, soil_type, suitable_soil_types, root_depth):
        """
        معامل التربة المحسن مع مراعاة عمق الجذور
        """
        if soil_type['id'] in suitable_soil_types:
            base_factor = 1.0
        else:
            # تحقق من مدى ملاءمة التربة مع مراعاة الخصائص الفيزيائية
            base_factor = 0.7  # الأساسي
        
        # تحسين النقاط بناءً على خصائص التربة
        if soil_type.get('organic_matter', 0) > 2:
            base_factor += 0.1
        if soil_type.get('ph', 7) >= 6 and soil_type.get('ph', 7) <= 7.5:
            base_factor += 0.1
        if soil_type.get('drainage') == 'متوسط':
            base_factor += 0.1
            
        # مراعاة عمق الجذور وعمق التربة
        soil_depth_factor = 1.0
        if soil_type.get('depth', 100) < root_depth:
            soil_depth_factor = soil_type.get('depth', 100) / root_depth
            
        return min(1.0, base_factor * soil_depth_factor)
    
    def _calculate_nutrient_factor_enhanced(self, n, p, k, n_needs, p_needs, k_needs, ph, organic_matter, cec):
        """
        معامل المغذيات المحسن مع مراعاة سعة التبادل الكاتيوني (CEC)
        """
        # تعديل الاحتياجات بناءً على خصائص التربة
        ph_factor = 1.0
        if ph < 6 or ph > 7.5:
            ph_factor = 0.8  # تقليل الكفاءة في التربة الحمضية أو القلوية
            
        om_factor = 1.0 + (organic_matter - 2) * 0.05  # زيادة الكفاءة مع زيادة المادة العضوية
        
        # مراعاة سعة التبادل الكاتيوني (CEC) في توفر المغذيات
        cec_factor = min(1.5, 0.5 + cec / 20)  # CEC المثالي حوالي 20-30 meq/100g
        
        n_factor = min(1.0, n / n_needs) * ph_factor * cec_factor
        p_factor = min(1.0, p / p_needs) * ph_factor * om_factor * cec_factor
        k_factor = min(1.0, k / k_needs) * ph_factor * cec_factor
        
        # المتوسط المرجح مع تعديلات إضافية
        return (n_factor * 0.5) + (p_factor * 0.3) + (k_factor * 0.2)
    
    def _calculate_water_factor_enhanced(self, irrigation_amount, frequency, quality, efficiency, min_needs, max_needs, drainage, water_holding_capacity, evapotranspiration):
        """
        معامل المياه المحسن مع مراعاة البخر-نتح وقدرة الاحتفاظ بالماء
        """
        # حساب كمية المياه الفعلية مع مراعاة الكفاءة
        actual_water = irrigation_amount * (30 / frequency) * efficiency
        
        # حساب فقدان المياه بالبخر-نتح
        et_loss = evapotranspiration * 30  # فقدان شهري
        
        # صافي المياه المتاحة بعد خصم البخر-نتح
        net_water = max(0, actual_water - et_loss)
        
        # تعديل الاحتياجات بناءً على تصريف التربة وقدرة الاحتفاظ بالماء
        drainage_adjustment = {
            "عالي": 1.2,    # تحتاج إلى مزيد من الماء
            "متوسط": 1.0,
            "منخفض": 0.8,   # تحتاج إلى كمية أقل من الماء
            "منخفض جداً": 0.6
        }.get(drainage, 1.0)
        
        # تعديل بناءً على قدرة الاحتفاظ بالماء
        whc_factor = 0.8 + (water_holding_capacity / 200)  # قدرة مثالية 200 مم/م
        
        adjusted_min = min_needs * drainage_adjustment * whc_factor
        adjusted_max = max_needs * drainage_adjustment * whc_factor
        
        if net_water < adjusted_min:
            return max(0.1, net_water / adjusted_min)
        elif net_water > adjusted_max:
            return max(0.3, 1 - ((net_water - adjusted_max) / (adjusted_max * 2)))
        else:
            # تعديل بناءً على جودة المياه
            quality_factor = 1.0
            if quality > 1.0:  # إذا كانت الملوحة عالية
                quality_factor = 1.0 - (quality - 1.0) * 0.2
            return max(0.3, quality_factor)
    
    def _calculate_heat_stress_advanced(self, current_temp, optimal_min, optimal_max, max_temp, min_temp):
        """
        حساب إجهاد الحرارة المتقدم مع مراعاة درجات الحرارة القصوى
        """
        # إجهاد البرودة
        cold_stress = 0
        if min_temp < optimal_min:
            cold_stress = min(100, ((optimal_min - min_temp) / optimal_min) * 100 * 0.7)  # وزن أقل للبرودة
        
        # إجهاد الحرارة
        heat_stress = 0
        if max_temp > optimal_max:
            heat_stress = min(100, ((max_temp - optimal_max) / optimal_max) * 100)
        
        # إجهاد التقلبات الحرارية
        temp_range_stress = 0
        temp_range = max_temp - min_temp
        if temp_range > 15:  # إذا كان المدى الحراري كبيراً
            temp_range_stress = min(30, (temp_range - 15) * 2)
        
        return max(cold_stress, heat_stress) + temp_range_stress
    
    def _calculate_water_stress_advanced(self, irrigation_amount, frequency, quality, min_needs, max_needs, water_holding_capacity, evapotranspiration):
        """
        حساب إجهاد المياه المتقدم مع مراعاة البخر-نتح
        """
        # حساب كمية المياه الفعلية
        actual_water = irrigation_amount * (30 / frequency)
        
        # حساب فقدان المياه بالبخر-نتح
        et_loss = evapotranspiration * 30  # فقدان شهري
        
        # صافي المياه المتاحة بعد خصم البخر-نتح
        net_water = max(0, actual_water - et_loss)
        
        if net_water < min_needs:
            return min(100, ((min_needs - net_water) / min_needs) * 100)
        elif net_water > max_needs:
            return min(30, ((net_water - max_needs) / max_needs) * 30)  # عقوبة أقل للزيادة
        else:
            # إجهاد الملوحة
            salinity_stress = 0
            if quality > 2.0:  # إذا كانت الملوحة عالية
                salinity_stress = min(30, (quality - 2.0) * 10)
            return salinity_stress
    
    def _calculate_nue_advanced(self, n, p, k, n_needs, p_needs, k_needs, ph, organic_matter, cec, water_factor, temp_factor):
        """
        حساب كفاءة استخدام المغذيات المتقدم مع مراعاة العوامل البيئية
        """
        # حساب الكفاءة الفعلية مع مراعاة خصائص التربة والعوامل البيئية
        n_efficiency = min(1.0, n / n_needs) * (0.9 if 6 <= ph <= 7.5 else 0.7) * water_factor * temp_factor
        p_efficiency = min(1.0, p / p_needs) * (1.0 + (organic_matter - 2) * 0.05) * water_factor * temp_factor
        k_efficiency = min(1.0, k / k_needs) * (0.9 if 6 <= ph <= 7.5 else 0.7) * water_factor * temp_factor
        
        # مراعاة سعة التبادل الكاتيوني
        cec_factor = min(1.2, 0.8 + cec / 50)
        
        return (n_efficiency * 0.5 + p_efficiency * 0.3 + k_efficiency * 0.2) * 100 * cec_factor
    
    def _calculate_carbon_footprint_advanced(self, fert_cf, n, p, k, water_energy, irrigation, tillage, area, organic_matter, carbon_sequestration):
        """
        حساب البصمة الكربونية المتقدم مع مراعاة عزل الكربون
        """
        # انبعاثات الأسمدة
        fertilizer_emissions = fert_cf * (n + p + k) * area
        
        # انبعاثات الري
        water_emissions = water_energy * irrigation * area
        
        # انبعاثات الحراثة
        tillage_emissions = {
            'conventional': 100,  # كجم CO2/هكتار
            'reduced': 70,
            'no-till': 40
        }.get(tillage, 100) * area
        
        # انبعاثات أخرى (وقود، نقل، إلخ)
        other_emissions = 50 * area
        
        # عزل الكربون (خصم من الانبعاثات)
        carbon_sequestered = carbon_sequestration * area * (1 + organic_matter / 10)
        
        return max(0, fertilizer_emissions + water_emissions + tillage_emissions + other_emissions - carbon_sequestered)
    
    def _calculate_potential_yield_advanced(self, base_yield, temp_factor, rain_factor, soil_factor, nutrient_factor, water_factor, co2_level, photosynthesis_type):
        """
        حساب الإنتاجية المحتملة باستخدام نموذج متقدم
        """
        # العوامل الأساسية
        growth_factor = temp_factor * rain_factor * soil_factor * nutrient_factor * water_factor
        
        # تأثير CO2 (تخصيب الكربون) - يختلف حسب نوع التمثيل الضوئي
        if photosynthesis_type == 'C3':
            co2_factor = 1 + (np.log(co2_level / 350) * 0.12)  # استجابة أعلى لنباتات C3 لزيادة CO2
        elif photosynthesis_type == 'C4':
            co2_factor = 1 + (np.log(co2_level / 350) * 0.06)  # استجابة أقل لنباتات C4
        else:  # CAM
            co2_factor = 1 + (np.log(co2_level / 350) * 0.08)  # استجابة متوسطة
        
        return base_yield * growth_factor * co2_factor
    
    def _calculate_pest_factor(self, pest_pressure, pest_resistance):
        """
        حساب معامل تأثير الآفات
        """
        # كلما زادت مقاومة النبات قل تأثير الآفات
        effectiveness = 1 - pest_resistance
        pest_impact = pest_pressure / 100 * effectiveness
        
        return 1 - min(0.7, pest_impact)  # أقصى خسارة 70%
    
    def _get_tillage_factor_advanced(self, tillage, soil_type, root_depth):
        """
        معامل الحراثة المحسن مع مراعاة عمق الجذور
        """
        base_factor = {
            'conventional': 1.0,
            'reduced': 1.05,
            'no-till': 1.1
        }.get(tillage, 1.0)
        
        # تعديل بناءً على نوع التربة
        soil_adjustment = {
            'طينية': 0.95 if tillage == 'no-till' else 1.0,
            'رملية': 1.05 if tillage == 'no-till' else 1.0,
            'مزيجية': 1.0
        }.get(soil_type.get('texture', 'مزيجية'), 1.0)
        
        # تعديل بناءً على عمق الجذور
        root_depth_factor = 1.0
        if root_depth > 50:  # إذا كانت الجذور عميقة
            root_depth_factor = 1.1 if tillage == 'conventional' else 1.0
        
        return base_factor * soil_adjustment * root_depth_factor
    
    def _calculate_rotation_factor(self, rotation_crops, plant_family):
        """
        حساب معامل الدورة الزراعية
        """
        if not rotation_crops or len(rotation_crops) == 0:
            return 1.0  # لا توجد دورة زراعية
        
        # حساب تنوع المحاصيل في الدورة
        diversity = len(set(rotation_crops)) / len(rotation_crops) if len(rotation_crops) > 0 else 1
        
        # التحقق من عدم تكرار المحاصيل من نفس العائلة
        family_repetition = 0
        for crop in rotation_crops:
            if crop.get('family') == plant_family:
                family_repetition += 1
        
        repetition_penalty = 1.0 - (family_repetition * 0.1)  # عقوبة 10% لكل تكرار
        
        return 0.8 + (diversity * 0.2) * repetition_penalty  # قيمة بين 0.8 و 1.0
    
    def _monte_carlo_yield_simulation_advanced(self, potential_yield, runs, temp_factor, rain_factor, soil_factor, nutrient_factor, water_factor, yield_variability):
        """
        محاكاة مونت كارلو المتقدمة لعدم اليقين في الإنتاجية
        """
        # إنشاء توزيعات احتمالية للعوامل مع مراعاة التباين
        temp_std = 0.1 * yield_variability
        rain_std = 0.15 * yield_variability
        soil_std = 0.05 * yield_variability
        nutrient_std = 0.1 * yield_variability
        water_std = 0.1 * yield_variability
        
        temp_samples = np.random.normal(temp_factor, temp_std, runs)
        rain_samples = np.random.normal(rain_factor, rain_std, runs)
        soil_samples = np.random.normal(soil_factor, soil_std, runs)
        nutrient_samples = np.random.normal(nutrient_factor, nutrient_std, runs)
        water_samples = np.random.normal(water_factor, water_std, runs)
        
        # حساب الإنتاجية لكل عينة
        yields = potential_yield * temp_samples * rain_samples * soil_samples * nutrient_samples * water_samples
        
        # حساب المتوسط وعدم اليقين (الانحراف المعياري)
        mean_yield = np.mean(yields)
        uncertainty = np.std(yields) / mean_yield * 100 if mean_yield > 0 else 0
        
        return mean_yield, uncertainty
    
    def _calculate_cost_per_ha_advanced(self, n, p, k, fert_cost, water_cost, irrigation, tillage, area, plant, pest_pressure, ph_correction_needed):
        """
        حساب التكلفة لكل هكتار المتقدمة
        """
        # تكلفة الأسمدة
        fertilizer_cost = (n + p + k) * fert_cost
        
        # تكلفة المياه
        water_cost_total = irrigation * water_cost
        
        # تكلفة الحراثة
        tillage_cost = {
            'conventional': 5000,  # دينار/هكتار
            'reduced': 3500,
            'no-till': 2000
        }.get(tillage, 5000)
        
        # تكاليف البذور (تعتمد على المحصول)
        seed_cost = {
            'قمح': 3000,
            'شعير': 2500,
            'ذرة': 4000,
            'بطاطس': 6000
        }.get(plant.get('name', 'قمح'), 3000)
        
        # تكاليف مكافحة الآفات (تعتمد على ضغط الآفات)
        pest_control_cost = pest_pressure / 100 * 2000  # حتى 2000 دينار/هكتار
        
        # تكاليف تصحيح درجة الحموضة إذا لزم الأمر
        ph_correction_cost = 1000 if ph_correction_needed else 0
        
        # تكاليف أخرى (عمالة، صيانة، إلخ)
        other_costs = 8000
        
        return fertilizer_cost + water_cost_total + tillage_cost + seed_cost + pest_control_cost + ph_correction_cost + other_costs
    
    def _calculate_food_security_index_advanced(self, actual_yield, potential_yield, area, region, nutritional_value):
        """
        حساب مؤشر الأمن الغذائي المتقدم مع مراعاة القيمة الغذائية
        """
        # نسبة تحقيق الإنتاجية القصوى
        yield_ratio = actual_yield / potential_yield if potential_yield > 0 else 0
        
        # عامل المنطقة (بعض المناطق لديها أولوية غذائية أعلى)
        region_factor = {
            'شمال': 1.2,
            'وسط': 1.0,
            'جنوب': 0.8
        }.get(region, 1.0)
        
        # عامل القيمة الغذائية
        nutrition_factor = 0.8 + (nutritional_value * 0.2)  # مضاعف من 0.8 إلى 1.0
        
        return min(100, yield_ratio * 100 * region_factor * nutrition_factor)
    
    def _calculate_stress_index_advanced(self, heat_stress, water_stress, pest_pressure, stress_tolerance):
        """
        حساب مؤشر الإجهاد الإجمالي المتقدم مع مراعاة تحمل النبات
        """
        # تقليل الإجهاد بناءً على تحمل النبات
        tolerance_factor = 1 - stress_tolerance
        
        return (heat_stress * 0.4 + water_stress * 0.4 + pest_pressure * 0.2) * tolerance_factor
    
    def _calculate_climate_risk(self, wilaya, temp_change, rain_change, co2_level, climate_vulnerability):
        """
        حساب مخاطر المناخ
        """
        # مخاطر درجة الحرارة
        temp_risk = min(100, abs(temp_change) * 10 * (1 + wilaya.get('temp_amplitude', 10) / 20))
        
        # مخاطر الهطول
        rain_risk = min(100, abs(rain_change) * 0.5 * (1 + (100 - wilaya.get('rainfall_reliability', 50)) / 100))
        
        # مخاطر التطرف المناخي
        extreme_risk = wilaya.get('extreme_events', 0) * 20
        
        return (temp_risk * 0.4 + rain_risk * 0.4 + extreme_risk * 0.2) * climate_vulnerability
    
    def _calculate_water_use_efficiency(self, yield_per_ha, irrigation, rainfall):
        """
        حساب كفاءة استخدام المياه (كجم/م³)
        """
        total_water = irrigation + rainfall
        return yield_per_ha / total_water if total_water > 0 else 0
    
    def _generate_growth_data_advanced(self, base_yield, expected_yield, years, monte_carlo_runs, temp_factor, rain_factor, soil_factor, nutrient_factor, water_factor, planting_date, growth_duration):
        """
        توليد بيانات النمو المتقدمة مع مراعاة تاريخ الزراعة ومدة النمو
        """
        if planting_date is None:
            planting_date = datetime.now()
        
        # تحديد مواعيد مراحل النمو بناءً على تاريخ الزراعة ومدة النمو
        germination_end = planting_date + timedelta(days=growth_duration * 0.1)
        vegetative_end = planting_date + timedelta(days=growth_duration * 0.5)
        flowering_end = planting_date + timedelta(days=growth_duration * 0.75)
        maturation_end = planting_date + timedelta(days=growth_duration)
        
        days = list(range(1, growth_duration + 1, 7))  # بيانات أسبوعية
        
        # استخدام نموذج النمو اللوجستي المحسن مع مراعاة مراحل النمو
        median_growth = []
        for day in days:
            # تحديد مرحلة النمو الحالية
            current_date = planting_date + timedelta(days=day)
            if current_date < germination_end:
                stage = 'germination'
            elif current_date < vegetative_end:
                stage = 'vegetative'
            elif current_date < flowering_end:
                stage = 'flowering'
            else:
                stage = 'maturation'
            
            # تطبيق معاملات مرحلة النمو
            stage_coeff = self.GROWTH_STAGE_COEFFICIENTS[stage]
            adjusted_temp_factor = temp_factor * stage_coeff['temp']
            adjusted_water_factor = water_factor * stage_coeff['water']
            adjusted_nutrient_factor = nutrient_factor * stage_coeff['nutrient']
            
            # نموذج النمو اللوجستي مع مراعاة العوامل البيئية
            growth_rate = self.GROWTH_RATE_BASE * adjusted_temp_factor * rain_factor * adjusted_nutrient_factor * adjusted_water_factor
            carrying_capacity = base_yield * 1.2
            initial_value = base_yield * 0.1
            
            value = carrying_capacity / (1 + np.exp(-growth_rate * (day - growth_duration/2) + 4))
            median_growth.append(value)
        
        # محاكاة مونت كارلو للشكوك
        p10_growth = [v * 0.85 for v in median_growth]  # تقدير متحفظ
        p90_growth = [v * 1.15 for v in median_growth]  # تقدير متفائل
        
        return {
            "days": days,
            "median": median_growth,
            "p10": p10_growth,
            "p90": p90_growth,
            "stages": {
                "germination": germination_end.strftime("%Y-%m-%d"),
                "vegetative": vegetative_end.strftime("%Y-%m-%d"),
                "flowering": flowering_end.strftime("%Y-%m-%d"),
                "maturation": maturation_end.strftime("%Y-%m-%d")
            }
        }
    
    def _generate_climate_data_advanced(self, wilaya, years, temp_change, rain_change, co2_level, climate_scenario):
        """
        توليد بيانات المناخ المتقدمة مع مراعاة سيناريو المناخ
        """
        months = ['جانفي', 'فيفري', 'مارس', 'أفريل', 'ماي', 'جوان', 
                 'جويلية', 'أوت', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر']
        
        # درجات الحرارة الشهرية مع مراعاة التغير المناخي والسيناريو
        base_temps = wilaya.get('monthly_temps', [12, 13, 15, 18, 22, 26, 29, 30, 27, 22, 17, 13])
        
        # تطبيق سيناريو المناخ على درجات الحرارة
        scenario_temp_factor = 1.0
        if climate_scenario == 'rcp45':
            scenario_temp_factor = 1.2
        elif climate_scenario == 'rcp85':
            scenario_temp_factor = 1.5
        
        temperatures = [t + temp_change * scenario_temp_factor for t in base_temps]
        
        # كمية الهطول الشهرية مع مراعاة التغير المناخي والسيناريو
        base_rainfall = wilaya.get('monthly_rainfall', [70, 60, 50, 40, 30, 10, 5, 10, 30, 50, 70, 80])
        
        # تطبيق سيناريو المناخ على الهطول
        scenario_rain_factor = 1.0
        if climate_scenario == 'rcp45':
            scenario_rain_factor = 0.9
        elif climate_scenario == 'rcp85':
            scenario_rain_factor = 0.8
        
        rainfall = [r * (1 + rain_change/100) * scenario_rain_factor for r in base_rainfall]
        
        # بيانات CO2 مع مراعاة السيناريو
        scenario_co2_factor = 1.0
        if climate_scenario == 'rcp45':
            scenario_co2_factor = 1.2
        elif climate_scenario == 'rcp85':
            scenario_co2_factor = 1.5
        
        co2_data = [co2_level * scenario_co2_factor] * 12
        
        return {
            "months": months,
            "temperature": temperatures,
            "rain": rainfall,
            "co2": co2_data,
            "scenario": climate_scenario
        }
    
    def _generate_costs_data_advanced(self, n, p, k, fert_cost, water_cost, irrigation, tillage, area, plant, pest_pressure, ph_correction_needed):
        """
        توليد بيانات التكاليف المتقدمة
        """
        # حساب التكاليف التفصيلية
        fertilizer_cost = (n + p + k) * fert_cost * area
        water_cost_total = irrigation * water_cost * area
        
        tillage_cost = {
            'conventional': 5000,
            'reduced': 3500,
            'no-till': 2000
        }.get(tillage, 5000) * area
        
        seed_cost = {
            'قمح': 3000,
            'شعير': 2500,
            'ذرة': 4000,
            'بطاطس': 6000
        }.get(plant.get('name', 'قمح'), 3000) * area
        
        pest_control_cost = pest_pressure / 100 * 2000 * area
        ph_correction_cost = 1000 * area if ph_correction_needed else 0
        labor_cost = 5000 * area
        other_costs = 3000 * area
        
        total_cost = fertilizer_cost + water_cost_total + tillage_cost + seed_cost + pest_control_cost + ph_correction_cost + labor_cost + other_costs
        
        return {
            "الأسمدة": fertilizer_cost,
            "الري": water_cost_total,
            "الحراثة": tillage_cost,
            "البذور": seed_cost,
            "مكافحة_الآفات": pest_control_cost,
            "تصحيح_الحموضة": ph_correction_cost,
            "العمالة": labor_cost,
            "أخرى": other_costs,
            "المجموع": total_cost
        }
    
    def _generate_comparison_data_advanced(self, plant, wilaya, soil_type, water_system, fertilizer,
                                        area, n, p, k, irrigation, climate_scenario, temp_change, rain_change, co2_level,
                                        tillage, planting_date):
        """
        توليد بيانات المقارنة المتقدمة مع مراعاة الممارسات الزراعية
        """
        # سيناريو الحالي
        current = {
            "yield": plant['base_yield'] * area * 0.9,
            "cost": 25000 * area,
            "profitability": 15,
            "carbon_footprint": 1200 * area,
            "water_use": irrigation + wilaya['avg_rainfall']
        }
        
        # سيناريو محسن (زيادة كفاءة استخدام المياه والمغذيات)
        optimized = {
            "yield": plant['base_yield'] * area * 1.1,
            "cost": 22000 * area,
            "profitability": 25,
            "carbon_footprint": 900 * area,
            "water_use": (irrigation * 0.8) + wilaya['avg_rainfall']
        }
        
        # سيناريو مستدام (تقليل المدخلات وزيادة الكفاءة)
        sustainable = {
            "yield": plant['base_yield'] * area * 1.05,
            "cost": 20000 * area,
            "profitability": 30,
            "carbon_footprint": 700 * area,
            "water_use": (irrigation * 0.7) + wilaya['avg_rainfall']
        }
        
        return {
            "current": current,
            "optimized": optimized,
            "sustainable": sustainable,
            "labels": ["الإنتاجية", "التكلفة", "الربحية", "البصمة الكربونية", "استخدام المياه"]
        }
    
    def _generate_recommendations_advanced(self, heat_stress, water_stress, nue, profitability, 
                                        yield_ratio, soil_type, water_system, fertilizer,
                                        temp_change, rain_change, climate_risk, pest_pressure,
                                        plant, wilaya):
        """
        توليد التوصيات المتقدمة مع رؤى قابلة للتنفيذ
        """
        recommendations = []
        
        # توصيات درجة الحرارة
        if heat_stress > 25:
            recommendations.append({
                "category": "درجة الحرارة",
                "priority": "عالية",
                "message": f"درجات الحرارة مرتفعة ({heat_stress:.1f}%)، يوصى باستخدام أصناف مقاومة للحرارة أو تغيير موعد الزراعة."
            })
        elif heat_stress > 15:
            recommendations.append({
                "category": "درجة الحرارة",
                "priority": "متوسطة",
                "message": f"درجات الحرارة معتدلة ({heat_stress:.1f}%)، يوصى بمراقبة حالة النبات بانتظام."
            })
        
        # توصيات المياه
        if water_stress > 30:
            recommendations.append({
                "category": "المياه",
                "priority": "عالية",
                "message": f"إجهاد مائي مرتفع ({water_stress:.1f}%)، يوصى بزيادة كمية الري أو تحسين كفاءة الري الحالية."
            })
        elif water_stress > 15:
            recommendations.append({
                "category": "المياه",
                "priority": "متوسطة",
                "message": f"إجهاد مائي معتدل ({water_stress:.1f}%)، يوصى بمراجعة جدولة الري."
            })
        
        # توصيات المغذيات
        if nue < 50:
            recommendations.append({
                "category": "المغذيات",
                "priority": "عالية",
                "message": f"كفاءة استخدام المغذيات منخفضة ({nue:.1f}%)، يوصى بتحسين توقيت وطريقة التسميد."
            })
        elif nue < 70:
            recommendations.append({
                "category": "المغذيات",
                "priority": "متوسطة",
                "message": f"كفاءة استخدام المغذيات مقبولة ({nue:.1f}%)، يمكن تحسينها بتعديل جرعات السماد."
            })
        
        # توصيات الربحية
        if profitability < 10:
            recommendations.append({
                "category": "الاقتصاد",
                "priority": "عالية",
                "message": f"الربحية منخفضة ({profitability:.1f}%)، يوصى بمراجعة تكاليف الإنتاج أو اختيار محصول أكثر ربحية."
            })
        elif profitability < 20:
            recommendations.append({
                "category": "الاقتصاد",
                "priority": "متوسطة",
                "message": f"الربحية مقبولة ({profitability:.1f}%)، يمكن تحسينها بزيادة كفاءة العمليات."
            })
        
        # توصيات الإنتاجية
        if yield_ratio < 0.8:
            recommendations.append({
                "category": "الإنتاجية",
                "priority": "عالية",
                "message": f"الإنتاجية أقل من المتوقع ({yield_ratio*100:.1f}%)، يوصى بفحص صحة النبات والتأكد من توفر المغذيات."
            })
        elif yield_ratio < 0.95:
            recommendations.append({
                "category": "الإنتاجية",
                "priority": "متوسطة",
                "message": f"الإنتاجية قريبة من المتوقع ({yield_ratio*100:.1f}%)، يمكن تحسينها بتعديل الممارسات الزراعية."
            })
        
        # توصيات التربة
        if soil_type['ph'] < 6:
            recommendations.append({
                "category": "التربة",
                "priority": "متوسطة",
                "message": f"درجة حموضة التربة منخفضة ({soil_type['ph']:.1f})، يوصى بإضافة مواد قلوية لرفع درجة الحموضة."
            })
        elif soil_type['ph'] > 7.5:
            recommendations.append({
                "category": "التربة",
                "priority": "متوسطة",
                "message": f"درجة حموضة التربة مرتفعة ({soil_type['ph']:.1f})، يوصى بإضافة مواد حمضية لخفض درجة الحموضة."
            })
        
        # توصيات الري
        if water_system['efficiency'] < 0.8:
            recommendations.append({
                "category": "الري",
                "priority": "متوسطة",
                "message": f"كفاءة نظام الري منخفضة ({water_system['efficiency']*100:.1f}%)، يوصى بالتحول إلى نظام ري أكثر كفاءة مثل الري بالتنقيط."
            })
        
        # توصيات التغير المناخي
        if temp_change > 2:
            recommendations.append({
                "category": "التغير المناخي",
                "priority": "عالية",
                "message": f"زيادة درجات الحرارة المتوقعة ({temp_change:+.1f}°C)، يوصى باعتماد ممارسات زراعية أكثر تكيفاً مع التغير المناخي."
            })
        
        if abs(rain_change) > 20:
            recommendations.append({
                "category": "التغير المناخي",
                "priority": "عالية",
                "message": f"تغير كبير في كمية الهطول المتوقعة ({rain_change:+.1f}%)، يوصى باعتماد أنظمة ري تكميلية."
            })
        
        # توصيات مخاطر المناخ
        if climate_risk > 50:
            recommendations.append({
                "category": "مخاطر المناخ",
                "priority": "عالية",
                "message": f"مخاطر مناخية مرتفعة ({climate_risk:.1f}%)، يوصى باعتماد ممارسات زراعية تقلل من المخاطر."
            })
        
        # توصيات الآفات
        if pest_pressure > 30:
            recommendations.append({
                "category": "الآفات",
                "priority": "عالية",
                "message": f"ضغط الآفات مرتفع ({pest_pressure:.1f}%)، يوصى بزيادة إجراءات المكافحة المتكاملة للآفات."
            })
        elif pest_pressure > 15:
            recommendations.append({
                "category": "الآفات",
                "priority": "متوسطة",
                "message": f"ضغط الآفات معتدل ({pest_pressure:.1f}%)، يوصى بمراقبة الآفات بانتظام."
            })
        
        # إذا لم تكن هناك توصيات محددة، أضف توصية عامة
        if len(recommendations) == 0:
            recommendations.append({
                "category": "عامة",
                "priority": "منخفضة",
                "message": "الظروف الحالية مناسبة للزراعة، يوصى بالاستمرار في الممارسات الحالية ومراقبة المحصول بانتظام."
            })
        
        return recommendations