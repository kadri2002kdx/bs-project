import os
import sys
import json
import base64
import requests
import numpy as np
import random
import math
import logging
from datetime import datetime
from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,
    PageBreak, Frame, PageTemplate, BaseDocTemplate
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
import arabic_reshaper
from bidi.algorithm import get_display
from scipy import stats

# إعداد المسارات
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, 'backend')
sys.path.insert(0, backend_dir)

# استيراد الوحدات من backend
from config import config
from simulation_models import AgriculturalSimulation
from database import Database

# إنشاء التطبيق
app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

# إعدادات التطبيق
app_env = os.environ.get('FLASK_ENV', 'development')
app_config = config.get(app_env, config['default'])
app.config.from_object(app_config)

# إعداد السجلات
log_dir = os.path.join(current_dir, 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# إنشاء مثيلات الوحدات
db = Database()
simulation = AgriculturalSimulation()

# ========== مسارات الواجهة الأمامية ==========

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    try:
        return send_from_directory(app.static_folder, path)
    except:
        return send_from_directory(app.static_folder, '404.html'), 404

# ========== مسارات API للمحاكاة (من server.py) ==========

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    try:
        plants_count = len(db.get_all_plants())
        wilayas_count = len(db.get_all_wilayas())
        
        test_result = simulation.run_simulation(
            plant=db.get_plant_by_id(1),
            wilaya=db.get_wilaya_by_id(1),
            soil_type=db.get_soil_type_by_id(1),
            water_system=db.get_water_system_by_id(1),
            fertilizer=db.get_fertilizer_by_id(1),
            area=1.0,
            nitrogen=120,
            phosphorus=60,
            potassium=80
        )
        
        return jsonify({
            "success": True,
            "status": "يعمل بشكل طبيعي",
            "timestamp": datetime.now().isoformat(),
            "database": {
                "plants": plants_count,
                "wilayas": wilayas_count,
                "status": "متصل"
            },
            "simulation": {
                "status": "يعمل",
                "test_result": "ناجح" if test_result.get("success", False) else "فشل"
            }
        })
    except Exception as e:
        app.logger.error(f"Health check failed: {str(e)}")
        return jsonify({
            "success": False,
            "status": "خطأ",
            "error": str(e)
        }), 500

@app.route('/api/v1/plants', methods=['GET'])
def get_plants():
    try:
        plants = db.get_all_plants()
        return jsonify({"success": True, "count": len(plants), "data": plants})
    except Exception as e:
        app.logger.error(f"Error in get_plants: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/v1/wilayas', methods=['GET'])
def get_wilayas():
    try:
        wilayas = db.get_all_wilayas()
        return jsonify({"success": True, "count": len(wilayas), "data": wilayas})
    except Exception as e:
        app.logger.error(f"Error in get_wilayas: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/v1/soil-types', methods=['GET'])
def get_soil_types():
    try:
        soil_types = db.get_all_soil_types()
        return jsonify({"success": True, "count": len(soil_types), "data": soil_types})
    except Exception as e:
        app.logger.error(f"Error in get_soil_types: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/v1/water-management', methods=['GET'])
def get_water_management():
    try:
        water_systems = db.get_all_water_systems()
        return jsonify({"success": True, "count": len(water_systems), "data": water_systems})
    except Exception as e:
        app.logger.error(f"Error in get_water_management: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/v1/fertilizer-types', methods=['GET'])
def get_fertilizer_types():
    try:
        fertilizers = db.get_all_fertilizers()
        return jsonify({"success": True, "count": len(fertilizers), "data": fertilizers})
    except Exception as e:
        app.logger.error(f"Error in get_fertilizer_types: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/v1/simulate', methods=['POST'])
def run_simulation():
    try:
        if not request.is_json:
            return jsonify({"success": False, "error": "يجب أن يكون الطلب من نوع JSON"}), 400
        
        data = request.get_json()
        
        if not data:
            return jsonify({"success": False, "error": "لم يتم تقديم أي بيانات"}), 400
        
        required_fields = ['plant_id', 'wilaya_id', 'area_ha']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            return jsonify({
                "success": False, 
                "error": f"الحقول المطلوبة مفقودة: {', '.join(missing_fields)}"
            }), 400
        
        plant_id = int(data.get('plant_id', 1))
        wilaya_id = int(data.get('wilaya_id', 1))
        soil_type_id = int(data.get('soil', 1))
        water_system_id = int(data.get('water', 1))
        fertilizer_id = int(data.get('fertilizer', 1))
        area = float(data.get('area_ha', 1.0))
        
        nitrogen = float(data.get('nitrogen', 120))
        phosphorus = float(data.get('phosphorus', 60))
        potassium = float(data.get('potassium', 80))
        
        irrigation_amount = float(data.get('irrigation_amount', 5000))
        irrigation_frequency = int(data.get('irrigation_frequency', 7))
        water_quality = float(data.get('water_quality', 1.2))
        
        climate_scenario = data.get('climate_scenario', 'current')
        years = int(data.get('years', 5))
        temp_change = float(data.get('delta_temp_c', 0))
        rain_change = float(data.get('delta_rain_pct', 0))
        co2_level = float(data.get('co2_ppm', 420))
        
        monte_carlo_runs = int(data.get('monte_carlo_runs', 100))
        pest_pressure = float(data.get('pest_pressure_pct', 10))
        tillage = data.get('tillage', 'conventional')
        
        plant = db.get_plant_by_id(plant_id)
        wilaya = db.get_wilaya_by_id(wilaya_id)
        soil_type = db.get_soil_type_by_id(soil_type_id)
        water_system = db.get_water_system_by_id(water_system_id)
        fertilizer = db.get_fertilizer_by_id(fertilizer_id)
        
        missing_entities = []
        if not plant: missing_entities.append(f"نبات (ID: {plant_id})")
        if not wilaya: missing_entities.append(f"ولاية (ID: {wilaya_id})")
        if not soil_type: missing_entities.append(f"نوع تربة (ID: {soil_type_id})")
        if not water_system: missing_entities.append(f"نظام ري (ID: {water_system_id})")
        if not fertilizer: missing_entities.append(f"سماد (ID: {fertilizer_id})")
        
        if missing_entities:
            return jsonify({
                "success": False, 
                "error": f"بيانات غير موجودة: {', '.join(missing_entities)}"
            }), 404
        
        app.logger.info(f"بدء محاكاة: نبات={plant_id}, ولاية={wilaya_id}, مساحة={area} هكتار")
        
        results = simulation.run_simulation(
            plant=plant,
            wilaya=wilaya,
            soil_type=soil_type,
            water_system=water_system,
            fertilizer=fertilizer,
            area=area,
            nitrogen=nitrogen,
            phosphorus=phosphorus,
            potassium=potassium,
            irrigation_amount=irrigation_amount,
            irrigation_frequency=irrigation_frequency,
            water_quality=water_quality,
            climate_scenario=climate_scenario,
            years=years,
            temp_change=temp_change,
            rain_change=rain_change,
            co2_level=co2_level,
            monte_carlo_runs=monte_carlo_runs,
            pest_pressure=pest_pressure,
            tillage=tillage
        )
        
        app.logger.info(f"تمت المحاكاة بنجاح: نبات={plant_id}, ولاية={wilaya_id}")
        
        return jsonify({"success": True, **results})
    
    except ValueError as e:
        app.logger.error(f"خطأ في القيم: {str(e)}")
        return jsonify({"success": False, "error": f"قيم غير صحيحة: {str(e)}"}), 400
    except Exception as e:
        app.logger.error(f"خطأ غير متوقع في المحاكاة: {str(e)}")
        return jsonify({"success": False, "error": f"خطأ غير متوقع: {str(e)}"}), 500

# ========== مسارات API للأنظمة البيئية والأنواع ==========

@app.route('/api/ecosystems', methods=['GET'])
def get_ecosystems():
    """الحصول على قائمة الأنظمة البيئية"""
    try:
        # محاولة قراءة البيانات من ملف JSON
        ecosystems_file = os.path.join(current_dir, 'ecosystems_data.json')
        
        if os.path.exists(ecosystems_file):
            with open(ecosystems_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return jsonify(data)
        else:
            # إذا لم يكن الملف موجودًا، أرجع بيانات نموذجية
            mock_ecosystems = {
                "ecosystems": [
                    {
                        "id": "eco-1",
                        "name": "بحيرة عياطة",
                        "wilaya": "المغير",
                        "type": "أراضي رطبة",
                        "coords": {"lat": 33.533, "lng": 6.900},
                        "area": "3500-4000 هكتار",
                        "altitude": "32 م",
                        "climate": "صحراوي جاف (BWh) حسب تصنيف كوبن للمناخ",
                        "biodiversity_index": "عالٍ"
                    },
                    {
                        "id": "eco-2",
                        "name": "الشريعة - الأرز",
                        "wilaya": "البليدة",
                        "type": "غابة صنوبرية",
                        "coords": {"lat": 36.433, "lng": 2.800},
                        "area": "3200 هكتار",
                        "altitude": "1500-1800 م",
                        "climate": "متوسطي رطب (Csa) مع تساقط ثلوج في الشتاء",
                        "biodiversity_index": "عالٍ جداً"
                    }
                ]
            }
            return jsonify(mock_ecosystems)
    except Exception as e:
        app.logger.error(f"Error in get_ecosystems: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/species', methods=['GET'])
def get_species():
    """الحصول على قائمة الأنواع"""
    try:
        # محاولة قراءة البيانات من ملف JSON
        species_file = os.path.join(current_dir, 'species_data.json')
        
        if os.path.exists(species_file):
            with open(species_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return jsonify(data)
        else:
            # إذا لم يكن الملف موجودًا، أرجع بيانات نموذجية
            mock_species = {
                "plants": [
                    {
                        "id": "plant-1",
                        "name": "شجرة الأرز الأطلسي",
                        "sciName": "Cedrus atlantica",
                        "description": "شجرة دائمة الخضرة تنمو في جبال الأطلس",
                        "region": "mountains",
                        "status": "endangered",
                        "type": "tree"
                    },
                    {
                        "id": "plant-2",
                        "name": "شجرة الزيتون",
                        "sciName": "Olea europaea",
                        "description": "شجرة دائمة الخضرة ذات أهمية اقتصادية كبيرة",
                        "region": "north",
                        "status": "secure",
                        "type": "tree"
                    }
                ],
                "animals": [
                    {
                        "id": "animal-1",
                        "name": "فهد الصحراء",
                        "sciName": "Acinonyx jubatus hecki",
                        "description": "أحد أنواع الفهود المهددة بالانقراض",
                        "region": "desert",
                        "status": "critical",
                        "type": "mammal"
                    }
                ],
                "fungi": [
                    {
                        "id": "fungi-1",
                        "name": "فطر الكمأة البيضاء",
                        "sciName": "Tuber magnatum",
                        "description": "فطر صحراوي نادر ينمو تحت الأرض",
                        "region": "desert",
                        "status": "vulnerable",
                        "type": "mushroom"
                    }
                ]
            }
            return jsonify(mock_species)
    except Exception as e:
        app.logger.error(f"Error in get_species: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

# ========== مسارات API للتحليل (من app.py) ==========

# إعدادات الخطوط متعددة اللغات
try:
    pdfmetrics.registerFont(TTFont('Arabic', 'arial.ttf'))
    pdfmetrics.registerFont(TTFont('Arabic-Bold', 'arialbd.ttf'))
    pdfmetrics.registerFont(TTFont('Latin', 'arial.ttf'))
    pdfmetrics.registerFont(TTFont('Latin-Bold', 'arialbd.ttf'))
except:
    try:
        pdfmetrics.registerFont(TTFont('Arabic', 'c:/windows/fonts/arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arabic-Bold', 'c:/windows/fonts/arialbd.ttf'))
        pdfmetrics.registerFont(TTFont('Latin', 'c:/windows/fonts/arial.ttf'))
        pdfmetrics.registerFont(TTFont('Latin-Bold', 'c:/windows/fonts/arialbd.ttf'))
    except:
        print("Warning: Custom fonts not found. Using default fonts.")
        pdfmetrics.registerFont(TTFont('Arabic', 'Helvetica'))
        pdfmetrics.registerFont(TTFont('Arabic-Bold', 'Helvetica-Bold'))
        pdfmetrics.registerFont(TTFont('Latin', 'Helvetica'))
        pdfmetrics.registerFont(TTFont('Latin-Bold', 'Helvetica-Bold'))

API_KEY = "IqjlPs2uNLx3cmzjM1wKX5oHiVsLXgsLHXBYEr36q5GbsNqRa9"
API_URL = "https://plant.id/api/v3/identification"

DISEASE_TRANSLATIONS = {
    "Tomato___Late_blight": {
        "ar": "اللفحة المتأخرة على الطماطم",
        "en": "Tomato Late Blight",
        "fr": "Mildiou de la tomate"
    },
    "Tomato___Yellow_Leaf_Curl_Virus": {
        "ar": "فيروس تجعد الأوراق الأصفر على الطماطم",
        "en": "Tomato Yellow Leaf Curl Virus",
        "fr": "Virus de l'enroulement des feuilles jaunes de la tomate"
    },
    "Apple___Apple_scab": {
        "ar": "جرب التفاح",
        "en": "Apple Scab",
        "fr": "Tavelure du pommier"
    },
    "Apple___Black_rot": {
        "ar": "العفن الأسود للتفاح",
        "en": "Apple Black Rot",
        "fr": "Pourriture noire du pommier"
    },
    "Apple___Cedar_apple_rust": {
        "ar": "صدأ أرز التفاح",
        "en": "Apple Cedar Rust",
        "fr": "Rouille du cèdre du pommier"
    },
    "Corn___Cercospora_leaf_spot Gray_leaf_spot": {
        "ar": "تبقع أوراق الذرة",
        "en": "Corn Gray Leaf Spot",
        "fr": "Tache grise des feuilles de maïs"
    },
    "Grape___Black_rot": {
        "ar": "العفن الأسود للعنب",
        "en": "Grape Black Rot",
        "fr": "Pourriture noire de la vigne"
    },
    "Healthy": {
        "ar": "سليم",
        "en": "Healthy",
        "fr": "Sain"
    }
}

PLANT_ADVICE = {
    "Tomato___Late_blight": {
        "ar": [
            "رش مبيد فطري مناسب مثل الكلوروثالونيل أو المانكوزيب",
            "إزالة الأجزاء المصابة والتخلص منها بشكل آمن",
            "تحسين التهوية حول النباتات",
            "تجنب الري العلوي لتقليل الرطوبة على الأوراق",
            "تطبيق برنامج رش وقائي خلال الطقس الرطب"
        ],
        "en": [
            "Spray appropriate fungicide such as chlorothalonil or mancozeb",
            "Remove and safely dispose of infected parts",
            "Improve ventilation around plants",
            "Avoid overhead irrigation to reduce leaf moisture",
            "Apply preventive spray program during wet weather"
        ],
        "fr": [
            "Pulvériser un fongicide approprié comme le chlorothalonil ou le mancozèbe",
            "Retirer et éliminer en toute sécurité les parties infectées",
            "Améliorer la ventilation autour des plantes",
            "Éviter l'irrigation par-dessus pour réduire l'humidité des feuilles",
            "Appliquer un programme de pulvérisation préventive par temps humide"
        ]
    },
    "Tomato___Yellow_Leaf_Curl_Virus": {
        "ar": [
            "إزالة النباتات المصابة لمنع انتشار الفيروس",
            "مكافحة الذبابة البيضاء باستخدام مصائد لاصقة أو مبيدات حشرية",
            "استخدام أصناف مقاومة للفيروس",
            "تغطية النباتات بشبكات واقية لمنع وصول الحشرات الناقلة"
        ],
        "en": [
            "Remove infected plants to prevent virus spread",
            "Control whiteflies using sticky traps or insecticides",
            "Use virus-resistant varieties",
            "Cover plants with protective nets to prevent insect vectors"
        ],
        "fr": [
            "Retirer les plantes infectées pour prévenir la propagation du virus",
            "Contrôler les aleurodes avec des pièges collants ou des insecticides",
            "Utiliser des variétés résistantes au virus",
            "Couvrir les plantes avec des filets de protection pour empêcher les insectes vecteurs"
        ]
    },
    "Healthy": {
        "ar": [
            "استمر في برنامج الرعاية الحالي",
            "حافظ على ري منتظم ومناسب",
            "استخدم سمادًا متوازنًا وفقًا لاحتياجات النبات",
            "راقب النبات بانتظام لاكتشاف أي مشاكل مبكرًا"
        ],
        "en": [
            "Continue with current care program",
            "Maintain regular and appropriate watering",
            "Use balanced fertilizer according to plant needs",
            "Regularly monitor the plant for early problem detection"
        ],
        "fr": [
            "Continuer avec le programme de soins actuel",
            "Maintenir un arrosage régulier et approprié",
            "Utiliser un engrais équilibré selon les besoins de la plante",
            "Surveiller régulièrement la plante pour une détection précoce des problèmes"
        ]
    }
}

def arabic_text(text):
    try:
        reshaped_text = arabic_reshaper.reshape(text)
        return get_display(reshaped_text)
    except:
        return text

def identify_plant(image_data):
    try:
        if "," in image_data:
            image_data = image_data.split(",")[1]
        payload = {
            "images": [image_data],
            "similar_images": True,
            "health": "all"
        }
        headers = {
            "Content-Type": "application/json",
            "Api-Key": API_KEY
        }
        response = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        
        if response.status_code == 201:
            return response.json()
        else:
            print(f"API Error: {response.status_code} - {response.text}")
            return {"error": f"API request failed with {response.status_code}"}
            
    except Exception as e:
        print(f"API Exception: {str(e)}")
        return {"error": f"API exception: {str(e)}"}

@app.route('/api/analyze', methods=['POST'])
def analyze_plant():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        image_data = data.get('image')
        user_notes = data.get('notes', '')
        language = data.get('language', 'ar')
        
        if not image_data:
            return jsonify({"error": "No image provided"}), 400
        
        if not isinstance(image_data, str) or not image_data.startswith('data:image'):
            return jsonify({"error": "Invalid image format"}), 400
        
        result = identify_plant(image_data)
        if 'error' in result:
            return jsonify({"error": result['error']}), 500
        
        is_plant_prob = result.get("result", {}).get("is_plant", {}).get("probability", 0)
        
        if is_plant_prob < 0.15:
            error_messages = {
                "ar": "الصورة لا تحتوي على نبات واضح",
                "en": "The image does not contain a clear plant",
                "fr": "L'image ne contient pas de plante claire"
            }
            suggestion_messages = {
                "ar": "يرجى تحميل صورة أكثر وضوحاً تظهر الأوراق أو الثمار بشكل واضح",
                "en": "Please upload a clearer image showing leaves or fruits clearly",
                "fr": "Veuillez télécharger une image plus claire montrant les feuilles ou les fruits clairement"
            }
            
            return jsonify({
                "error": error_messages.get(language, error_messages["ar"]),
                "is_plant_probability": round(is_plant_prob * 100, 2),
                "details": f"{round(is_plant_prob * 100, 2)}%",
                "suggestion": suggestion_messages.get(language, suggestion_messages["ar"]),
                "status": "low_confidence"
            }), 400
        
        suggestions = result.get("result", {}).get("classification", {}).get("suggestions", [])
        best_match = suggestions[0] if suggestions else {}
        
        health = result.get("result", {}).get("is_healthy", {})
        
        health_status_messages = {
            "ar": {"healthy": "سليم", "unhealthy": "مريض"},
            "en": {"healthy": "Healthy", "unhealthy": "Unhealthy"},
            "fr": {"healthy": "Sain", "unhealthy": "Malade"}
        }
        
        health_status = health_status_messages[language]["healthy"] if health.get('binary', False) else health_status_messages[language]["unhealthy"]
        health_probability = health.get('probability', 0) * 100
        
        diseases = result.get("result", {}).get("disease", {}).get("suggestions", [])
        diseases_list = []
        if diseases:
            for d in diseases[:3]:
                disease_name = DISEASE_TRANSLATIONS.get(d['name'], {}).get(language, d['name'])
                diseases_list.append(f"{disease_name} ({d['probability']*100:.1f}%)")
        
        recommendations = PLANT_ADVICE.get("Healthy", {}).get(language, [])
        if diseases and diseases[0]['name'] in PLANT_ADVICE:
            recommendations = PLANT_ADVICE[diseases[0]['name']].get(language, [])
        
        response_data = {
            "plant_type": best_match.get('name', 'Unknown'),
            "confidence": round(best_match.get('probability', 0) * 100, 2),
            "health_status": health_status,
            "health_confidence": round(health_probability, 2),
            "diseases": diseases_list,
            "recommendations": recommendations,
            "is_plant_probability": round(is_plant_prob * 100, 2),
            "timestamp": datetime.now().isoformat(),
            "user_notes": user_notes,
            "language": language
        }
        
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# ========== مسار إنشاء التقارير ==========

@app.route('/api/report', methods=['POST'])
def generate_report():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        analysis_data = data.get('analysis_data', {})
        image_data = data.get('image_data')
        language = data.get('language', 'ar')
        
        buffer = BytesIO()
        
        doc = SimpleDocTemplate(buffer, pagesize=A4,
                                rightMargin=2.5*cm, leftMargin=2.5*cm,
                                topMargin=3*cm, bottomMargin=2.5*cm)
        
        styles = getSampleStyleSheet()
        
        title_style = ParagraphStyle(
            name="ReportTitle", 
            fontSize=18, 
            alignment=1, 
            textColor=colors.HexColor("#2e7d32"),
            spaceAfter=20,
            fontName="Arabic-Bold" if language == "ar" else "Latin-Bold"
        )
        
        section_style = ParagraphStyle(
            name="SectionHeader", 
            fontSize=14, 
            textColor=colors.HexColor("#2e7d32"), 
            spaceAfter=12,
            spaceBefore=20,
            fontName="Arabic-Bold" if language == "ar" else "Latin-Bold",
            leftIndent=5
        )
        
        body_style = ParagraphStyle(
            name="BodyTextCustom", 
            fontSize=11, 
            leading=14,
            textColor=colors.HexColor("#333333"),
            fontName="Arabic" if language == "ar" else "Latin",
            spaceAfter=6,
            alignment=2 if language == "ar" else 0
        )
        
        content = []
        
        # العنوان الرئيسي
        title_text = {
            "ar": "تقرير تحليل النبات",
            "en": "Plant Analysis Report",
            "fr": "Rapport d'analyse des plantes"
        }
        
        content.append(Paragraph(
            arabic_text(title_text[language]) if language == "ar" else title_text[language], 
            title_style
        ))
        content.append(Spacer(1, 15))
        
        # إضافة صورة النبات إذا كانت متوفرة
        if image_data:
            try:
                img_bytes = base64.b64decode(image_data.split(",")[1])
                img_buffer = BytesIO(img_bytes)
                plant_img = Image(img_buffer, width=10*cm, height=7*cm)
                plant_img.hAlign = 'CENTER'
                content.append(plant_img)
                content.append(Spacer(1, 20))
            except Exception as e:
                error_text = {
                    "ar": "تعذر إدراج صورة النبات",
                    "en": "Failed to insert plant image",
                    "fr": "Échec de l'insertion de l'image de la plante"
                }
                content.append(Paragraph(
                    arabic_text(error_text[language]) if language == "ar" else error_text[language], 
                    body_style
                ))
        
        # قسم المعلومات الأساسية
        info_title = {
            "ar": "المعلومات الأساسية",
            "en": "Basic Information",
            "fr": "Informations de base"
        }
        
        content.append(Paragraph(
            arabic_text(info_title[language]) if language == "ar" else info_title[language], 
            section_style
        ))
        
        # نصوص الترجمة للجدول
        date_text = {"ar": "التاريخ", "en": "Date", "fr": "Date"}
        plant_type_text = {"ar": "نوع النبات", "en": "Plant Type", "fr": "Type de plante"}
        health_status_text = {"ar": "الحالة الصحية", "en": "Health Status", "fr": "État de santé"}
        confidence_text = {"ar": "نسبة الثقة", "en": "Confidence", "fr": "Confiance"}
        
        info_data = [
            [
                Paragraph(arabic_text(date_text[language]) if language == "ar" else date_text[language], body_style), 
                Paragraph(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), body_style)
            ],
            [
                Paragraph(arabic_text(plant_type_text[language]) if language == "ar" else plant_type_text[language], body_style), 
                Paragraph(analysis_data.get("plant_type", "Unknown"), body_style)
            ],
            [
                Paragraph(arabic_text(health_status_text[language]) if language == "ar" else health_status_text[language], body_style), 
                Paragraph(analysis_data.get("health_status", "Unknown"), body_style)
            ],
            [
                Paragraph(arabic_text(confidence_text[language]) if language == "ar" else confidence_text[language], body_style), 
                Paragraph(f"{analysis_data.get('confidence', 0)}%", body_style)
            ],
        ]
        
        info_table = Table(info_data, colWidths=[4*cm, 10*cm])
        info_table.setStyle(TableStyle([
            ("ALIGN", (0, 0), (-1, -1), "RIGHT" if language == "ar" else "LEFT"),
            ("FONTNAME", (0, 0), (-1, -1), "Arabic" if language == "ar" else "Latin"),
            ("FONTSIZE", (0, 0), (-1, -1), 11),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("LINEBELOW", (0, 0), (-1, -1), 1, colors.HexColor("#e0e0e0")),
            ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#f5f5f5")),
            ("BACKGROUND", (1, 0), (1, -1), colors.HexColor("#fafafa")),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#333333")),
            ("FONTNAME", (0, 0), (0, -1), "Arabic-Bold" if language == "ar" else "Latin-Bold"),
        ]))
        content.append(info_table)
        content.append(Spacer(1, 20))
        
        # قسم الأمراض إذا كانت موجودة
        if analysis_data.get("diseases") and len(analysis_data.get("diseases")) > 0:
            diseases_title = {
                "ar": "الأمراض المحتملة",
                "en": "Possible Diseases",
                "fr": "Maladies possibles"
            }
            
            content.append(Paragraph(
                arabic_text(diseases_title[language]) if language == "ar" else diseases_title[language], 
                section_style
            ))
            
            diseases_text = ", ".join(analysis_data.get("diseases", []))
            content.append(Paragraph(diseases_text, body_style))
            content.append(Spacer(1, 20))
        
        # قسم التوصيات
        recommendations_title = {
            "ar": "التوصيات",
            "en": "Recommendations",
            "fr": "Recommandations"
        }
        
        content.append(Paragraph(
            arabic_text(recommendations_title[language]) if language == "ar" else recommendations_title[language], 
            section_style
        ))
        
        for rec in analysis_data.get("recommendations", []):
            content.append(Paragraph(f"• {rec}", body_style))
        
        # بناء المستند
        doc.build(content)
        
        buffer.seek(0)
        return send_file(buffer,
                         as_attachment=True,
                         download_name=f"plant_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                         mimetype="application/pdf")
    except Exception as e:
        return jsonify({"error": f"PDF error: {str(e)}"}), 500

# ========== معالجة المسارات غير الصالحة ==========

@app.route('/<path:path>')
def handle_invalid_routes(path):
    """معالجة المسارات غير الصالحة"""
    # إذا كان المسار يحتوي على متغيرات قالب غير مستبدلة
    if '${' in path or path == 'undefined':
        app.logger.warning(f"Invalid route requested: {path}")
        return jsonify({"error": "Invalid route"}), 404
    
    # محاولة تقديم الملف من المجلد الثابت
    try:
        return send_from_directory(app.static_folder, path)
    except:
        return jsonify({"error": "Resource not found"}), 404

# ========== إضافة رؤوس للتحكم في التخزين المؤقت ==========

@app.after_request
def add_cache_headers(response):
    """إضافة رؤوس للتحكم في التخزين المؤقت"""
    if request.endpoint and 'static' in request.endpoint:
        response.cache_control.max_age = 86400  # يوم واحد
        response.cache_control.public = True
    return response

# ========== تشغيل التطبيق ==========

if __name__ == '__main__':
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    
    print(f"\n🌱 جاري تشغيل خادم EcoPlant DZ...")
    print(f"📍 متاح على: http://{host}:{port}")
    print(f"📍 البيئة: {app_env}")
    print("\n🛑 اضغط على CTRL+C لإيقاف الخادم")
    
    app.run(host=host, port=port, debug=app_config.DEBUG)