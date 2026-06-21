import re
import json

with open('/Users/sartmhmdalmry/Desktop/carousel-creator-skill-main/template.html', 'r', encoding='utf-8') as f:
    content = f.read()

slides_json = """[
  { type: 'hook',  label: 'سارة المهندسة', tag: 'h1', main: 'أكثر تخصص تقني <span class="accent-text">مظلوم.</span>', sub: 'مو مجرد "جوجل درايف".', footer: 'اسحب الشاشة' },
  { type: 'hook',  label: 'سارة المهندسة', tag: 'h2', main: 'الإعلام صور الكلاود للناس على إنه مجرد مساحة تخزين.', sub: 'بينما هو في الحقيقة "المصنع" اللي يشتغل فيه الذكاء الاصطناعي وكل المواقع الضخمة.', footer: 'كمل قراءة' },
  { type: 'hook',  label: 'سارة المهندسة', tag: 'h3', main: 'الزاوية اللي الكل غافل عنها؟', sub: 'إن السعودية الآن من أكبر أسواق الحوسبة في المنطقة، وهذا يعني فرص وظيفية مهولة.', footer: 'العمود الفقري المختفي' },
  { type: 'hook',  label: 'سارة المهندسة', tag: 'h2', main: 'وش هي الحوسبة السحابية أصلاً؟', sub: 'ببساطة: بدل ما الشركات تشتري سيرفرات غالية، تستأجر كمبيوترات ضخمة عن بعد وتدفع بس على قد استخدامها.', footer: 'توفير ومرونة' },
  { type: 'stack', label: 'سارة المهندسة', rows: [
      { cat: 'الطلب في السوق', val: 'عجز كبير في الكفاءات السحابية' },
      { cat: 'الرواتب', val: 'من الأعلى في قطاع التقنية حالياً' },
      { cat: 'الاستثمارات', val: 'مليارات تضخها الشركات الكبرى' }
    ], footer: 'أرقام تتكلم' },
  { type: 'steps', label: 'سارة المهندسة', items: [
      'دخول عملاق لـ Google Cloud للسعودية',
      'مراكز بيانات ضخمة لـ Oracle و Microsoft',
      'توسع غير مسبوق لـ Amazon Web Services'
    ], footer: 'عمالقة التقنية عندنا' },
  { type: 'hook',  label: 'سارة المهندسة', tag: 'h2', main: 'طيب وش تدرس في هالتخصص؟', sub: 'تدرس كيف تبني، تدير، وتحمي هذي البنية التحتية الضخمة اللي تعتمد عليها كل التطبيقات والجهات الحكومية اليوم.', footer: 'مهندس المستقبل' },
  { type: 'steps', label: 'سارة المهندسة', items: [
      'تفهم أساسيات الشبكات',
      'تتقن أنظمة التشغيل (زي Linux)',
      'تبدأ تاخذ شهادات مهنية من أمازون أو مايكروسوفت'
    ], footer: 'كيف تبدأ؟' },
  { type: 'hook',  label: 'سارة المهندسة', tag: 'h2', main: 'الخطوة الأولى العملية:', sub: 'شهادة <span class="accent-text ltr-inline">AWS Cloud Practitioner</span> أو <span class="accent-text ltr-inline">Azure Fundamentals</span> تعطيك الأساسيات وتفتح لك أبواب المقابلات.', footer: 'ابدأ اليوم' },
  { type: 'cta',   label: 'سارة المهندسة', main: 'احفظ البوست.', sub: 'عشان ترجع لأسماء الشهادات بعدين.', cta: 'اكتب "كلاود" في التعليقات وأرسل لك مسار التعلم كامل.', footer: '★ حفظ' }
]"""

# Replace slides
content = re.sub(r'const slides = \[.*?\];', f'const slides = {slides_json};', content, flags=re.DOTALL)

# Add aws theme
aws_theme = """
  aws: {
    colors: { dark: '#232F3E', light: '#FFFFFF', accent: '#FF9900' },
    text:   { onDark: '#FFFFFF', onLight: '#232F3E', onAccent: '#FFFFFF', onAccentEmph: '#232F3E' },
    fonts: {
      en: { heading: "'Inter Tight', sans-serif", body: "'Space Grotesk', sans-serif", numeral: "'Inter Tight', sans-serif" },
      ar: { heading: "'Cairo', sans-serif", body: "'Cairo', sans-serif", numeral: "'Cairo', sans-serif" }
    },
    weights: { heading: 900, numeral: 900 },
    radius: '8px',
    tracking: { h: '0px', h2: '0px' },
    lineHeight: '1.2',
    bignumOpacity: 0.05
  },"""
content = content.replace('const themes = {', f'const themes = {{{aws_theme}')

# Replace language and theme applications
content = content.replace("applyLanguage('en');", "applyLanguage('ar');")
content = content.replace("applyTheme('tech');", "applyTheme('aws');")

# Save new file
with open('/Users/sartmhmdalmry/Desktop/carousel-creator-skill-main/carousel-aws-ar-cloud-computing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
