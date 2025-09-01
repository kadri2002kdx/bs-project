import json, os

def create_ecosystems_data():
    data = {
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
                "geomorphology": "حوض مغلق Endoréique تابع للشطوط الشرقية، يتشكل من منخفض طبيعي في الصحراء الشمالية الشرقية",
                "soil": "تربة مالحة (Solonchaks) مع طبقات طينية ومواد عضوية متحللة",
                "hydrology": "وادي عياطة + مياه جوفية ضحلة من الطبقات المائية الضحلة في العصر الرباعي",
                "biodiversity_index": "عالٍ",
                "vegetation": [
                    {"scientific": "Salicornia arabica", "common": "قرمل", "status": "سائد"},
                    {"scientific": "Suaeda fruticosa", "common": "سويداء", "status": "سائد"},
                    {"scientific": "Atriplex halimus", "common": "قطف", "status": "متوسط"},
                    {"scientific": "Tamarix gallica", "common": "أثل", "status": "متوسط"},
                    {"scientific": "Juncus maritimus", "common": "البوص البحري", "status": "نادر"}
                ],
                "birds": [
                    {"scientific": "Phoenicopterus roseus", "common": "فلامنغو وردي", "status": "مهاجر"},
                    {"scientific": "Threskiornis aethiopicus", "common": "أبو منجل المقدس", "status": "مقيم"},
                    {"scientific": "Anas platyrhynchos", "common": "بط بري", "status": "مهاجر"},
                    {"scientific": "Himantopus himantopus", "common": "الزنَّار", "status": "مقيم"}
                ],
                "fauna": [
                    {"scientific": "Varanus griseus", "common": "ورل الصحراء", "status": "مهدد"},
                    {"scientific": "Fennecus zerda", "common": "ثعلب الصحراء", "status": "مقيم"},
                    {"scientific": "Gerbillus gerbillus", "common": "جرذ الكثبان", "status": "شائع"}
                ],
                "invertebrates": [
                    {"scientific": "Artemia salina", "common": "جمبري الملح", "status": "سائد"},
                    {"scientific": "Hemilepistus aphgianus", "common": "حشرة الرطوبة", "status": "متخصص"}
                ],
                "threats": [
                    {"name": "استغلال المياه الجوفية", "severity": "عالية", "trend": "متزايد"},
                    {"name": "التوسع الفلاحي", "severity": "متوسطة", "trend": "مستقر"},
                    {"name": "التغير المناخي", "severity": "عالية", "trend": "متزايد"},
                    {"name": "الرعي الجائر", "severity": "منخفضة", "trend": "متناقص"}
                ],
                "conservation_status": "مهدد بشكل متوسط",
                "protection_level": "غير محمي بشكل كاف",
                "recommendations": [
                    "تصنيفها كموقع رامسار",
                    "برامج مراقبة الطيور المنتظمة",
                    "إيكوتوريزم مستدام",
                    "وضع خطة إدارة متكاملة للموارد المائية"
                ],
                "research_opportunities": [
                    "دراسات التنوع البيولوجي الموسمي",
                    "مراقبة تأثير التغير المناخي",
                    "دراسات الهجرة الطيرية"
                ],
                "images": [
                    "https://example.com/aiata-lake1.jpg",
                    "https://example.com/aiata-lake2.jpg"
                ]
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
                "geomorphology": "منحدرات جبل الأطلس التلي مع تكوينات صخرية كلسية",
                "soil": "تربة بنية غابية وتربة حمراء متوسطية",
                "hydrology": "أمطار موسمية + ينابيع جبلية",
                "biodiversity_index": "عالٍ جداً",
                "vegetation": [
                    {"scientific": "Cedrus atlantica", "common": "أرز الأطلس", "status": "سائد"},
                    {"scientific": "Quercus ilex", "common": "البلوط الأخضر", "status": "مساعد"},
                    {"scientific": "Acer monspessulanum", "common": "القيقب", "status": "نادر"},
                    {"scientific": "Ilex aquifolium", "common": "البهشية", "status": "نادر"}
                ],
                "birds": [
                    {"scientific": "Gypaetus barbatus", "common": "كاسر العظام", "status": "مهدد عالمياً"},
                    {"scientific": "Aquila chrysaetos", "common": "النسر الذهبي", "status": "مقيم"},
                    {"scientific": "Dendrocopos major", "common": "نقار الخشب", "status": "شائع"}
                ],
                "fauna": [
                    {"scientific": "Macaca sylvanus", "common": "مكاك بربري", "status": "مهدد"},
                    {"scientific": "Cervus elaphus", "common": "الأيل الأحمر", "status": "مقيم"},
                    {"scientific": "Panthera pardus", "common": "فهد شمال أفريقيا", "status": "مهدد بشدة"}
                ],
                "invertebrates": [
                    {"scientific": "Rosalia alpina", "common": "خنفساء الأرز", "status": "مهدد"},
                    {"scientific": "Lucanus cervus", "common": "خنفساء الوعل", "status": "نادر"}
                ],
                "threats": [
                    {"name": "الحرائق", "severity": "عالية", "trend": "متزايد"},
                    {"name": "الرعي الجائر", "severity": "متوسطة", "trend": "مستقر"},
                    {"name": "الضغط السياحي", "severity": "متوسطة", "trend": "متزايد"}
                ],
                "conservation_status": "محمي جزئياً",
                "protection_level": "محمية طبيعية",
                "recommendations": [
                    "تعزيز مكافحة الحرائق",
                    "تنظيم السياحة البيئية",
                    "برامج إكثار الأنواع المهددة"
                ],
                "research_opportunities": [
                    "دراسات التنوع الجيني لأرز الأطلس",
                    "مراقبة المجتمعات الحيوانية الكبيرة",
                    "دراسات تأثير التغير المناخي على الغابات"
                ],
                "images": [
                    "https://example.com/chrea-cedar1.jpg",
                    "https://example.com/chrea-cedar2.jpg"
                ]
            },
            {
                "id": "eco-3",
                "name": "الشط الشرقي",
                "wilaya": "وادي سوف",
                "type": "سبخة مالحة",
                "coords": {"lat": 33.683, "lng": 6.850},
                "area": "550000 هكتار",
                "altitude": "15-30 م",
                "climate": "صحراوي حار (BWh) مع قلة الأمطار",
                "geomorphology": "منخفض شاسع في الصحراء الشرقية، أحد أكبر المسطحات الملحية في العالم",
                "soil": "تربة ملحية شديدة الملوحة (Solonchaks) مع قشور ملحية",
                "hydrology": "مياه جوفية مالحة + فيضانات موسمية نادرة",
                "biodiversity_index": "متوسط (متخصص)",
                "vegetation": [
                    {"scientific": "Halocnemum strobilaceum", "common": "شورة", "status": "سائد"},
                    {"scientific": "Arthrocnemum macrostachyum", "common": "أرطى", "status": "سائد"},
                    {"scientific": "Zygophyllum album", "common": "الرطريط", "status": "مساعد"}
                ],
                "birds": [
                    {"scientific": "Cursorius cursor", "common": "الكروان الصحراوي", "status": "مقيم"},
                    {"scientific": "Pterocles orientalis", "common": "القَطَا", "status": "مهاجر"},
                    {"scientific": "Oenanthe deserti", "common": "أبو ب沙漠", "status": "مقيم"}
                ],
                "fauna": [
                    {"scientific": "Scincus scincus", "common": "سمكة الرمال", "status": "متخصص"},
                    {"scientific": "Uromastyx acanthinura", "common": "ضب", "status": "مقيم"},
                    {"scientific": "Vulpes rueppellii", "common": "ثعلب روبل", "status": "نادر"}
                ],
                "invertebrates": [
                    {"scientific": "Adesmia antiqua", "common": "خنفساء السبخة", "status": "متخصص"},
                    {"scientific": "Sphingonotus savignyi", "common": "جراد الملح", "status": "سائد"}
                ],
                "threats": [
                    {"name": "الاستغلال المفرط للملح", "severity": "عالية", "trend": "متزايد"},
                    {"name": "التغير المناخي", "severity": "عالية", "trend": "متزايد"},
                    {"name": "الاضطراب البشري", "severity": "متوسطة", "trend": "مستقر"}
                ],
                "conservation_status": "مهدد بشكل كبير",
                "protection_level": "غير محمي",
                "recommendations": [
                    "وضع خطة استغلال مستدام للملح",
                    "إنشاء محمية طبيعية",
                    "مراقبة التغيرات البيئية"
                ],
                "research_opportunities": [
                    "دراسات التكيف مع الملوحة العالية",
                    "بحوث الجيولوجيا والهيدرولوجيا",
                    "دراسات الكائنات المتخصصة"
                ],
                "images": [
                    "https://example.com/chott-est1.jpg",
                    "https://example.com/chott-est2.jpg"
                ]
            },
            {
                "id": "eco-4",
                "name": "الحظيرة الوطنية لقورايا",
                "wilaya": "بجاية",
                "type": "نظام بيئي ساحلي-بحري",
                "coords": {"lat": 36.750, "lng": 5.100},
                "area": "2080 هكتار بري + 7842 هكتار بحري",
                "altitude": "0-500 م",
                "climate": "متوسطي رطب (Csa) مع تأثيرات بحرية",
                "geomorphology": "منحدرات ساحلية صخرية، كهوف بحرية، وشواطئ رملية",
                "soil": "تربة متوسطية حمراء وتربة ساحلية رملية",
                "hydrology": "مياه البحر الأبيض المتوسط + أنهار ساحلية صغيرة",
                "biodiversity_index": "عالٍ جداً",
                "vegetation": [
                    {"scientific": "Pinus halepensis", "common": "صنوبر حلب", "status": "سائد"},
                    {"scientific": "Juniperus phoenicea", "common": "العرعر الفينيقي", "status": "مساعد"},
                    {"scientific": "Posidonia oceanica", "common": "أعشاب بوسيدونيا البحرية", "status": "سائد تحت مائي"}
                ],
                "birds": [
                    {"scientific": "Calonectris diomedea", "common": "جلم ماء", "status": "متعشش"},
                    {"scientific": "Falco eleonorae", "common": "صقر إليونورا", "status": "مهاجر"},
                    {"scientific": "Larus audouinii", "common": "نورس أودوين", "status": "مقيم"}
                ],
                "fauna": [
                    {"scientific": "Monachus monachus", "common": "فقمة الراهب", "status": "مهدد بشدة"},
                    {"scientific": "Delphinus delphis", "common": "دلفين شائع", "status": "مقيم"},
                    {"scientific": "Caretta caretta", "common": "سلحفاة بحرية ضخمة الرأس", "status": "متعشش"}
                ],
                "invertebrates": [
                    {"scientific": "Patella ferruginea", "common": "بطيلة صدئة", "status": "مهدد"},
                    {"scientific": "Pinna nobilis", "common": "محارة نبل", "status": "مهدد"}
                ],
                "threats": [
                    {"name": "التلوث البحري", "severity": "عالية", "trend": "متزايد"},
                    {"name": "الصيد الجائر", "severity": "عالية", "trend": "مستقر"},
                    {"name": "الضغط السياحي", "severity": "متوسطة", "trend": "متزايد"}
                ],
                "conservation_status": "محمي بشكل جيد",
                "protection_level": "محمية وطنية",
                "recommendations": [
                    "تعزيز المراقبة البحرية",
                    "برامج التوعية البيئية",
                    "تنمية السياحة البيئية المستدامة"
                ],
                "research_opportunities": [
                    "دراسات التنوع البيولوجي البحري",
                    "مراقبة الثدييات البحرية",
                    "بحوث بيئة الأعشاب البحرية"
                ],
                "images": [
                    "https://example.com/gouraya1.jpg",
                    "https://example.com/gouraya2.jpg"
                ]
            },
            {
                "id": "eco-5",
                "name": "الهقار",
                "wilaya": "تمنراست",
                "type": "نظام بيئي صحراوي جبلي",
                "coords": {"lat": 23.292, "lng": 5.525},
                "area": "450000 هكتار",
                "altitude": "900-3000 م",
                "climate": "صحراوي شديد الجفاف (BWh) مع تباين حراري كبير",
                "geomorphology": "جبال بركانية، هضاب صخرية، وكثبان رملية",
                "soil": "تربة صحراوية خشنة، رمال، وصخور مكشوفة",
                "hydrology": "أمطار نادرة + وديان موسمية (أودية)",
                "biodiversity_index": "منخفض ولكن متخصص",
                "vegetation": [
                    {"scientific": "Acacia raddiana", "common": "طلح", "status": "نادر"},
                    {"scientific": "Calotropis procera", "common": "عشار", "status": "مساعد"},
                    {"scientific": "Peganum harmala", "common": "حرمل", "status": "منتشر"}
                ],
                "birds": [
                    {"scientific": "Neophron percnopterus", "common": "رخمة مصرية", "status": "مقيم"},
                    {"scientific": "Alaemon alaudipes", "common": "قبرة الصحراء", "status": "مقيم"},
                    {"scientific": "Oenanthe leucopyga", "common": "أبو ب أبيض القنة", "status": "مقيم"}
                ],
                "fauna": [
                    {"scientific": "Ammotragus lervia", "common": "كبش أروي", "status": "مهدد"},
                    {"scientific": "Gazella dorcas", "common": "غزال دوركاس", "status": "مهدد"},
                    {"scientific": "Cheetah saharicus", "common": "فهد الصحراء", "status": "مهدد بشدة"}
                ],
                "invertebrates": [
                    {"scientific": "Scorpio maurus", "common": "عقرب أصفر", "status": "شائع"},
                    {"scientific": "Androctonus australis", "common": "عقرب سميك الذيل", "status": "شائع"}
                ],
                "threats": [
                    {"name": "الرعي الجائر", "severity": "عالية", "trend": "مستقر"},
                    {"name": "الاضطراب البشري", "severity": "متوسطة", "trend": "متزايد"},
                    {"name": "التغير المناخي", "severity": "عالية", "trend": "متزايد"}
                ],
                "conservation_status": "محمي جزئياً",
                "protection_level": "محمية طبيعية وطنية",
                "recommendations": [
                    "حماية الأنواع المهددة",
                    "تنظيم السياحة الصحراوية",
                    "بحوث التكيف مع الجفاف"
                ],
                "research_opportunities": [
                    "دراسات التكيف مع الظروف القاسية",
                    "بحوث الجيولوجيا والبراكين القديمة",
                    "دراسات الفن الصخري والبيئة القديمة"
                ],
                "images": [
                    "https://example.com/hoggar1.jpg",
                    "https://example.com/hoggar2.jpg"
                ]
            },
            {
                "id": "eco-6",
                "name": "المنطقة الرطبة للطارف",
                "wilaya": "الطارف",
                "type": "منطقة رطبة ساحلية",
                "coords": {"lat": 36.767, "lng": 8.317},
                "area": "12500 هكتار",
                "altitude": "0-50 م",
                "climate": "متوسطي رطب (Csa) مع أمطار غزيرة",
                "geomorphology": "مستنقعات، بحيرات ساحلية، وكثبان رملية",
                "soil": "تربة طينية وتربة عضوية (Histosols)",
                "hydrology": "أمطار + أنهار صغيرة + مد وجزر",
                "biodiversity_index": "عالٍ جداً",
                "vegetation": [
                    {"scientific": "Phragmites australis", "common": "قصب", "status": "سائد"},
                    {"scientific": "Typha angustifolia", "common": "بطنج", "status": "سائد"},
                    {"scientific": "Nymphaea alba", "common": "زنبق الماء", "status": "نادر"}
                ],
                "birds": [
                    {"scientific": "Plegadis falcinellus", "common": "أبو معول", "status": "مهاجر"},
                    {"scientific": "Sterna hirundo", "common": "خرشنة بحرية", "status": "متعشش"},
                    {"scientific": "Ardea purpurea", "common": "مالك الحزين الأرجواني", "status": "مقيم"}
                ],
                "fauna": [
                    {"scientific": "Lutra lutra", "common": "ثعلب الماء", "status": "مهدد"},
                    {"scientific": "Emys orbicularis", "common": "سلحفاة المستنقعات", "status": "مهدد"},
                    {"scientific": "Rana saharica", "common": "ضفدع الصحراء", "status": "شائع"}
                ],
                "invertebrates": [
                    {"scientific": "Coenagrion mercuriale", "common": "يعسوب نادر", "status": "مهدد"},
                    {"scientific": "Astacus astacus", "common": "جراد البحر", "status": "منقرض محلياً"}
                ],
                "threats": [
                    {"name": "التوسع العمراني", "severity": "عالية", "trend": "متزايد"},
                    {"name": "التلوث الزراعي", "severity": "متوسطة", "trend": "مستقر"},
                    {"name": "الأنواع الدخيلة", "severity": "منخفضة", "trend": "متزايد"}
                ],
                "conservation_status": "مهدد بشكل متوسط",
                "protection_level": "موقع رامسار",
                "recommendations": [
                    "تعزيز الحماية القانونية",
                    "إنشاء مرصد بيئي",
                    "برامج التوعية للمجتمع المحلي"
                ],
                "research_opportunities": [
                    "دراسات هجرة الطيور",
                    "مراقبة جودة المياه",
                    "بحوث التنوع البيولوجي"
                ],
                "images": [
                    "https://example.com/el-tarf1.jpg",
                    "https://example.com/el-tarf2.jpg"
                ]
            },
            {
                "id": "eco-7",
                "name": "غابات البلوط الفليني",
                "wilaya": "القالة",
                "type": "غابة متوسطية",
                "coords": {"lat": 36.900, "lng": 8.450},
                "area": "18000 هكتار",
                "altitude": "200-800 م",
                "climate": "متوسطي رطب (Csa) مع صيف حار وجاف",
                "geomorphology": "هضاب وتلال منخفضة مع تكوينات صخرية رملية",
                "soil": "تربة حمراء متوسطية (Terra Rossa) وتربة بنية غابية",
                "hydrology": "أمطار موسمية + جداول موسمية",
                "biodiversity_index": "عالٍ",
                "vegetation": [
                    {"scientific": "Quercus suber", "common": "البلوط الفليني", "status": "سائد"},
                    {"scientific": "Erica arborea", "common": "الإيريكا", "status": "مساعد"},
                    {"scientific": "Cistus salviifolius", "common": "اللبادية", "status": "شائع"},
                    {"scientific": "Lavandula stoechas", "common": "الخزامى", "status": "شائع"}
                ],
                "birds": [
                    {"scientific": "Dendrocopos major", "common": "نقار الخشب", "status": "مقيم"},
                    {"scientific": "Circaetus gallicus", "common": "أفعام", "status": "مهاجر"},
                    {"scientific": "Bubo bubo", "common": "البومة النسارية", "status": "مقيم"}
                ],
                "fauna": [
                    {"scientific": "Genetta genetta", "common": "الزريقاء", "status": "مقيم"},
                    {"scientific": "Sus scrofa", "common": "خنزير بري", "status": "شائع"},
                    {"scientific": "Barbary stag", "common": "الأيل البربري", "status": "مقيم"}
                ],
                "invertebrates": [
                    {"scientific": "Lucanus cervus", "common": "خنفساء الوعل", "status": "نادر"},
                    {"scientific": "Rosalia alpina", "common": "خنفساء روزاليا", "status": "مهدد"}
                ],
                "threats": [
                    {"name": "الحرائق", "severity": "عالية", "trend": "متزايد"},
                    {"name": "استغلال الفلين", "severity": "متوسطة", "trend": "مستقر"},
                    {"name": "تغير استخدام الأراضي", "severity": "متوسطة", "trend": "متزايد"}
                ],
                "conservation_status": "محمي جزئياً",
                "protection_level": "غابة محمية",
                "recommendations": [
                    "إدارة مستدامة لاستغلال الفلين",
                    "أنظمة إنذار مبكر للحرائق",
                    "الحفاظ على التنوع الجيني للبلوط"
                ],
                "research_opportunities": [
                    "دراسات إدارة الغابات",
                    "بحوث التنوع البيولوجي",
                    "دراسات التغير المناخي وتأثيره"
                ],
                "images": [
                    "https://example.com/el-kala-cork1.jpg",
                    "https://example.com/el-kala-cork2.jpg"
                ]
            }
        ]
    }
    return data

def save_to_json(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"تم حفظ البيانات في: {file_path}")

if __name__ == "__main__":
    ecosystems_data = create_ecosystems_data()
    save_path = r"C:\Users\LAPTA\ecoplant-dz\ecosystems_data.json"
    save_to_json(ecosystems_data, save_path)
