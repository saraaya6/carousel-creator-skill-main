import argparse
import re
import os

# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate BitToBest AI Shift Carousel")
parser.add_argument("--dark", type=str, default="#0A192F", help="Custom dark hex color (e.g. #0A192F)")
parser.add_argument("--light", type=str, default="#ffffff", help="Custom light hex color (e.g. #ffffff)")
args = parser.parse_args()

script_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(script_dir, 'template.html')

with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the Saudi dialect slides JSON for the AI shift topic
slides_js = """[
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h1',
    main: 'كودك شغال في ChatGPT.. <br><strong>بس ليش ينهار في البرودكشن؟</strong> 🤯',
    footer: 'اسحب الشاشة'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'الـ ChatGPT ممتاز للأفكار السريعة..',
    sub: 'لكن الاعتماد الأعمى عليه صار كابوس! تنسخ الكود، تشغله، وبأول ضغط عمل حقيقي ينهار النظام بالكامل. وش السبب؟',
    footer: 'المشكلة الحقيقية'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'لأن الـ AI ما يدري عن <strong>سياق مشروعك</strong> بالكامل!',
    sub: 'الملفات، قواعد البيانات، والربط بين الأجزاء.. كل هالأمور ChatGPT ما يشوفها، فيعطيك كود يهلوس أو يتعارض مع ملفاتك.',
    footer: 'فجوة السياق'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'الحل؟ الانتقال لـ <strong>النماذج المدمجة (IDEs)</strong>',
    sub: 'مثل Claude 3.5 Sonnet أو GitHub Copilot داخل بيئة عملك. هذي الأدوات تقرأ مشروعك كامل وتفهم الترابط بين ملفاتك تلقائياً.',
    footer: 'التحول الجديد'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'اكتب المنطق بنفسك.. <strong>وخل الـ AI يراجعك!</strong>',
    sub: 'المبرمج المحترف يكتب الهيكل والمنطق الأساسي بيده، ثم يطلب من الـ AI مراجعة الكود، البحث عن الثغرات الأمنية، وتحسين الأداء.',
    footer: 'الممارسة الصحيحة'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'خل الـ AI يكتب لك <strong>الاختبارات (Tests)</strong>',
    sub: 'كتابة اختبارات الكود (Unit Tests) تستهلك وقت المبرمج. دع الذكاء الاصطناعي يغطي الحالات المختلفة (Edge Cases) ويوفر وقتك اليوم.',
    footer: 'تسريع العمل'
  },
  {
    type: 'stack',
    label: 'BitToBest',
    main: 'كيف تغيرت طريقة استخدام الـ AI؟',
    sub: 'الفرق بين استخدام المبتدئ والمطور المحترف للذكاء الاصطناعي:',
    rows: [
      { cat: 'مطور ChatGPT', val: 'نسخ ولصق بدون فهم المنطق' },
      { cat: 'مطور IDE-Integrated', val: 'تعديل الكود في مكانه مع فهم السياق' },
      { cat: 'المطور المحترف', val: 'استخدام الـ AI كمراجع وموجه ومختبر لكوده' }
    ],
    footer: 'مقارنة المنهجية'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'الـ AI أداة لزيادة الإنتاجية.. <strong>وليس تفكيرك الهندسي!</strong>',
    sub: 'الذكاء الاصطناعي لن يحل محل قدرتك على بناء المنطق وحل المشكلات المعقدة. هو مساعدك الشخصي، وليس رئيس المهندسين.',
    footer: 'خلاصة القول'
  },
  {
    type: 'steps',
    label: 'BitToBest',
    main: 'خطتك اليوم لتغيير المعادلة 🚀',
    sub: 'ابدأ بتطبيق هذي الخطوات الثلاث في مشروعك القادم:',
    items: [
      'استخدم أدوات مثل Cursor أو Copilot داخل الـ IDE',
      'اكتب الكود الأساسي بنفسك أولاً لتضمن فهمه',
      'اطلب من الـ AI مراجعة الكود وكتابة الاختبارات'
    ],
    footer: 'خطوات التغيير'
  },
  {
    type: 'cta',
    label: 'BitToBest',
    main: 'احفظ هذا المنشور 📌',
    sub: 'ليحميك في المرة القادمة التي تفكر فيها بالنسخ واللصق الأعمى!',
    cta: 'اكتب "كود" في التعليقات ونرسل لك دليل دمج Claude 3.5 Sonnet مع بيئة تطويرك!',
    footer: '★ حفظ'
  }
]"""

# Replace the slides array in template
content = re.sub(r'const slides = \[.*?\];', f'const slides = {slides_js};', content, flags=re.DOTALL)

# Replace the default language to Arabic
content = content.replace("applyLanguage('en');", "applyLanguage('ar');")
content = content.replace("applyLanguage('ar');", "applyLanguage('ar');") # In case it was already 'ar'

# Replace theme from 'bittobest' to 'tech'
content = content.replace("applyTheme('bittobest');", "applyTheme('tech');")

# Replace custom color values inside init call
content = content.replace("applyCustomColors('#0A192F', '#ffffff');", f"applyCustomColors('{args.dark}', '{args.light}');")

# Make sure outputs directory exists
output_dir = os.path.join(script_dir, 'outputs')
os.makedirs(output_dir, exist_ok=True)

# Define output path
output_path = os.path.join(output_dir, 'carousel-tech-ar-ai-shift.html')

# Save new file
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated carousel at {output_path}")
