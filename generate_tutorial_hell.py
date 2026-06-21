import re
import os

# Read the template file
template_path = '/Users/sartmhmdalmry/Desktop/carousel-creator-skill-main/template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the Saudi dialect slides JSON
slides_js = """[
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h1',
    main: 'تتابع كورس ورا كورس ولسا <span class="accent-text">مو جاهز؟</span>',
    sub: 'تعال أطلعك من "جحيم الكورسات"🛑',
    footer: 'اسحب الشاشة'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'تجميع الشهادات يعطيك <span class="accent-text">شعور وهمي</span> بالإنجاز.',
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
    main: 'الحل يبدأ بـ <span class="accent-text">قاعدة 20/80</span>',
    sub: 'خصص 20% فقط من وقتك لمشاهدة الكورس، والـ 80% الباقية طبق فيها عملياً واغلط براحتك.',
    footer: 'النسبة الذهبية'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'الشركات ما توظف <span class="accent-text">جامعي شهادات</span>',
    sub: 'في المقابلات التقنية، محد يهمه كم كورس خلصت. يهمهم كم مشكلة حليت وبنيت بنفسك.',
    footer: 'واقع سوق العمل'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'ابنِ مشاريع <span class="accent-text">تعدلها بنفسك</span>',
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
    sub: 'التعلم الحقيقي هو عدد المرات اللي <span class="accent-text">تعطل فيها الكود</span> وعرفت كيف تحل المشكلة بنفسك.',
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

# Replace the default theme and language
content = content.replace("applyLanguage('en');", "applyLanguage('ar');")
  # Already tech, but to be sure

# Make sure outputs directory exists
output_dir = '/Users/sartmhmdalmry/Desktop/carousel-creator-skill-main/outputs'
os.makedirs(output_dir, exist_ok=True)

# Define output path
output_path = os.path.join(output_dir, 'carousel-tech-ar-tutorial-hell.html')

# Save new file
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated carousel at {output_path}")
