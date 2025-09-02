import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import arabic_reshaper
from bidi.algorithm import get_display

# مسار مجلد الخطوط
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, '..', 'fonts')

# قائمة الخطوط التي تريد تسجيلها
fonts = {
    'Amiri': 'Amiri-Regular.ttf',
    'Amiri-Bold': 'Amiri-Bold.ttf',
    'Amiri-Italic': 'Amiri-Italic.ttf',
    'Amiri-BoldItalic': 'Amiri-BoldItalic.ttf',
    'AmiriQuran': 'AmiriQuran.ttf'
}

# تسجيل الخطوط
for font_name, font_file in fonts.items():
    try:
        pdfmetrics.registerFont(TTFont(font_name, os.path.join(FONTS_DIR, font_file)))
        print(f"✅ تم تسجيل الخط {font_name}")
    except Exception as e:
        print(f"⚠️ لم يتم تسجيل الخط {font_name}: {e}")

# دالة لتهيئة النص العربي (من اليمين لليسار)
def arabic_text(text):
    try:
        reshaped_text = arabic_reshaper.reshape(text)
        return get_display(reshaped_text)
    except:
        return text

# دالة لإنشاء PDF بالخط الافتراضي
def create_pdf(filename, pagesize=A4):
    c = canvas.Canvas(filename, pagesize=pagesize)
    c.setFont('Amiri', 14)  # الخط الافتراضي Amiri وحجمه 14
    return c

# دالة لرسم نص عربي في Canvas
def draw_arabic_text(canvas_obj, text, x, y, font_name='Amiri', font_size=14, direction='rtl'):
    """
    رسم نص عربي في Canvas مع دعم الاتجاه من اليمين لليسار
    
    المعاملات:
    - canvas_obj: كائن Canvas من ReportLab
    - text: النص المراد رسمه
    - x, y: الإحداثيات
    - font_name: اسم الخط (الافتراضي Amiri)
    - font_size: حجم الخط (الافتراضي 14)
    - direction: اتجاه النص (rtl للعربية، ltr للإنجليزية)
    """
    canvas_obj.setFont(font_name, font_size)
    
    if direction == 'rtl':
        # للنص العربي من اليمين لليسار
        processed_text = arabic_text(text)
        # حساب عرض النص لضبط موقعه
        text_width = canvas_obj.stringWidth(processed_text, font_name, font_size)
        canvas_obj.drawString(x - text_width, y, processed_text)
    else:
        # للنص الإنجليزي من اليسار ليمين
        canvas_obj.drawString(x, y, text)

# دالة لرسم نص عربي متعدد الأسطر
def draw_multiline_arabic_text(canvas_obj, text, x, y, width, height, font_name='Amiri', font_size=14, line_spacing=1.2):
    """
    رسم نص عربي متعدد الأسطر
    
    المعاملات:
    - canvas_obj: كائن Canvas من ReportLab
    - text: النص المراد رسمه
    - x, y: الإحداثيات
    - width, height: أبعاد مربع النص
    - font_name: اسم الخط
    - font_size: حجم الخط
    - line_spacing: المسافة بين الأسطر
    """
    canvas_obj.setFont(font_name, font_size)
    
    # تقسيم النص إلى أسطر
    words = text.split(' ')
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        test_width = canvas_obj.stringWidth(test_line, font_name, font_size)
        
        if test_width <= width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    # رسم الأسطر
    line_height = font_size * line_spacing
    for i, line in enumerate(lines):
        if y - (i * line_height) < 0:  # التحقق من الخروج من الصفحة
            break
        
        processed_line = arabic_text(line)
        line_width = canvas_obj.stringWidth(processed_line, font_name, font_size)
        canvas_obj.drawString(x - line_width, y - (i * line_height), processed_line)