import json
import os

def create_complete_species_data():
    """إنشاء بيانات كاملة للأنواع تتوافق مع متطلبات واجهة المستخدم"""
    
    data = {
        "plants": [
            {
                "id": "plant-1",
                "name": "شجرة الأرز الأطلسي",
                "sciName": "Cedrus atlantica",
                "description": "شجرة دائمة الخضرة تنمو في جبال الأطلس، يصل ارتفاعها إلى 40 متراً. تعتبر من الأنواع المهددة بسبب القطع الجائر والتغيرات المناخية. تتميز بخشبها العالي الجودة وأوراقها الإبرية الدائمة الخضرة.",
                "image": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
                "images": [
                    "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1512428813834-c702c770a65f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
                ],
                "region": "mountains",
                "status": "endangered",
                "type": "tree",
                "conservation": {
                    "level": "protected",
                    "trend": "متناقص",
                    "threats": "القطع الجائر، التغير المناخي، الحرائق",
                    "actions": "محميات طبيعية، منع القطع، برامج إعادة التشجير",
                    "size": "أقل من 10000 شجرة بالغة",
                    "density": "منخفضة",
                    "fragmentation": "عالية",
                    "efforts": "تم إنشاء عدة محميات طبيعية في جبال الأطلس لحماية هذه الشجرة، وتنفذ برامج لإعادة التشجير ومراقبة السكان المتبقين."
                },
                "ecology": {
                    "habitat": "forest",
                    "temperature": "5-25°C",
                    "rainfall": "600-1500 ملم سنوياً",
                    "soil": "تربة غنية جيدة التصريف",
                    "ph": "5.5-7.5",
                    "symbiosis": "تعيش في تعايش مع فطريات الجذور",
                    "predators": "قليلة بسبب حجمها الكبير",
                    "parasites": "بعض أنواع الحشرات والفطريات",
                    "pollination": "عن طريق الرياح"
                },
                "biology": {
                    "size": "يصل إلى 40 متر ارتفاعاً و2 متر قطراً",
                    "weight": "يصل إلى 10 أطنان للشجرة البالغة",
                    "shape": "مخروطي الشكل، أفرع أفقية",
                    "colors": "أخضر داكن للأوراق، بني للجذع",
                    "breeding": "من سبتمبر إلى نوفمبر",
                    "reproduction": "تتكاثر بالأبواغ الذكرية والأنثوية",
                    "growth": "بطيئة (10-15 سم سنوياً)",
                    "lifespan": "500-1000 سنة",
                    "diet": "تتغذى على المعادن والمواد العضوية من التربة"
                },
                "distribution": {
                    "region": "جبال الأطلس",
                    "habitat": "الغابات الجبلية على ارتفاعات 1500-2500 متر",
                    "elevation": "1500-2500 متر فوق سطح البحر",
                    "presence": "متفرقة في جبال الأطلس الجزائرية"
                },
                "taxonomy": {
                    "kingdom": "النباتات",
                    "phylum": "مخروطيات",
                    "class": "صنوبرانية",
                    "order": "صنوبريات",
                    "family": "الصنوبرية",
                    "genus": "الأرز"
                }
            },
            {
                "id": "plant-2",
                "name": "شجرة الزيتون",
                "sciName": "Olea europaea",
                "description": "شجرة دائمة الخضرة ذات أهمية اقتصادية كبيرة في منطقة البحر الأبيض المتوسط. تنتج ثمار الزيتون التي تستخدم للطعام واستخراج زيت الزيتون.",
                "image": "https://images.unsplash.com/photo-1571667140536-8dbe9e54cfb3?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
                "images": [
                    "https://images.unsplash.com/photo-1571667140536-8dbe9e54cfb3?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1470058869958-2a77ade41c4d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
                ],
                "region": "north",
                "status": "secure",
                "type": "tree",
                "conservation": {
                    "level": "unprotected",
                    "trend": "مستقر",
                    "threats": "الأمراض الفطرية، تغير المناخ",
                    "actions": "لا توجد إجراءات حماية محددة",
                    "size": "واسع الانتشار",
                    "density": "عالية",
                    "fragmentation": "منخفضة",
                    "efforts": "لا توجد جهود حماية محددة."
                },
                "ecology": {
                    "habitat": "forest",
                    "temperature": "10-35°C",
                    "rainfall": "400-800 ملم سنوياً",
                    "soil": "تربة جيرية جيدة التصريف",
                    "ph": "6.0-8.5",
                    "symbiosis": "تتعايش مع بعض الفطريات الجذرية",
                    "predators": "بعض الحشرات والقوارض",
                    "parasites": "ذبابة ثمار الزيتون، بعض الفطريات",
                    "pollination": "عن طريق الرياح"
                },
                "biology": {
                    "size": "يصل إلى 10 أمتار ارتفاعاً",
                    "weight": "يصل إلى 2 طن للشجرة البالغة",
                    "shape": "شجرة متوسطة الحجم، تاج كثيف",
                    "colors": "أخضر فضي للأوراق، بني للجذع",
                    "breeding": "من مايو إلى يونيو",
                    "reproduction": "تتكاثر بالبذور والعقل",
                    "growth": "بطيئة إلى متوسطة",
                    "lifespan": "300-600 سنة",
                    "diet": "تتغذى على المعادن من التربة"
                },
                "distribution": {
                    "region": "مناطق البحر المتوسط",
                    "habitat": "المناطق الجبلية والهضاب",
                    "elevation": "0-1000 متر فوق سطح البحر",
                    "presence": "منتشر في شمال الجزائر"
                },
                "taxonomy": {
                    "kingdom": "النباتات",
                    "phylum": "مستورات البذور",
                    "class": "ثنائيات الفلقة",
                    "order": "شفويات",
                    "family": "الزيتونية",
                    "genus": "الزيتون"
                }
            },
            # سيتم إضافة باقي النباتات هنا بنفس التفصيل
        ],
        "animals": [
            {
                "id": "animal-1",
                "name": "فهد الصحراء",
                "sciName": "Acinonyx jubatus hecki",
                "description": "أحد أنواع الفهود المهددة بالانقراض الذي يتواجد في مناطق الصحراء الكبرى، يتميز بسرعته الفائقة وقدرته على التكيف مع الظروف الصحراوية.",
                "image": "https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
                "images": [
                    "https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1506891532572-ecbd35c5350b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
                ],
                "region": "desert",
                "status": "critical",
                "type": "mammal",
                "conservation": {
                    "level": "protected",
                    "trend": "متناقص بشكل خطير",
                    "threats": "فقدان الموائل، الصيد الجائر، نقص الفرائس",
                    "actions": "محميات طبيعية، برامج التكاثر في الأسر",
                    "size": "أقل من 250 فرد بالغ",
                    "density": "منخفضة جداً",
                    "fragmentation": "عالية جداً",
                    "efforts": "برامج حماية دولية، إنشاء محميات، مكافحة الصيد غير المشروع"
                },
                "ecology": {
                    "habitat": "desert",
                    "temperature": "20-45°C",
                    "rainfall": "50-150 ملم سنوياً",
                    "soil": "رملية وصخرية",
                    "ph": "6.5-8.5",
                    "symbiosis": "لا يوجد",
                    "predators": "لا يوجد مفترسات طبيعية",
                    "parasites": "البراغيث والقراد",
                    "pollination": "لا ينطبق"
                },
                "biology": {
                    "size": "110-135 سم طول الجسم، 70-90 سم ارتفاع الكتف",
                    "weight": "35-65 كجم",
                    "shape": "جسم رشيق، رأس صغير، أطراف طويلة",
                    "colors": "أصفر باهت مع بقع سوداء",
                    "breeding": "على مدار العام",
                    "reproduction": "ولودة، 3-5 جراء في البطن",
                    "growth": "سريع في السنة الأولى",
                    "lifespan": "10-12 سنة في البرية",
                    "diet": "لواحم: غزلان، أرانب، طيور، وزواحف"
                },
                "distribution": {
                    "region": "الصحراء الكبرى",
                    "habitat": "المناطق الصحراوية وشبه الصحراوية",
                    "elevation": "تحت 1000 متر",
                    "presence": "نادر جداً ومتفرق"
                },
                "taxonomy": {
                    "kingdom": "الحيوانات",
                    "phylum": "الحبليات",
                    "class": "الثدييات",
                    "order": "لواحم",
                    "family": "السنوريات",
                    "genus": "Acinonyx"
                }
            },
            # سيتم إضافة باقي الحيوانات هنا بنفس التفصيل
        ],
        "fungi": [
            {
                "id": "fungi-1",
                "name": "فطر الكمأة البيضاء",
                "sciName": "Tuber magnatum",
                "description": "فطر صحراوي نادر ينمو تحت الأرض، يعتبر من أغلى أنواع الفطريات في العالم due to ندرته ونكهته المميزة.",
                "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
                "images": [
                    "https://images.unsplash.com/photo-1578662996442-48f60103fc96?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1519708227416-6f6d37eef2db?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
                ],
                "region": "desert",
                "status": "vulnerable",
                "type": "mushroom",
                "conservation": {
                    "level": "unprotected",
                    "trend": "مستقر",
                    "threats": "القطف الجائر، تغير المناخ",
                    "actions": "لا توجد إجراءات حماية محددة",
                    "size": "غير معروف",
                    "density": "منخفضة",
                    "fragmentation": "عالية",
                    "efforts": "لا توجد جهود حماية محددة."
                },
                "ecology": {
                    "habitat": "desert",
                    "temperature": "15-25°C",
                    "rainfall": "100-300 ملم سنوياً",
                    "soil": "رملية جيرية",
                    "ph": "7.0-8.5",
                    "symbiosis": "يتعايش مع جذور بعض النباتات الصحراوية",
                    "predators": "بعض القوارض والحشرات",
                    "parasites": "قليلة",
                    "pollination": "لا ينطبق"
                },
                "biology": {
                    "size": "2-10 سم قطراً",
                    "weight": "10-100 غرام",
                    "shape": "كروي إلى غير منتظم",
                    "colors": "أبيض إلى بيج",
                    "breeding": "خريف وربيع",
                    "reproduction": "أبواغ",
                    "growth": "بطيئة تحت الأرض",
                    "lifespan": "عدة أشهر",
                    "diet": "يتغذى على المواد العضوية في التربة"
                },
                "distribution": {
                    "region": "الصحراء",
                    "habitat": "المناطق الصحراوية تحت أشجار معينة",
                    "elevation": "تحت 500 متر",
                    "presence": "نادر ومتفرق"
                },
                "taxonomy": {
                    "kingdom": "الفطريات",
                    "phylum": "فطريات زقية",
                    "class": "Pezizomycetes",
                    "order": "Pezizales",
                    "family": "Tuberaceae",
                    "genus": "Tuber"
                }
            },
            # سيتم إضافة باقي الفطريات هنا بنفس التفصيل
        ]
    }
    
    # إضافة المزيد من البيانات هنا...
    
    return data

def save_to_json(data, file_path):
    """حفظ البيانات إلى ملف JSON"""
    # التأكد من وجود المجلد
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"تم حفظ البيانات في: {file_path}")

if __name__ == "__main__":
    # إنشاء البيانات
    species_data = create_complete_species_data()
    
    # تحديد مسار الحفظ
    save_path = r"C:\Users\LAPTA\ecoplant-dz\species_data.json"
    
    # حفظ البيانات في ملف JSON
    save_to_json(species_data, save_path)