import re
import os

files = ['generate_carousel.py', 'generate_tutorial_hell.py', 'generate_git_horror.py']
dir_path = '/Users/sartmhmdalmry/Desktop/carousel-creator-skill-main'

for file in files:
    filepath = os.path.join(dir_path, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove theme injections
    content = re.sub(r'aws_theme\s*=\s*\"\"\"[\s\S]*?\"\"\"', '', content)
    content = re.sub(r"content\s*=\s*content\.replace\('const themes = \{', f'const themes = \{\{\{aws_theme\}'\)", '', content)

    content = re.sub(r'sara_theme\s*=\s*\"\"\"[\s\S]*?\"\"\"', '', content)
    content = re.sub(r"content\s*=\s*content\.replace\('const themes = \{', f'const themes = \{\{\{sara_theme\}'\)", '', content)
    
    content = re.sub(r'custom_css\s*=\s*\"\"\"[\s\S]*?\"\"\"', '', content)
    content = re.sub(r"content\s*=\s*content\.replace\('</style>', f'\{custom_css\}\\n</style>'\)", '', content)

    # Change applyTheme
    content = re.sub(r"applyTheme\('[^']+'\);", "applyTheme('bittobest');", content)
    content = re.sub(r"content\s*=\s*content\.replace\(\"applyTheme\('[^']+'\);\", \"applyTheme\('[^']+'\);\"\)", "", content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Generators fixed.")
