import os
import glob
import re

dir_path = '/Users/sartmhmdalmry/Desktop/carousel-creator-skill-main'

# Replace branding in all text files
for ext in ['*.md', '*.py', '*.html']:
    for filepath in glob.glob(os.path.join(dir_path, ext)):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace names
        content = content.replace("BitToBest", "BitToBest")
        content = content.replace("BitToBest", "BitToBest")
        content = content.replace("BitToBest", "BitToBest")
        content = content.replace("BitToBest_Carousels.zip", "BitToBest_Carousels.zip")
        content = content.replace("منشورات_BitToBest_المهندسة.zip", "BitToBest_Carousels.zip")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Brand names replaced globally.")
