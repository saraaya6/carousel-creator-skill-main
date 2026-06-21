import re
import os

# Read the template file
template_path = '/Users/sartmhmdalmry/Desktop/carousel-creator-skill-main/template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the highly concise and human-centric Git & GitHub slides JSON
slides_js = """[
  {
    type: 'hook',
    label: 'سارة المهندسة',
    tag: 'h1',
    main: 'تحسب <span class="accent-text">Git</span> هو نفسه <span class="accent-text">GitHub</span>؟ 🤯',
    sub: 'إذا بتسوي مشروع تخرج أو بتقدم على وظيفة.. تعال أقول لك وش الفرق الحقيقي وبأبسط شكل!',
    footer: 'اسحب الشاشة'
  },
  {
    type: 'hook',
    label: 'سارة المهندسة',
    tag: 'h2',
    main: 'مشكلة "الملف النهائي الحقيقي" 💀',
    sub: 'تذكر لما كنت تكتب بحث وتسميه: (النهائي)، (النهائي 2)، (النهائي والله العظيم)؟<br><br>في الكود هذي الطريقة كارثة.. والـ Git جاء يحلها بالكامل!',
    footer: 'وش السالفة؟'
  },
  {
    type: 'hook',
    label: 'سارة المهندسة',
    tag: 'h2',
    main: 'الـ <span class="accent-text">Git</span>: آلة الزمن بجهازك ⏳',
    sub: 'نظام يشتغل داخل لابتوبك. وظيفته يصور كودك بكل مرحلة.<br><br>لو عدلت شي وخرب المشروع؟ بضغطة زر يرجعك للنسخة اللي كانت شغالة تمام.',
    footer: 'آلة الزمن الكودية'
  },
  {
    type: 'hook',
    label: 'سارة المهندسة',
    tag: 'h2',
    main: 'الـ <span class="accent-text">GitHub</span>: سحابة المبرمجين ☁️',
    sub: 'موقع ترفع عليه اللقطات اللي صورها الـ Git.<br><br>عشان كودك ما يضيع لو خرب جهازك، وعشان تشتغل مع فريقك على نفس المشروع بدون ما يخرب شغل أحد.',
    footer: 'السحابة البرمجية'
  },
  {
    type: 'stack',
    label: 'سارة المهندسة',
    main: 'قاموس الـ <span class="accent-text">Git</span>: على جهازك 💻',
    sub: 'ثلاثة مفاهيم تدور كلها داخل لابتوبك:',
    rows: [
      { cat: 'Repo', val: 'مجلد مشروعك اللي يراقبه الـ Git ويحفظ تاريخه.' },
      { cat: 'Commit', val: 'لقطة سريعة لحفظ كودك وتوثيق التعديل الحالي.' },
      { cat: 'Branch', val: 'غصن جانبي تجرب فيه كودك الجديد بدون تخريب الأساسي.' }
    ],
    footer: 'قاموس المصطلحات ١'
  },
  {
    type: 'stack',
    label: 'سارة المهندسة',
    main: 'تابع القاموس: مع التيم أونلاين ☁️',
    sub: 'كيف تتواصل مع السحابة والشباب بالعمل الجماعي:',
    rows: [
      { cat: 'Push', val: 'ترفع لقطات كودك من جهازك إلى موقع GitHub أونلاين.' },
      { cat: 'Pull', val: 'تسحب تعديلات فريقك الجديدة والجاهزة لجهازك.' },
      { cat: 'Merge', val: 'تدمج كودك الجانبي مع الأساسي بعد ما تتأكد منه.' }
    ],
    footer: 'قاموس المصطلحات ٢'
  },
  {
    type: 'stack',
    label: 'سارة المهندسة',
    main: 'أوامر البداية والتحضير 🧙‍♂️',
    sub: 'تكتبها في الـ Terminal عشان تبدأ مشروعك وتجهزه:',
    rows: [
      { cat: 'git init', val: 'تشغل الـ Git في مجلد مشروعك لأول مرة.' },
      { cat: 'git add .', val: 'تجهز كل الملفات اللي غيرتها عشان تتصور بالكامل.' }
    ],
    footer: 'الأوامر السحرية ١'
  },
  {
    type: 'stack',
    label: 'سارة المهندسة',
    main: 'أوامر الحفظ والرفع أونلاين 🚀',
    sub: 'عشان توثق وترفع تعبك وتشاركه مع التيم:',
    rows: [
      { cat: 'git commit -m "رسالة"', val: 'تحفظ اللقطة بجهازك مع شرح بسيط للتعديل.' },
      { cat: 'git push origin main', val: 'ترفع شغلك واللقطات الحالية أونلاين على GitHub.' },
      { cat: 'git status', val: 'تشوف الملفات اللي تعدلت ولسه ما حفظتها.' }
    ],
    footer: 'الأوامر السحرية ٢'
  },
  {
    type: 'hook',
    label: 'سارة المهندسة',
    tag: 'h2',
    main: 'نصيحة من تجربة ✨',
    sub: 'تكفى.. لا تكتب في الـ Commit رسالة زي "fixed" أو "تعديل".<br><br>اكتب وش غيرت بالضبط بذكاء. بعد 6 شهور لما ترجع لكودك، بتشكر نفسك وتدعي لي! 😉',
    footer: 'نصيحة سارة المهندسة'
  },
  {
    type: 'cta',
    label: 'سارة المهندسة',
    main: 'احفظه وشاركه! 🎓🔥',
    sub: 'الحين وضحت لك الصورة؟<br><br>احفظ البوست لأنك بتحتاجه وقت الزنقة، ورسله لقروب التخرج عشان ترتاحون من حوسة الملفات!',
    cta: 'اكتب "جيت" بالتعليقات وأرسل لك ملخص كامل لأشهر أوامر Git اللي تنقذ حياتك!',
    footer: '★ سارة المهندسة'
  }
]"""

# Replace the slides array in template
content = re.sub(r'const slides = \[.*?\];', f'const slides = {slides_js};', content, flags=re.DOTALL)

# Add custom brand colors as 'sara_beige' theme (Pure Beige & Black)
sara_theme = """
  sara_beige: {
    colors: { dark: '#0A0A0A', light: '#F5F0E8', accent: '#F5F0E8' },
    text:   { onDark: '#F5F0E8', onLight: '#0A0A0A', onAccent: '#0A0A0A', onAccentEmph: '#0A0A0A' },
    fonts: {
      en: { heading: "'Inter Tight', sans-serif", body: "'Space Grotesk', sans-serif", numeral: "'Inter Tight', sans-serif" },
      ar: { heading: "'IBM Plex Sans Arabic', sans-serif", body: "'Cairo', sans-serif", numeral: "'IBM Plex Sans Arabic', sans-serif" }
    },
    weights: { heading: 900, numeral: 900 },
    radius: '0px', /* Clean editorial square corners for premium feel */
    tracking: { h: '-1.5px', h2: '-1px' },
    lineHeight: '1.25',
    bignumOpacity: 0.05
  },"""

content = content.replace('const themes = {', f'const themes = {{{sara_theme}')

# Inject custom brand style rules for pure Beige and Black theme
custom_css = """
  /* Custom Branding Rules for Sara Al-Muhandisa - Pure Beige & Black */
  .slide.dark h1, .slide.dark h2, .slide.dark h3 {
    color: #F5F0E8 !important; /* Beige for dark slide headings */
  }
  .slide.light h1, .slide.light h2, .slide.light h3 {
    color: #0A0A0A !important; /* Black for light slide headings */
  }
  .slide.dark .accent-text {
    color: #F5F0E8 !important;
    text-decoration: underline;
    text-decoration-color: #F5F0E8 !important;
    text-underline-offset: 6px;
    text-decoration-thickness: 2px;
  }
  .slide.light .accent-text {
    color: #0A0A0A !important;
    text-decoration: underline;
    text-decoration-color: #0A0A0A !important;
    text-underline-offset: 6px;
    text-decoration-thickness: 2px;
  }
  .slide.accent h1, .slide.accent h2, .slide.accent h3 {
    color: var(--text-on-accent) !important;
  }
  .row .cat {
    color: #F5F0E8 !important; /* Beige on dark slides */
    opacity: 1 !important;
    font-weight: 700;
    letter-spacing: 0.5px;
  }
  .slide.light .row .cat {
    color: #0A0A0A !important; /* Black on light slides */
  }
  .slide.accent .row .cat {
    color: var(--text-on-accent) !important;
  }
  .dot {
    background: currentColor !important; /* Dot matches current text color */
  }
"""

content = content.replace('</style>', f'{custom_css}\n</style>')

# Enhance the stack renderer in memory to handle title/subtitle
old_stack_renderer = 'body = `<div class="stack">${s.rows.map(r => `<div class="row"><div class="cat">${r.cat}</div><div class="val">${r.val}</div></div>`).join(\'\')}</div>`;'
new_stack_renderer = """body = '';
      if (s.main) body += `<h2>${s.main}</h2>`;
      if (s.sub) body += `<div style="height:12px;"></div><div class="body-text" style="opacity:0.6;font-size:16px;line-height:1.4;margin-bottom:12px;">${s.sub}</div>`;
      body += `<div class="stack" style="gap:14px;">${s.rows.map(r => `<div class="row" style="padding-top:8px;gap:2px;"><div class="cat" style="font-size:11px;margin-bottom:2px;">${r.cat}</div><div class="val" style="font-size:18px;">${r.val}</div></div>`).join('')}</div>`;"""

content = content.replace(old_stack_renderer, new_stack_renderer)

# Replace the default theme and language applications
content = content.replace("applyLanguage('en');", "applyLanguage('ar');")
content = content.replace("applyTheme('tech');", "applyTheme('sara_beige');")

# Make sure outputs directory exists
output_dir = '/Users/sartmhmdalmry/Desktop/carousel-creator-skill-main/outputs'
os.makedirs(output_dir, exist_ok=True)

# Define output path
output_path = os.path.join(output_dir, 'carousel-tech-ar-git-horror.html')

# Save new file
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated updated and shortened pure beige and black carousel at {output_path}")
