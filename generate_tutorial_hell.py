import argparse
import re
import os

# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate BitToBest Tutorial Hell Carousel")
parser.add_argument("--dark", type=str, default="#1e0b36", help="Custom dark hex color (e.g. #1e0b36)")
parser.add_argument("--light", type=str, default="#ffffff", help="Custom light hex color (e.g. #ffffff)")
args = parser.parse_args()

script_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(script_dir, 'template.html')

with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the Saudi dialect slides JSON
slides_js = """[
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h1',
    main: 'تتابع كورس ورا كورس ولسا <strong>مو جاهز؟</strong>',
    footer: 'اسحب الشاشة'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'تجميع الشهادات يعطيك <strong>شعور وهمي</strong> بالإنجاز.',
    sub: 'بينما الحقيقة؟ أنت جالس تنسخ كود المدرب بدون ما تفهم كيف تبني بنفسك.',
    footer: 'السر النفسي خلف الفخ'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h3',
    main: 'تحس بالأمان والفيديو شغال، وتضيع أول ما تفتح صفحة بيضاء؟',
    sub: 'دماغك يتعرف على الحل بسهولة بس ما يعرف يستدعيه لما يكون لحاله. هل قد عشت هذا الشعور؟',
    footer: 'وهم المعرفة'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'الحل يبدأ بـ <strong>قاعدة 20/80</strong>',
    sub: 'خصص 20% فقط من وقتك لمشاهدة الكورس، والـ 80% الباقية طبق فيها عملياً واغلط براحتك.',
    footer: 'النسبة الذهبية'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'الشركات ما توظف <strong>جامعي شهادات</strong>',
    sub: 'في المقابلات التقنية، محد يهمه كم كورس خلصت. يهمهم كم مشكلة حليت وبنيت بنفسك.',
    footer: 'واقع سوق العمل'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'ابنِ مشاريع <strong>تعدلها بنفسك</strong>',
    sub: 'إذا طبقت مشروع كورس، غير فيه! أضف ميزة جديدة، غير التصميم، خله يخصك. كذا تبني عضلاتك البرمجية.',
    footer: 'طريقة التعديل'
  },
  {
    type: 'stack',
    label: 'BitToBest',
    rows: [
      { cat: 'جامع الشهادات', val: 'ينسخ الكود ويجمع ورق' },
      { cat: 'المبرمج الحقيقي', val: 'يغلط، يبحث، ويبني مشاريع' },
      { cat: 'الهدف الأهم', val: 'معرض أعمال قوي يثبت قوتك' }
    ],
    footer: 'فرق جوهري'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'التعلم مو بكثرة الفيديوهات.',
    sub: 'التعلم الحقيقي هو عدد المرات اللي <strong>تعطل فيها الكود</strong> وعرفت كيف تحل المشكلة بنفسك.',
    footer: 'منعطف حاسم'
  },
  {
    type: 'steps',
    label: 'BitToBest',
    items: [
      'قفل الكورس وابدأ فكرة مشروع بسيطة',
      'ابحث بالـ Documentation وحل مشاكلك بنفسك',
      'ارفع مشاريعك على GitHub ورتب معرض أعمالك'
    ],
    footer: 'خطتك للهروب اليوم'
  },
  {
    type: 'cta',
    label: 'BitToBest',
    main: 'جاهز للهروب؟',
    sub: 'لا تخلي الكورسات تخدعك وتضيع وقتك، ابدأ ابنِ معرض أعمالك اليوم.',
    cta: 'اكتب "جاهز" بالتعليقات وأرسل لك دليل بناء أول مشروع حقيقي بنفسك!',
    footer: '★ BitToBest'
  }
]"""

# Replace the slides array in template
content = re.sub(r'const slides = \[.*?\];', f'const slides = {slides_js};', content, flags=re.DOTALL)

# Replace the default language
content = content.replace("applyLanguage('en');", "applyLanguage('ar');")

# Replace custom color values inside init call
content = content.replace("applyCustomColors('#1e0b36', '#ffffff');", f"applyCustomColors('{args.dark}', '{args.light}');")

# Make sure outputs directory exists
output_dir = os.path.join(script_dir, 'outputs')
os.makedirs(output_dir, exist_ok=True)

# Define output path
output_path = os.path.join(output_dir, 'carousel-tech-ar-tutorial-hell.html')

# Save new file
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated carousel at {output_path}")
