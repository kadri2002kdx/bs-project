# قاعدة بيانات النباتات (60 نباتًا شائعًا في الجزائر)
plants_data = [
    {
        "id": 1,
        "name": "قمح صلب",
        "optimal_temp_min": 15,
        "optimal_temp_max": 25,
        "water_needs_min": 400,
        "water_needs_max": 700,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 160,
        "phosphorus_needs": 80,
        "potassium_needs": 110,
        "base_yield": 3.8,
        "price_per_ton": 38000
    },
    {
        "id": 2,
        "name": "شعير",
        "optimal_temp_min": 10,
        "optimal_temp_max": 25,
        "water_needs_min": 300,
        "water_needs_max": 600,
        "suitable_soil_types": [1, 2, 3],
        "nitrogen_needs": 130,
        "phosphorus_needs": 65,
        "potassium_needs": 90,
        "base_yield": 3.2,
        "price_per_ton": 32000
    },
    {
        "id": 3,
        "name": "ذرة صفراء",
        "optimal_temp_min": 20,
        "optimal_temp_max": 30,
        "water_needs_min": 500,
        "water_needs_max": 800,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 200,
        "phosphorus_needs": 90,
        "potassium_needs": 130,
        "base_yield": 6.5,
        "price_per_ton": 42000
    },
    {
        "id": 4,
        "name": "طماطم",
        "optimal_temp_min": 18,
        "optimal_temp_max": 28,
        "water_needs_min": 600,
        "water_needs_max": 900,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 220,
        "phosphorus_needs": 110,
        "potassium_needs": 270,
        "base_yield": 45.0,
        "price_per_ton": 8500
    },
    {
        "id": 5,
        "name": "بطاطس",
        "optimal_temp_min": 15,
        "optimal_temp_max": 25,
        "water_needs_min": 500,
        "water_needs_max": 750,
        "suitable_soil_types": [1, 2, 3],
        "nitrogen_needs": 270,
        "phosphorus_needs": 130,
        "potassium_needs": 380,
        "base_yield": 35.0,
        "price_per_ton": 6500
    },
    {
        "id": 6,
        "name": "زيتون",
        "optimal_temp_min": 15,
        "optimal_temp_max": 30,
        "water_needs_min": 400,
        "water_needs_max": 700,
        "suitable_soil_types": [2, 3],
        "nitrogen_needs": 150,
        "phosphorus_needs": 70,
        "potassium_needs": 200,
        "base_yield": 5.0,
        "price_per_ton": 120000
    },
    {
        "id": 7,
        "name": "تمر",
        "optimal_temp_min": 22,
        "optimal_temp_max": 35,
        "water_needs_min": 300,
        "water_needs_max": 600,
        "suitable_soil_types": [2],
        "nitrogen_needs": 120,
        "phosphorus_needs": 60,
        "potassium_needs": 180,
        "base_yield": 8.0,
        "price_per_ton": 150000
    },
    {
        "id": 8,
        "name": "عنب",
        "optimal_temp_min": 15,
        "optimal_temp_max": 30,
        "water_needs_min": 500,
        "water_needs_max": 800,
        "suitable_soil_types": [2, 3],
        "nitrogen_needs": 140,
        "phosphorus_needs": 80,
        "potassium_needs": 220,
        "base_yield": 15.0,
        "price_per_ton": 30000
    },
    {
        "id": 9,
        "name": "برتقال",
        "optimal_temp_min": 15,
        "optimal_temp_max": 28,
        "water_needs_min": 600,
        "water_needs_max": 900,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 180,
        "phosphorus_needs": 90,
        "potassium_needs": 250,
        "base_yield": 25.0,
        "price_per_ton": 35000
    },
    {
        "id": 10,
        "name": "فلفل",
        "optimal_temp_min": 20,
        "optimal_temp_max": 30,
        "water_needs_min": 500,
        "water_needs_max": 700,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 200,
        "phosphorus_needs": 100,
        "potassium_needs": 280,
        "base_yield": 20.0,
        "price_per_ton": 25000
    },
    {
        "id": 11,
        "name": "بازلاء",
        "optimal_temp_min": 10,
        "optimal_temp_max": 22,
        "water_needs_min": 350,
        "water_needs_max": 550,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 40,
        "phosphorus_needs": 70,
        "potassium_needs": 90,
        "base_yield": 8.0,
        "price_per_ton": 45000
    },
    {
        "id": 12,
        "name": "جزر",
        "optimal_temp_min": 12,
        "optimal_temp_max": 24,
        "water_needs_min": 450,
        "water_needs_max": 700,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 110,
        "phosphorus_needs": 60,
        "potassium_needs": 190,
        "base_yield": 40.0,
        "price_per_ton": 12000
    },
    {
        "id": 13,
        "name": "بصل",
        "optimal_temp_min": 13,
        "optimal_temp_max": 26,
        "water_needs_min": 350,
        "water_needs_max": 550,
        "suitable_soil_types": [1, 2, 3],
        "nitrogen_needs": 130,
        "phosphorus_needs": 55,
        "potassium_needs": 150,
        "base_yield": 30.0,
        "price_per_ton": 15000
    },
    {
        "id": 14,
        "name": "ثوم",
        "optimal_temp_min": 12,
        "optimal_temp_max": 25,
        "water_needs_min": 300,
        "water_needs_max": 500,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 150,
        "phosphorus_needs": 70,
        "potassium_needs": 140,
        "base_yield": 12.0,
        "price_per_ton": 40000
    },
    {
        "id": 15,
        "name": "خيار",
        "optimal_temp_min": 20,
        "optimal_temp_max": 30,
        "water_needs_min": 550,
        "water_needs_max": 850,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 180,
        "phosphorus_needs": 95,
        "potassium_needs": 230,
        "base_yield": 35.0,
        "price_per_ton": 10000
    },
    {
        "id": 16,
        "name": "قرع",
        "optimal_temp_min": 18,
        "optimal_temp_max": 28,
        "water_needs_min": 500,
        "water_needs_max": 750,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 160,
        "phosphorus_needs": 85,
        "potassium_needs": 210,
        "base_yield": 30.0,
        "price_per_ton": 11000
    },
    {
        "id": 17,
        "name": "باذنجان",
        "optimal_temp_min": 22,
        "optimal_temp_max": 32,
        "water_needs_min": 600,
        "water_needs_max": 900,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 190,
        "phosphorus_needs": 100,
        "potassium_needs": 260,
        "base_yield": 25.0,
        "price_per_ton": 13000
    },
    {
        "id": 18,
        "name": "فاصوليا خضراء",
        "optimal_temp_min": 18,
        "optimal_temp_max": 26,
        "water_needs_min": 400,
        "water_needs_max": 600,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 50,
        "phosphorus_needs": 65,
        "potassium_needs": 100,
        "base_yield": 15.0,
        "price_per_ton": 28000
    },
    {
        "id": 19,
        "name": "لفت",
        "optimal_temp_min": 10,
        "optimal_temp_max": 20,
        "water_needs_min": 350,
        "water_needs_max": 550,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 120,
        "phosphorus_needs": 50,
        "potassium_needs": 160,
        "base_yield": 35.0,
        "price_per_ton": 9000
    },
    {
        "id": 20,
        "name": "سبانخ",
        "optimal_temp_min": 8,
        "optimal_temp_max": 22,
        "water_needs_min": 400,
        "water_needs_max": 650,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 170,
        "phosphorus_needs": 55,
        "potassium_needs": 140,
        "base_yield": 18.0,
        "price_per_ton": 22000
    },
    {
        "id": 21,
        "name": "خس",
        "optimal_temp_min": 10,
        "optimal_temp_max": 20,
        "water_needs_min": 350,
        "water_needs_max": 600,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 140,
        "phosphorus_needs": 45,
        "potassium_needs": 170,
        "base_yield": 22.0,
        "price_per_ton": 18000
    },
    {
        "id": 22,
        "name": "شمار",
        "optimal_temp_min": 12,
        "optimal_temp_max": 22,
        "water_needs_min": 450,
        "water_needs_max": 700,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 130,
        "phosphorus_needs": 60,
        "potassium_needs": 200,
        "base_yield": 28.0,
        "price_per_ton": 20000
    },
    {
        "id": 23,
        "name": "كرنب",
        "optimal_temp_min": 8,
        "optimal_temp_max": 20,
        "water_needs_min": 400,
        "water_needs_max": 650,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 190,
        "phosphorus_needs": 70,
        "potassium_needs": 180,
        "base_yield": 40.0,
        "price_per_ton": 10000
    },
    {
        "id": 24,
        "name": "قرنبيط",
        "optimal_temp_min": 12,
        "optimal_temp_max": 22,
        "water_needs_min": 450,
        "water_needs_max": 700,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 180,
        "phosphorus_needs": 80,
        "potassium_needs": 190,
        "base_yield": 20.0,
        "price_per_ton": 15000
    },
    {
        "id": 25,
        "name": "فجل",
        "optimal_temp_min": 10,
        "optimal_temp_max": 20,
        "water_needs_min": 300,
        "water_needs_max": 500,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 100,
        "phosphorus_needs": 40,
        "potassium_needs": 120,
        "base_yield": 15.0,
        "price_per_ton": 17000
    },
    {
        "id": 26,
        "name": "بقدونس",
        "optimal_temp_min": 12,
        "optimal_temp_max": 22,
        "water_needs_min": 350,
        "water_needs_max": 550,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 150,
        "phosphorus_needs": 50,
        "potassium_needs": 160,
        "base_yield": 10.0,
        "price_per_ton": 50000
    },
    {
        "id": 27,
        "name": "نعناع",
        "optimal_temp_min": 15,
        "optimal_temp_max": 25,
        "water_needs_min": 500,
        "water_needs_max": 750,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 160,
        "phosphorus_needs": 60,
        "potassium_needs": 170,
        "base_yield": 12.0,
        "price_per_ton": 60000
    },
    {
        "id": 28,
        "name": "شمام",
        "optimal_temp_min": 20,
        "optimal_temp_max": 32,
        "water_needs_min": 600,
        "water_needs_max": 900,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 140,
        "phosphorus_needs": 70,
        "potassium_needs": 210,
        "base_yield": 25.0,
        "price_per_ton": 22000
    },
    {
        "id": 29,
        "name": "بطيخ",
        "optimal_temp_min": 22,
        "optimal_temp_max": 32,
        "water_needs_min": 550,
        "water_needs_max": 850,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 130,
        "phosphorus_needs": 65,
        "potassium_needs": 200,
        "base_yield": 30.0,
        "price_per_ton": 18000
    },
    {
        "id": 30,
        "name": "تين",
        "optimal_temp_min": 15,
        "optimal_temp_max": 30,
        "water_needs_min": 400,
        "water_needs_max": 650,
        "suitable_soil_types": [2, 3],
        "nitrogen_needs": 100,
        "phosphorus_needs": 50,
        "potassium_needs": 150,
        "base_yield": 10.0,
        "price_per_ton": 70000
    },
    {
        "id": 31,
        "name": "رمان",
        "optimal_temp_min": 18,
        "optimal_temp_max": 28,
        "water_needs_min": 500,
        "water_needs_max": 800,
        "suitable_soil_types": [2, 3],
        "nitrogen_needs": 120,
        "phosphorus_needs": 60,
        "potassium_needs": 170,
        "base_yield": 15.0,
        "price_per_ton": 60000
    },
    {
        "id": 32,
        "name": "مشمش",
        "optimal_temp_min": 12,
        "optimal_temp_max": 25,
        "water_needs_min": 450,
        "water_needs_max": 700,
        "suitable_soil_types": [1, 2, 3],
        "nitrogen_needs": 110,
        "phosphorus_needs": 55,
        "potassium_needs": 160,
        "base_yield": 18.0,
        "price_per_ton": 50000
    },
    {
        "id": 33,
        "name": "خوخ",
        "optimal_temp_min": 12,
        "optimal_temp_max": 25,
        "water_needs_min": 500,
        "water_needs_max": 750,
        "suitable_soil_types": [1, 2, 3],
        "nitrogen_needs": 130,
        "phosphorus_needs": 65,
        "potassium_needs": 180,
        "base_yield": 20.0,
        "price_per_ton": 45000
    },
    {
        "id": 34,
        "name": "دراق",
        "optimal_temp_min": 15,
        "optimal_temp_max": 26,
        "water_needs_min": 550,
        "water_needs_max": 800,
        "suitable_soil_types": [1, 2, 3],
        "nitrogen_needs": 140,
        "phosphorus_needs": 70,
        "potassium_needs": 190,
        "base_yield": 22.0,
        "price_per_ton": 40000
    },
    {
        "id": 35,
        "name": "تفاح",
        "optimal_temp_min": 10,
        "optimal_temp_max": 22,
        "water_needs_min": 600,
        "water_needs_max": 900,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 160,
        "phosphorus_needs": 75,
        "potassium_needs": 210,
        "base_yield": 30.0,
        "price_per_ton": 38000
    },
    {
        "id": 36,
        "name": "كمثرى",
        "optimal_temp_min": 10,
        "optimal_temp_max": 22,
        "water_needs_min": 550,
        "water_needs_max": 850,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 150,
        "phosphorus_needs": 70,
        "potassium_needs": 200,
        "base_yield": 28.0,
        "price_per_ton": 35000
    },
    {
        "id": 37,
        "name": "ليمون",
        "optimal_temp_min": 15,
        "optimal_temp_max": 28,
        "water_needs_min": 600,
        "water_needs_max": 950,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 170,
        "phosphorus_needs": 85,
        "potassium_needs": 230,
        "base_yield": 22.0,
        "price_per_ton": 42000
    },
    {
        "id": 38,
        "name": "يوسفي",
        "optimal_temp_min": 15,
        "optimal_temp_max": 28,
        "water_needs_min": 580,
        "water_needs_max": 900,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 165,
        "phosphorus_needs": 80,
        "potassium_needs": 220,
        "base_yield": 24.0,
        "price_per_ton": 40000
    },
    {
        "id": 39,
        "name": "فول",
        "optimal_temp_min": 10,
        "optimal_temp_max": 22,
        "water_needs_min": 400,
        "water_needs_max": 600,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 30,
        "phosphorus_needs": 60,
        "potassium_needs": 90,
        "base_yield": 4.0,
        "price_per_ton": 50000
    },
    {
        "id": 40,
        "name": "عدس",
        "optimal_temp_min": 12,
        "optimal_temp_max": 24,
        "water_needs_min": 350,
        "water_needs_max": 550,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 25,
        "phosphorus_needs": 50,
        "potassium_needs": 70,
        "base_yield": 2.0,
        "price_per_ton": 80000
    },
    {
        "id": 41,
        "name": "حمص",
        "optimal_temp_min": 15,
        "optimal_temp_max": 26,
        "water_needs_min": 300,
        "water_needs_max": 500,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 20,
        "phosphorus_needs": 55,
        "potassium_needs": 75,
        "base_yield": 2.5,
        "price_per_ton": 75000
    },
    {
        "id": 42,
        "name": "ذرة بيضاء",
        "optimal_temp_min": 20,
        "optimal_temp_max": 30,
        "water_needs_min": 450,
        "water_needs_max": 700,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 120,
        "phosphorus_needs": 60,
        "potassium_needs": 100,
        "base_yield": 4.5,
        "price_per_ton": 35000
    },
    {
        "id": 43,
        "name": "عنب الثعلب",
        "optimal_temp_min": 12,
        "optimal_temp_max": 22,
        "water_needs_min": 500,
        "water_needs_max": 750,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 110,
        "phosphorus_needs": 55,
        "potassium_needs": 150,
        "base_yield": 12.0,
        "price_per_ton": 32000
    },
    {
        "id": 44,
        "name": "كرز",
        "optimal_temp_min": 10,
        "optimal_temp_max": 20,
        "water_needs_min": 550,
        "water_needs_max": 800,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 150,
        "phosphorus_needs": 65,
        "potassium_needs": 180,
        "base_yield": 12.0,
        "price_per_ton": 90000
    },
    {
        "id": 45,
        "name": "لوز",
        "optimal_temp_min": 12,
        "optimal_temp_max": 25,
        "water_needs_min": 400,
        "water_needs_max": 650,
        "suitable_soil_types": [2, 3],
        "nitrogen_needs": 100,
        "phosphorus_needs": 50,
        "potassium_needs": 130,
        "base_yield": 2.5,
        "price_per_ton": 180000
    },
    {
        "id": 46,
        "name": "جوز",
        "optimal_temp_min": 10,
        "optimal_temp_max": 22,
        "water_needs_min": 600,
        "water_needs_max": 900,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 130,
        "phosphorus_needs": 60,
        "potassium_needs": 170,
        "base_yield": 3.0,
        "price_per_ton": 150000
    },
    {
        "id": 47,
        "name": "زعتر",
        "optimal_temp_min": 15,
        "optimal_temp_max": 26,
        "water_needs_min": 300,
        "water_needs_max": 500,
        "suitable_soil_types": [2, 3],
        "nitrogen_needs": 90,
        "phosphorus_needs": 40,
        "potassium_needs": 110,
        "base_yield": 3.0,
        "price_per_ton": 120000
    },
    {
        "id": 48,
        "name": "حلبة",
        "optimal_temp_min": 10,
        "optimal_temp_max": 22,
        "water_needs_min": 350,
        "water_needs_max": 550,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 30,
        "phosphorus_needs": 45,
        "potassium_needs": 60,
        "base_yield": 2.5,
        "price_per_ton": 95000
    },
    {
        "id": 49,
        "name": "كراوية",
        "optimal_temp_min": 12,
        "optimal_temp_max": 22,
        "water_needs_min": 400,
        "water_needs_max": 600,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 80,
        "phosphorus_needs": 40,
        "potassium_needs": 100,
        "base_yield": 2.0,
        "price_per_ton": 110000
    },
    {
        "id": 50,
        "name": "كزبرة",
        "optimal_temp_min": 12,
        "optimal_temp_max": 22,
        "water_needs_min": 350,
        "water_needs_max": 550,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 70,
        "phosphorus_needs": 35,
        "potassium_needs": 90,
        "base_yield": 3.5,
        "price_per_ton": 100000
    },
    {
        "id": 51,
        "name": "بنجر",
        "optimal_temp_min": 12,
        "optimal_temp_max": 22,
        "water_needs_min": 450,
        "water_needs_max": 700,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 120,
        "phosphorus_needs": 55,
        "potassium_needs": 170,
        "base_yield": 50.0,
        "price_per_ton": 8000
    },
    {
        "id": 52,
        "name": "كرات",
        "optimal_temp_min": 12,
        "optimal_temp_max": 22,
        "water_needs_min": 400,
        "water_needs_max": 600,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 140,
        "phosphorus_needs": 60,
        "potassium_needs": 160,
        "base_yield": 25.0,
        "price_per_ton": 14000
    },
    {
        "id": 53,
        "name": "كوسا",
        "optimal_temp_min": 20,
        "optimal_temp_max": 30,
        "water_needs_min": 500,
        "water_needs_max": 750,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 170,
        "phosphorus_needs": 90,
        "potassium_needs": 220,
        "base_yield": 35.0,
        "price_per_ton": 9000
    },
    {
        "id": 54,
        "name": "فاصوليا جافة",
        "optimal_temp_min": 18,
        "optimal_temp_max": 26,
        "water_needs_min": 400,
        "water_needs_max": 600,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 25,
        "phosphorus_needs": 60,
        "potassium_needs": 95,
        "base_yield": 3.0,
        "price_per_ton": 70000
    },
    {
        "id": 55,
        "name": "بامية",
        "optimal_temp_min": 22,
        "optimal_temp_max": 32,
        "water_needs_min": 550,
        "water_needs_max": 800,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 180,
        "phosphorus_needs": 95,
        "potassium_needs": 240,
        "base_yield": 15.0,
        "price_per_ton": 28000
    },
    {
        "id": 56,
        "name": "ريحان",
        "optimal_temp_min": 18,
        "optimal_temp_max": 26,
        "water_needs_min": 400,
        "water_needs_max": 600,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 110,
        "phosphorus_needs": 50,
        "potassium_needs": 130,
        "base_yield": 8.0,
        "price_per_ton": 85000
    },
    {
        "id": 57,
        "name": "شمر",
        "optimal_temp_min": 12,
        "optimal_temp_max": 22,
        "water_needs_min": 450,
        "water_needs_max": 700,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 100,
        "phosphorus_needs": 45,
        "potassium_needs": 140,
        "base_yield": 10.0,
        "price_per_ton": 45000
    },
    {
        "id": 58,
        "name": "خرشوف",
        "optimal_temp_min": 12,
        "optimal_temp_max": 22,
        "water_needs_min": 500,
        "water_needs_max": 750,
        "suitable_soil_types": [1, 2],
        "nitrogen_needs": 150,
        "phosphorus_needs": 70,
        "potassium_needs": 190,
        "base_yield": 12.0,
        "price_per_ton": 30000
    },
    {
        "id": 59,
        "name": "بطاطا حلوة",
        "optimal_temp_min": 20,
        "optimal_temp_max": 30,
        "water_needs_min": 550,
        "water_needs_max": 850,
        "suitable_soil_types": [1, 3],
        "nitrogen_needs": 130,
        "phosphorus_needs": 65,
        "potassium_needs": 200,
        "base_yield": 25.0,
        "price_per_ton": 20000
    },
    {
        "id": 60,
        "name": "فستق",
        "optimal_temp_min": 15,
        "optimal_temp_max": 28,
        "water_needs_min": 350,
        "water_needs_max": 600,
        "suitable_soil_types": [2, 3],
        "nitrogen_needs": 110,
        "phosphorus_needs": 55,
        "potassium_needs": 140,
        "base_yield": 2.0,
        "price_per_ton": 200000
    }
]

wilayas_data = [
    {"id": 1, "name": "أدرار", "avg_temp": 28.5, "avg_rainfall": 45, "region": "الصحراء", "soil_types": [2], "altitude": 280},
    {"id": 2, "name": "الشلف", "avg_temp": 18.2, "avg_rainfall": 380, "region": "الغرب", "soil_types": [1, 3], "altitude": 114},
    {"id": 3, "name": "الأغواط", "avg_temp": 20.1, "avg_rainfall": 180, "region": "الهضاب العليا", "soil_types": [2, 3], "altitude": 750},
    {"id": 4, "name": "أم البواقي", "avg_temp": 15.5, "avg_rainfall": 320, "region": "الشرق", "soil_types": [1, 3], "altitude": 890},
    {"id": 5, "name": "باتنة", "avg_temp": 14.8, "avg_rainfall": 350, "region": "الأوراس", "soil_types": [1, 2], "altitude": 1050},
    {"id": 6, "name": "بجاية", "avg_temp": 17.3, "avg_rainfall": 820, "region": "الشمال", "soil_types": [1, 3], "altitude": 30},
    {"id": 7, "name": "بسكرة", "avg_temp": 22.4, "avg_rainfall": 130, "region": "الصحراء", "soil_types": [2, 3], "altitude": 120},
    {"id": 8, "name": "بشار", "avg_temp": 26.8, "avg_rainfall": 70, "region": "الصحراء", "soil_types": [2], "altitude": 450},
    {"id": 9, "name": "البليدة", "avg_temp": 17.5, "avg_rainfall": 520, "region": "الشمال", "soil_types": [1, 3], "altitude": 260},
    {"id": 10, "name": "البويرة", "avg_temp": 15.7, "avg_rainfall": 450, "region": "الشمال", "soil_types": [1, 2], "altitude": 510},
    {"id": 11, "name": "تمنراست", "avg_temp": 30.2, "avg_rainfall": 35, "region": "الصحراء", "soil_types": [2], "altitude": 1400},
    {"id": 12, "name": "تبسة", "avg_temp": 16.3, "avg_rainfall": 280, "region": "الشرق", "soil_types": [1, 2], "altitude": 960},
    {"id": 13, "name": "تلمسان", "avg_temp": 16.8, "avg_rainfall": 410, "region": "الغرب", "soil_types": [1, 3], "altitude": 800},
    {"id": 14, "name": "تيارت", "avg_temp": 16.0, "avg_rainfall": 310, "region": "الهضاب العليا", "soil_types": [1, 3], "altitude": 1000},
    {"id": 15, "name": "تيزي وزو", "avg_temp": 16.2, "avg_rainfall": 650, "region": "الشمال", "soil_types": [1, 3], "altitude": 200},
    {"id": 16, "name": "الجزائر العاصمة", "avg_temp": 18.5, "avg_rainfall": 600, "region": "الشمال", "soil_types": [1, 3], "altitude": 10},
    {"id": 17, "name": "الجلفة", "avg_temp": 17.2, "avg_rainfall": 250, "region": "الهضاب العليa", "soil_types": [2, 3], "altitude": 1100},
    {"id": 18, "name": "جيجل", "avg_temp": 17.6, "avg_rainfall": 780, "region": "الشمال", "soil_types": [1, 3], "altitude": 10},
    {"id": 19, "name": "سطيف", "avg_temp": 14.2, "avg_rainfall": 420, "region": "الهضاب العليا", "soil_types": [1, 3], "altitude": 1100},
    {"id": 20, "name": "سعيدة", "avg_temp": 15.9, "avg_rainfall": 340, "region": "الغرب", "soil_types": [1, 3], "altitude": 850},
    {"id": 21, "name": "سكيكدة", "avg_temp": 18.0, "avg_rainfall": 580, "region": "الشرق", "soil_types": [1, 3], "altitude": 25},
    {"id": 22, "name": "سيدي بلعباس", "avg_temp": 17.4, "avg_rainfall": 360, "region": "الغرب", "soil_types": [1, 3], "altitude": 470},
    {"id": 23, "name": "عنابة", "avg_temp": 18.7, "avg_rainfall": 620, "region": "الشرق", "soil_types": [1, 3], "altitude": 3},
    {"id": 24, "name": "قالمة", "avg_temp": 16.5, "avg_rainfall": 480, "region": "الشرق", "soil_types": [1, 3], "altitude": 250},
    {"id": 25, "name": "قسنطينة", "avg_temp": 15.8, "avg_rainfall": 480, "region": "الشرق", "soil_types": [1, 3], "altitude": 650},
    {"id": 26, "name": "المدية", "avg_temp": 16.1, "avg_rainfall": 440, "region": "الشمال", "soil_types": [1, 3], "altitude": 920},
    {"id": 27, "name": "مستغانم", "avg_temp": 18.3, "avg_rainfall": 400, "region": "الغرب", "soil_types": [1, 3], "altitude": 80},
    {"id": 28, "name": "المسيلة", "avg_temp": 17.8, "avg_rainfall": 270, "region": "الهضاب العليا", "soil_types": [2, 3], "altitude": 470},
    {"id": 29, "name": "معسكر", "avg_temp": 17.6, "avg_rainfall": 370, "region": "الغرب", "soil_types": [1, 3], "altitude": 580},
    {"id": 30, "name": "ورقلة", "avg_temp": 27.5, "avg_rainfall": 50, "region": "الصحراء", "soil_types": [2], "altitude": 150},
    {"id": 31, "name": "وهران", "avg_temp": 18.2, "avg_rainfall": 380, "region": "الغرب", "soil_types": [1, 3], "altitude": 100},
    {"id": 32, "name": "البيض", "avg_temp": 19.5, "avg_rainfall": 180, "region": "الهضاب العليا", "soil_types": [2, 3], "altitude": 1300},
    {"id": 33, "name": "إيليزي", "avg_temp": 29.3, "avg_rainfall": 40, "region": "الصحراء", "soil_types": [2], "altitude": 420},
    {"id": 34, "name": "برج بوعريريج", "avg_temp": 15.9, "avg_rainfall": 400, "region": "الهضاب العليا", "soil_types": [1, 3], "altitude": 920},
    {"id": 35, "name": "بومرداس", "avg_temp": 18.0, "avg_rainfall": 620, "region": "الشمال", "soil_types": [1, 3], "altitude": 30},
    {"id": 36, "name": "الطارف", "avg_temp": 17.9, "avg_rainfall": 640, "region": "الشرق", "soil_types": [1, 3], "altitude": 20},
    {"id": 37, "name": "تندوف", "avg_temp": 31.5, "avg_rainfall": 30, "region": "الصحراء", "soil_types": [2], "altitude": 400},
    {"id": 38, "name": "تيسمسيلت", "avg_temp": 16.3, "avg_rainfall": 350, "region": "الهضاب العليا", "soil_types": [1, 3], "altitude": 850},
    {"id": 39, "name": "الوادي", "avg_temp": 25.8, "avg_rainfall": 60, "region": "الصحراء", "soil_types": [2], "altitude": 80},
    {"id": 40, "name": "خنشلة", "avg_temp": 15.2, "avg_rainfall": 300, "region": "الأوراس", "soil_types": [1, 2], "altitude": 1200},
    {"id": 41, "name": "سوق أهراس", "avg_temp": 16.0, "avg_rainfall": 420, "region": "الشرق", "soil_types": [1, 3], "altitude": 700},
    {"id": 42, "name": "تيبازة", "avg_temp": 17.8, "avg_rainfall": 580, "region": "الشمال", "soil_types": [1, 3], "altitude": 50},
    {"id": 43, "name": "ميلة", "avg_temp": 16.4, "avg_rainfall": 460, "region": "الشرق", "soil_types": [1, 3], "altitude": 470},
    {"id": 44, "name": "عين الدفلى", "avg_temp": 16.7, "avg_rainfall": 420, "region": "الشمال", "soil_types": [1, 3], "altitude": 950},
    {"id": 45, "name": "النعامة", "avg_temp": 20.5, "avg_rainfall": 120, "region": "الهضاب العليا", "soil_types": [2], "altitude": 1100},
    {"id": 46, "name": "عين تموشنت", "avg_temp": 18.5, "avg_rainfall": 390, "region": "الغرب", "soil_types": [1, 3], "altitude": 250},
    {"id": 47, "name": "غرداية", "avg_temp": 24.6, "avg_rainfall": 70, "region": "الصحراء", "soil_types": [2], "altitude": 520},
    {"id": 48, "name": "غليزان", "avg_temp": 17.9, "avg_rainfall": 350, "region": "الغرب", "soil_types": [1, 3], "altitude": 110},
    {"id": 49, "name": "تيميمون", "avg_temp": 27.2, "avg_rainfall": 45, "region": "الصحراء", "soil_types": [2], "altitude": 290},
    {"id": 50, "name": "برج البحري", "avg_temp": 17.8, "avg_rainfall": 550, "region": "الشمال", "soil_types": [1, 3], "altitude": 10},
    {"id": 51, "name": "عين صالح", "avg_temp": 29.7, "avg_rainfall": 35, "region": "الصحراء", "soil_types": [2], "altitude": 280},
    {"id": 52, "name": "جانت", "avg_temp": 30.8, "avg_rainfall": 25, "region": "الصحراء", "soil_types": [2], "altitude": 1050},
    {"id": 53, "name": "المغير", "avg_temp": 26.3, "avg_rainfall": 55, "region": "الصحراء", "soil_types": [2], "altitude": 60},
    {"id": 54, "name": "المسيلة", "avg_temp": 17.8, "avg_rainfall": 270, "region": "الهضاب العليا", "soil_types": [2, 3], "altitude": 470},
    {"id": 55, "name": "برج باجي مختار", "avg_temp": 32.0, "avg_rainfall": 20, "region": "الصحراء", "soil_types": [2], "altitude": 400},
    {"id": 56, "name": "أولاد جلال", "avg_temp": 21.5, "avg_rainfall": 90, "region": "الهضاب العليا", "soil_types": [2], "altitude": 350},
    {"id": 57, "name": "بني عباس", "avg_temp": 28.5, "avg_rainfall": 40, "region": "الصحراء", "soil_types": [2], "altitude": 500},
    {"id": 58, "name": "عين قزام", "avg_temp": 31.2, "avg_rainfall": 15, "region": "الصحراء", "soil_types": [2], "altitude": 380}
]

# قاعدة بيانات أنواع التربة
soil_types_data = [
    {
        "id": 1,
        "name": "طينية",
        "texture": "طينية",
        "drainage": "منخفض",
        "fertility": "عالية",
        "ph": 7.2,
        "organic_matter": 3.5,  # %
        "water_holding_capacity": 0.45,  # cm³/cm³
        "bulk_density": 1.1,  # g/cm³
        "cation_exchange_capacity": 25  # meq/100g
    },
    {
        "id": 2,
        "name": "رملية",
        "texture": "رملية",
        "drainage": "عالي",
        "fertility": "منخفضة",
        "ph": 6.5,
        "organic_matter": 1.2,
        "water_holding_capacity": 0.15,
        "bulk_density": 1.6,
        "cation_exchange_capacity": 8
    },
    {
        "id": 3,
        "name": "طميية",
        "texture": "متوسطة",
        "drainage": "جيد",
        "fertility": "عالية",
        "ph": 6.8,
        "organic_matter": 2.8,
        "water_holding_capacity": 0.35,
        "bulk_density": 1.3,
        "cation_exchange_capacity": 18
    },
    {
        "id": 4,
        "name": "جيرية",
        "texture": "خشنة",
        "drainage": "عالي جداً",
        "fertility": "منخفضة",
        "ph": 8.2,
        "organic_matter": 0.8,
        "water_holding_capacity": 0.12,
        "bulk_density": 1.7,
        "cation_exchange_capacity": 6
    },
    {
        "id": 5,
        "name": "سبخة",
        "texture": "متماسكة",
        "drainage": "منخفض جداً",
        "fertility": "منخفضة جداً",
        "ph": 8.5,
        "organic_matter": 0.5,
        "water_holding_capacity": 0.18,
        "bulk_density": 1.65,
        "cation_exchange_capacity": 9
    },
    # الأنواع المضافة حديثًا
    {
        "id": 6,
        "name": "طميية رملية",
        "texture": "متوسطة إلى خشنة",
        "drainage": "جيد إلى عالي",
        "fertility": "متوسطة",
        "ph": 6.9,
        "organic_matter": 1.8,
        "water_holding_capacity": 0.25,
        "bulk_density": 1.5,
        "cation_exchange_capacity": 12
    },
    {
        "id": 7,
        "name": "طينية رملية",
        "texture": "متوسطة",
        "drainage": "متوسط",
        "fertility": "متوسطة إلى عالية",
        "ph": 7.0,
        "organic_matter": 2.5,
        "water_holding_capacity": 0.30,
        "bulk_density": 1.4,
        "cation_exchange_capacity": 16
    },
    {
        "id": 8,
        "name": "جفتية (عضوية)",
        "texture": "إسفنجية/عضوية",
        "drainage": "منخفض إلى متوسط",
        "fertility": "عالية جداً (لكنها حامضية)",
        "ph": 5.2,
        "organic_matter": 35.0,  # نسبة عالية جدًا
        "water_holding_capacity": 0.60,  # أعلى قدرة على الاحتفاظ بالماء
        "bulk_density": 0.2,  # كثافة ظاهرية منخفضة جدًا
        "cation_exchange_capacity": 35  # عالي جدًا
    },
    {
        "id": 9,
        "name": "طباشيرية",
        "texture": "خشنة",
        "drainage": "عالي",
        "fertility": "منخفضة",
        "ph": 8.0,
        "organic_matter": 1.0,
        "water_holding_capacity": 0.20,
        "bulk_density": 1.55,
        "cation_exchange_capacity": 10
    },
    {
        "id": 10,
        "name": "غرينية",
        "texture": "ناعمة",
        "drainage": "متوسط إلى منخفض",
        "fertility": "عالية جداً",
        "ph": 7.0,
        "organic_matter": 3.2,
        "water_holding_capacity": 0.40,
        "bulk_density": 1.25,
        "cation_exchange_capacity": 22
    },
    {
        "id": 11,
        "name": "حصوية",
        "texture": "خشنة جدًا",
        "drainage": "عالي جداً",
        "fertility": "منخفضة جداً",
        "ph": 6.8,
        "organic_matter": 0.6,
        "water_holding_capacity": 0.10,
        "bulk_density": 1.8,
        "cation_exchange_capacity": 4
    }
]

# قاعدة بيانات أنظمة الري
water_systems_data = [
    {
        "id": 1,
        "name": "ري بالتنقيط",
        "efficiency": 0.95,
        "cost_per_cubic_meter": 15,
        "energy_consumption": 0.5,
        "installation_cost": 12000,
        "maintenance_cost": 800,
        "lifespan": 10,
        "suitable_soil_types": [1, 3, 4],  # رملية، طينية، طميية
        "suitable_crops": [1, 3, 4, 5, 9, 10]  # خضروات، أشجار فاكهة، عنب، توت، نباتات زينة، محاصيل صفية
    },
    {
        "id": 2,
        "name": "ري بالرش",
        "efficiency": 0.75,
        "cost_per_cubic_meter": 8,
        "energy_consumption": 1.2,
        "installation_cost": 8000,
        "maintenance_cost": 600,
        "lifespan": 8,
        "suitable_soil_types": [2, 3, 6],  # طينية خفيفة، طميية، طفيلية
        "suitable_crops": [2, 6, 7, 8]  # قمح، برسيم، نباتات علفية، مراعي
    },
    {
        "id": 3,
        "name": "ري بالغمر",
        "efficiency": 0.60,
        "cost_per_cubic_meter": 5,
        "energy_consumption": 0.3,
        "installation_cost": 3000,
        "maintenance_cost": 400,
        "lifespan": 15,
        "suitable_soil_types": [1, 3, 7],  # رملية، طميية، غضارية
        "suitable_crops": [1, 2, 3]  # خضروات، قمح، أرز
    },
    {
        "id": 4,
        "name": "ري تحت السطحي",
        "efficiency": 0.92,
        "cost_per_cubic_meter": 18,
        "energy_consumption": 0.2,
        "installation_cost": 15000,
        "maintenance_cost": 500,
        "lifespan": 15,
        "suitable_soil_types": [1, 3, 6],  # رملية، طميية، طفيلية
        "suitable_crops": [4, 5, 9, 10]  # عنب، توت، نباتات زينة، محاصيل صفية
    },
    {
        "id": 5,
        "name": "ري بالأنابيب",
        "efficiency": 0.85,
        "cost_per_cubic_meter": 12,
        "energy_consumption": 0.4,
        "installation_cost": 10000,
        "maintenance_cost": 700,
        "lifespan": 12,
        "suitable_soil_types": [1, 3, 5],  # رملية، طميية، جيرية
        "suitable_crops": [1, 2, 3, 4, 5]  # خضروات، قمح، أرز، عنب، توت
    },
    # الأنواع المضافة حديثًا
    {
        "id": 6,
        "name": "ري محوري",
        "efficiency": 0.85,
        "cost_per_cubic_meter": 10,
        "energy_consumption": 1.5,
        "installation_cost": 25000,
        "maintenance_cost": 1200,
        "lifespan": 15,
        "suitable_soil_types": [2, 3, 6],  # طينية خفيفة، طميية، طفيلية
        "suitable_crops": [2, 6, 7]  # قمح، برسيم، نباتات علفية
    },
    {
        "id": 7,
        "name": "ري بالفقاعات (Bubbler)",
        "efficiency": 0.88,
        "cost_per_cubic_meter": 14,
        "energy_consumption": 0.6,
        "installation_cost": 9000,
        "maintenance_cost": 550,
        "lifespan": 12,
        "suitable_soil_types": [1, 3, 4],  # رملية، طميية، طميية
        "suitable_crops": [3, 4, 5]  # أشجار فاكهة، عنب، توت
    },
    {
        "id": 8,
        "name": "ري ذاتي (ذكي)",
        "efficiency": 0.96,
        "cost_per_cubic_meter": 20,
        "energy_consumption": 0.7,
        "installation_cost": 18000,
        "maintenance_cost": 1000,
        "lifespan": 10,
        "suitable_soil_types": [1, 3, 4, 5],  # رملية، طميية، طميية، جيرية
        "suitable_crops": [1, 4, 5, 9, 10]  # خضروات، عنب، توت، نباتات زينة، محاصيل صفية
    },
    {
        "id": 9,
        "name": "ري بالضباب (Mist Irrigation)",
        "efficiency": 0.90,
        "cost_per_cubic_meter": 16,
        "energy_consumption": 1.0,
        "installation_cost": 7500,
        "maintenance_cost": 650,
        "lifespan": 8,
        "suitable_soil_types": [1, 4],  # رملية، طميية
        "suitable_crops": [9, 10]  # نباتات زينة، محاصيل صفية (بيوت محمية)
    },
    {
        "id": 10,
        "name": "ري بالسواقي (الري السطحي التقليدي)",
        "efficiency": 0.55,
        "cost_per_cubic_meter": 4,
        "energy_consumption": 0.1,
        "installation_cost": 2000,
        "maintenance_cost": 300,
        "lifespan": 20,
        "suitable_soil_types": [3, 7],  # طميية، غضارية
        "suitable_crops": [1, 2, 3]  # خضروات، قمح، أرز
    }
]

# قاعدة بيانات الأسمدة
fertilizers_data = [
    {
        "id": 1,
        "name": "يوريا",
        "type": "نيتروجين",
        "n_content": 46,
        "p_content": 0,
        "k_content": 0,
        "cost_per_kg": 60,
        "carbon_footprint": 3.5,
        "solubility": 1080,
        "volatilization_factor": 0.15,
        "leaching_factor": 0.25
    },
    {
        "id": 2,
        "name": "سلفات الأمونيوم",
        "type": "نيتروجين",
        "n_content": 21,
        "p_content": 0,
        "k_content": 0,
        "cost_per_kg": 40,
        "carbon_footprint": 2.5,
        "solubility": 750,
        "volatilization_factor": 0.08,
        "leaching_factor": 0.18
    },
    {
        "id": 3,
        "name": "فوسفات أحادي الأمونيوم (MAP)",
        "type": "فوسفات",
        "n_content": 11,
        "p_content": 52,
        "k_content": 0,
        "cost_per_kg": 55,
        "carbon_footprint": 2.8,
        "solubility": 370,
        "volatilization_factor": 0.05,
        "leaching_factor": 0.10
    },
    {
        "id": 4,
        "name": "كلوريد البوتاسيوم",
        "type": "بوتاسيوم",
        "n_content": 0,
        "p_content": 0,
        "k_content": 60,
        "cost_per_kg": 45,
        "carbon_footprint": 1.8,
        "solubility": 340,
        "volatilization_factor": 0.02,
        "leaching_factor": 0.20
    },
    {
        "id": 5,
        "name": "سماد عضوي (كمبوست)",
        "type": "عضوي",
        "n_content": 2,
        "p_content": 1,
        "k_content": 2,
        "cost_per_kg": 5,
        "carbon_footprint": 0.8,
        "solubility": 10,
        "volatilization_factor": 0.15,
        "leaching_factor": 0.05
    },
    # الأنواع المضافة حديثًا
    {
        "id": 6,
        "name": "نترات الأمونيوم",
        "type": "نيتروجين",
        "n_content": 34,
        "p_content": 0,
        "k_content": 0,
        "cost_per_kg": 65,
        "carbon_footprint": 3.2,
        "solubility": 1180,
        "volatilization_factor": 0.03,  # منخفضة بسبب شكل النترات
        "leaching_factor": 0.40        # عالية بسبب سهولة ذوبان النترات
    },
    {
        "id": 7,
        "name": "فوسفات ثنائي الأمونيوم (DAP)",
        "type": "مركب",
        "n_content": 18,
        "p_content": 46,
        "k_content": 0,
        "cost_per_kg": 70,
        "carbon_footprint": 3.0,
        "solubility": 410,
        "volatilization_factor": 0.10,
        "leaching_factor": 0.15
    },
    {
        "id": 8,
        "name": "سلفات البوتاسيوم",
        "type": "بوتاسيوم",
        "n_content": 0,
        "p_content": 0,
        "k_content": 50,
        "cost_per_kg": 75,
        "carbon_footprint": 2.0,
        "solubility": 120,
        "volatilization_factor": 0.02,
        "leaching_factor": 0.15
    },
    {
        "id": 9,
        "name": "نترات البوتاسيوم",
        "type": "مركب",
        "n_content": 13,
        "p_content": 0,
        "k_content": 44,
        "cost_per_kg": 85,
        "carbon_footprint": 3.3,
        "solubility": 360,
        "volatilization_factor": 0.03,
        "leaching_factor": 0.35
    },
    {
        "id": 10,
        "name": "NPK مركب (15-15-15)",
        "type": "مركب",
        "n_content": 15,
        "p_content": 15,
        "k_content": 15,
        "cost_per_kg": 80,
        "carbon_footprint": 3.6,
        "solubility": 200,
        "volatilization_factor": 0.12,
        "leaching_factor": 0.25
    },
    {
        "id": 11,
        "name": "جبس زراعي",
        "type": "كبريت",
        "n_content": 0,
        "p_content": 0,
        "k_content": 0,
        "cost_per_kg": 15,
        "carbon_footprint": 1.2,
        "solubility": 2.4,  # ذوبانية منخفضة
        "volatilization_factor": 0.01,
        "leaching_factor": 0.05
    },
    {
        "id": 12,
        "name": "سماد الدواجن",
        "type": "عضوي",
        "n_content": 4,
        "p_content": 3,
        "k_content": 2,
        "cost_per_kg": 8,
        "carbon_footprint": 1.5,
        "solubility": 30,
        "volatilization_factor": 0.25,  # عالية بسبب محتوى النيتروجين الأمونيومي
        "leaching_factor": 0.15
    }
]

class Database:
    def __init__(self):
        # في تطبيق حقيقي، سيتم الاتصال بقاعدة بيانات حقيقية
        # هنا نستخدم قواميس البيانات المحددة أعلاه
        self.plants = plants_data
        self.wilayas = wilayas_data
        self.soil_types = soil_types_data
        self.water_systems = water_systems_data
        self.fertilizers = fertilizers_data
    
    def get_all_plants(self):
        """الحصول على جميع النباتات"""
        return self.plants
    
    def get_plant_by_id(self, plant_id):
        """الحصول على نبات محدد بالمعرف"""
        for plant in self.plants:
            if plant['id'] == plant_id:
                return plant
        return None
    
    def get_all_wilayas(self):
        """الحصول على جميع الولايات"""
        return self.wilayas
    
    def get_wilaya_by_id(self, wilaya_id):
        """الحصول على ولاية محددة بالمعرف"""
        for wilaya in self.wilayas:
            if wilaya['id'] == wilaya_id:
                return wilaya
        return None
    
    def get_all_soil_types(self):
        """الحصول على جميع أنواع التربة"""
        return self.soil_types
    
    def get_soil_type_by_id(self, soil_type_id):
        """الحصول على نوع تربة محدد بالمعرف"""
        for soil_type in self.soil_types:
            if soil_type['id'] == soil_type_id:
                return soil_type
        return None
    
    def get_all_water_systems(self):
        """الحصول على جميع أنظمة الري"""
        return self.water_systems
    
    def get_water_system_by_id(self, water_system_id):
        """الحصول على نظام ري محدد بالمعرف"""
        for water_system in self.water_systems:
            if water_system['id'] == water_system_id:
                return water_system
        return None
    
    def get_all_fertilizers(self):
        """الحصول على جميع الأسمدة"""
        return self.fertilizers
    
    def get_fertilizer_by_id(self, fertilizer_id):
        """الحصول على سماد محدد بالمعرف"""
        for fertilizer in self.fertilizers:
            if fertilizer['id'] == fertilizer_id:
                return fertilizer
        return None