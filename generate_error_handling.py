import argparse
import re
import os

# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate BitToBest Error Handling Carousel")
parser.add_argument("--dark", type=str, default="#0A192F", help="Custom dark hex color (e.g. #0A192F)")
parser.add_argument("--light", type=str, default="#ffffff", help="Custom light hex color (e.g. #ffffff)")
args = parser.parse_args()

script_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(script_dir, 'template.html')

with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the Saudi dialect slides JSON
slides_json = """[
  { type: 'hook',  label: 'BitToBest', tag: 'h1', main: 'كودك يشتغل.. <br><strong>بس كم مرة انهار في البرودكشن؟</strong> 🤯', footer: 'اسحب الشاشة' },
  { type: 'hook',  label: 'BitToBest', tag: 'h2', main: 'كلنا نمر بنفس الشعور:', sub: 'تخلص الميزة (Feature)، تفرح وتعمل Push.. وفجأة السيرفر يطيح!<br><br>السبب غالباً مو إنك مبرمج سيء، السبب هو غياب الـ Error Handling الصحيح.', footer: 'المشكلة' },
  { type: 'hook',  label: 'BitToBest', tag: 'h3', main: 'القاعدة الذهبية في BitToBest:', sub: 'لا تفترض أبداً أن <strong>"كل شيء تمام".</strong><br><br>استخدم <span class="accent-text ltr-inline">try-catch</span> دائماً، وتوقع غير المتوقع (مثل انقطاع الاتصال بقاعدة البيانات أو مدخلات خاطئة).', footer: 'الحل اللطيف' },
  { type: 'hook',  label: 'BitToBest', tag: 'h3', main: 'ابدأ اليوم:', sub: 'بدلاً من طباعة الخطأ بـ <strong>console.log(error)</strong>..<br><br>استخدم نظام Log محترم يوضح لك (أين ومتى ولماذا) حدثت المشكلة لتصلحها في ثوانٍ.', footer: 'نصيحة سريعة' },
  { type: 'cta',   label: 'BitToBest', main: 'شاركنا في التعليقات:', sub: 'وش أغرب "Bug" واجهك وخلاك تشك بمهاراتك البرمجية؟ 🛠️', cta: 'للمزيد من الممارسات الاحترافية، تابع خارطة الطريق في موقعنا: bittobest.com', footer: '★ حفظ' }
]"""

# Replace slides
content = re.sub(r'const slides = \[.*?\];', f'const slides = {slides_json};', content, flags=re.DOTALL)

# Replace the default language
content = content.replace("applyLanguage('en');", "applyLanguage('ar');")

# Replace custom color values inside init call
content = content.replace("applyCustomColors('#0A192F', '#ffffff');", f"applyCustomColors('{args.dark}', '{args.light}');")

# Make sure outputs directory exists
output_dir = os.path.join(script_dir, 'outputs')
os.makedirs(output_dir, exist_ok=True)

# Define output path
output_path = os.path.join(output_dir, 'carousel-error-handling.html')

# Save new file
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done generating carousel-error-handling.html")
