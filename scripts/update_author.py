
import os
import glob

posts_dir = "_posts"
search_text = "author: AI Pulse"
replace_text = "author: Sinan Koparan"

for filepath in glob.glob(os.path.join(posts_dir, "*.md")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if search_text in content:
        new_content = content.replace(search_text, replace_text)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Skipped {filepath} (author match not found)")
