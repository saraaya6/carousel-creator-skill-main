import os
import re

path = '/Users/sartmhmdalmry/Desktop/carousel-creator-skill-main/template.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add 'bittobest' theme
bittobest_theme = """
  bittobest: {
    colors: { dark: '#1A1A3A', light: '#FFFFFF', accent: '#0A0A23' },
    text:   { onDark: '#FFFFFF', onLight: '#1A1A3A', onAccent: '#FFFFFF', onAccentEmph: '#FFFFFF' },
    fonts: {
      en: { heading: "'Inter Tight', sans-serif", body: "'Space Grotesk', sans-serif", numeral: "'Inter Tight', sans-serif" },
      ar: { heading: "'IBM Plex Sans Arabic', sans-serif", body: "'Cairo', sans-serif", numeral: "'IBM Plex Sans Arabic', sans-serif" }
    },
    weights: { heading: 800, numeral: 900 },
    radius: '0px',
    tracking: { h: '-2px', h2: '-1.5px' },
    lineHeight: '1.2',
    bignumOpacity: 0.03
  },"""
if 'bittobest:' not in content:
    content = content.replace('const themes = {', f'const themes = {{{bittobest_theme}')

# 2. Replace the `.bignum` with `.watermark` inside renderSlides
content = re.sub(r'<div class="bignum">\$\{num\}</div>', r'<div class="watermark">B2B</div>', content)

# 3. Update the CSS styles for the watermark instead of bignum
watermark_css = """
  .watermark {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: var(--font-heading);
    font-weight: 900;
    font-size: 280px;
    opacity: 0.03;
    pointer-events: none;
    z-index: 1;
    color: currentColor;
  }
"""
content = re.sub(r'\.bignum\s*\{[^}]+\}', watermark_css, content, count=1)

content = re.sub(r'body\.lang-ar\s*\.bignum\s*\{[^}]+\}', '', content)
content = re.sub(r'\.slide\.dark\s*\.bignum\s*\{[^}]+\}', '', content)
content = re.sub(r'\.slide\.light\s*\.bignum\s*\{[^}]+\}', '', content)
content = re.sub(r'\.slide\.accent\s*\.bignum\s*\{[^}]+\}', '', content)

content = re.sub(r'\.bignum\s*\{[^}]+!important;\s*\}', """
    .watermark {
      font-size: 700px !important;
    }
""", content)
content = re.sub(r'body\.lang-ar\s*\.bignum\s*\{[^}]+!important;\s*\}', '', content)

# 4. Modify default apply calls
content = content.replace("applyLanguage('en');", "applyLanguage('ar');")
content = re.sub(r"applyTheme\('[^']+'\);", "applyTheme('bittobest');", content)

# 5. Gradient accent text
gradient_css = """
  .accent-text { 
    background: linear-gradient(90deg, #87CEEB, #8A2BE2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
  }
  .slide.accent .accent-text { 
    background: linear-gradient(90deg, #FFFFFF, #E0E0E0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
  }
"""
content = re.sub(r'\.accent-text\s*\{[^}]+\}', gradient_css, content, count=1)
content = re.sub(r'\.slide\.accent\s*\.accent-text\s*\{[^}]+\}', '', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Template updated")
