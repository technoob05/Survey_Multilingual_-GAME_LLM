import re
from collections import defaultdict

def normalize_title(title):
    if not title:
        return ""
    # Remove braces, punctuation, and whitespace, then lowercase
    return re.sub(r'[\s\W_]+', '', title.lower().strip('{}'))

def find_duplicates(bib_file):
    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex to extract entries
    entries = re.findall(r'@(\w+)\{([^,]+),([\s\S]*?)\n\}', content)
    
    titles = defaultdict(list)
    keys_by_id = {}
    
    for entry_type, key, body in entries:
        title_match = re.search(r'title\s*=\s*\{+([^}]+)\}+', body, re.IGNORECASE)
        title = title_match.group(1) if title_match else ""
        norm_title = normalize_title(title)
        if norm_title:
            titles[norm_title].append(key)
        keys_by_id[key] = (entry_type, title)

    print("Potential duplicates by title:")
    for norm_title, keys in titles.items():
        if len(keys) > 1:
            print(f"- Title: {keys_by_id[keys[0]][1]}")
            print(f"  Keys: {', '.join(keys)}")

bib_path = r'd:\Survey_Multilingual_ GAME_LLM\Association_for_Computational_Linguistics__ACL__conference__6_\latex\custom.bib'
find_duplicates(bib_path)
