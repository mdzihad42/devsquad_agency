import os
import re

TEMPLATE_DIR = r"f:\zihad\ss\pp\agent\devsquad_agency\templates"
CSS_FILE = r"f:\zihad\ss\pp\agent\devsquad_agency\static\css\styles.css"

replacements = [
    # Backgrounds & Cards
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-black-pure\b', r'\1-brand-bg'),
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-black-soft\b', r'\1-brand-bg'),
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-black-surface\b', r'\1-brand-card'),
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-galaxy-900\b', r'\1-brand-bg'),
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-galaxy-950\b', r'\1-brand-bg'),
    
    # Primary & Accent Colors
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-sunset-orange\b', r'\1-brand-primary'),
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-sunset-amber\b', r'\1-brand-accent'),
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-sunset-glow\b', r'\1-brand-primary'),
    
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-accent-light\b', r'\1-brand-accent'),
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-accent-dark\b', r'\1-brand-primary'),
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-accent\b', r'\1-brand-primary'),
    
    # Text White -> Text Brand
    (r'\b(bg|text|border|from|to|via|ring|shadow|divide)-white\b', r'\1-brand-text'),
    
    # Custom Shadow/RGBA values matching sunset-orange (249, 115, 22) to brand-primary (59, 130, 246)
    (r'249,\s*115,\s*22', r'59, 130, 246'),
    
    # Custom RGBA values matching sunset-amber (251, 191, 36) to brand-accent (6, 182, 212)
    (r'251,\s*191,\s*36', r'6, 182, 212'),
]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content
    for pattern, repl in replacements:
        new_content = re.sub(pattern, repl, new_content)
        
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")

for root, dirs, files in os.walk(TEMPLATE_DIR):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

if os.path.exists(CSS_FILE):
    process_file(CSS_FILE)

print("Update complete.")
