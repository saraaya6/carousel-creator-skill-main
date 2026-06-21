import argparse
import re
import os

# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate BitToBest Git Horror Carousel")
parser.add_argument("--dark", type=str, default="#0A192F", help="Custom dark hex color (e.g. #0A192F)")
parser.add_argument("--light", type=str, default="#ffffff", help="Custom light hex color (e.g. #ffffff)")
args = parser.parse_args()

script_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(script_dir, 'template.html')

with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the highly concise and human-centric Git & GitHub slides JSON
slides_js = """[
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h1',
    main: 'تحسب <strong>Git</strong> هو نفسه <strong>GitHub</strong>؟ 🤯',
    footer: 'اسحب الشاشة'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'مشكلة <strong>"الملف النهائي الحقيقي"</strong> 💀',
    sub: 'تذكر لما كنت تكتب بحث وتسميه: (النهائي)، (النهائي 2)، (النهائي والله العظيم)؟<br><br>في الكود هذي الطريقة كارثة.. والـ Git جاء يحلها بالكامل!',
    footer: 'وش السالفة؟'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'الـ <strong>Git</strong>: آلة الزمن بجهازك ⏳',
    sub: 'نظام يشتغل داخل لابتوبك. وظيفته يصور كودك بكل مرحلة.<br><br>لو عدلت شي وخرب المشروع؟ بضغطة زر يرجعك للنسخة اللي كانت شغالة تمام.',
    footer: 'آلة الزمن الكودية'
  },
  {
    type: 'hook',
    label: 'BitToBest',
    tag: 'h2',
    main: 'الـ <strong>GitHub</strong>: سحابة المبرمجين ☁️',
    sub: 'موقع ترفع عليه اللقطات اللي صورها الـ Git.<br><br>عشان كودك ما يضيع لو خرب جهازك، وعشان تشتغل مع فريقك على نفس المشروع بدون ما يخرب شغل أحد.',
    footer: 'السحابة البرمجية'
  },
  {
    type: 'stack',
    label: 'BitToBest',
    main: 'قاموس الـ <strong>Git</strong>: على جهازك 💻',
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
    label: 'BitToBest',
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
    label: 'BitToBest',
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
    label: 'BitToBest',
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
    label: 'BitToBest',
    tag: 'h2',
    main: 'نصيحة من تجربة ✨',
    sub: 'تكفى.. لا تكتب في الـ Commit رسالة زي "fixed" أو "تعديل".<br><br>اكتب وش غيرت بالضبط بذكاء. بعد 6 شهور لما ترجع لكودك، بتشكر نفسك وتدعي لي! 😉',
    footer: 'نصيحة'
  },
  {
    type: 'cta',
    label: 'BitToBest',
    main: 'احفظه وشاركه! 🎓🔥',
    sub: 'الحين وضحت لك الصورة؟<br><br>احفظ البوست لأنك بتحتاجه وقت الزنقة، ورسله لقروب التخرج عشان ترتاحون من حوسة الملفات!',
    cta: 'اكتب "جيت" بالتعليقات وأرسل لك ملخص كامل لأشهر أوامر Git اللي تنقذ حياتك!',
    footer: '★ حفظ'
  }
]"""

# Replace the slides array in template
content = re.sub(r'const slides = \[.*?\];', f'const slides = {slides_js};', content, flags=re.DOTALL)

# Replace the default language
content = content.replace("applyLanguage('en');", "applyLanguage('ar');")

# Replace custom color values inside init call
content = content.replace("applyCustomColors('#0A192F', '#ffffff');", f"applyCustomColors('{args.dark}', '{args.light}');")

# Make sure outputs directory exists
output_dir = os.path.join(script_dir, 'outputs')
os.makedirs(output_dir, exist_ok=True)

# Define output path
output_path = os.path.join(output_dir, 'carousel-tech-ar-git-horror.html')

# Save new file
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated updated and shortened pure beige and black carousel at {output_path}")
