import re
import os

def get_cited_keys(tex_file):
    if not os.path.exists(tex_file):
        print(f"File not found: {tex_file}")
        return set()
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Match \cite{key1, key2}, \citep{key1}, \citet{key1}, etc.
    citations = re.findall(r'\\cite[pt]*\{([^}]+)\}', content)
    keys = set()
    for cite in citations:
        for key in cite.split(','):
            keys.add(key.strip())
    return keys

def get_bib_keys(bib_file):
    if not os.path.exists(bib_file):
        print(f"File not found: {bib_file}")
        return set()
    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Match @article{key, ...}, @inproceedings{key, ...}, etc.
    keys = re.findall(r'@\w+\{([^,]+),', content)
    return set(keys)

tex_path = r'd:\Survey_Multilingual_ GAME_LLM\Association_for_Computational_Linguistics__ACL__conference__6_\latex\acl_latex.tex'
bib_path = r'd:\Survey_Multilingual_ GAME_LLM\Association_for_Computational_Linguistics__ACL__conference__6_\latex\custom.bib'

cited = get_cited_keys(tex_path)
available = get_bib_keys(bib_path)

missing = cited - available
print("Missing keys:")
for m in sorted(missing):
    print(m)
