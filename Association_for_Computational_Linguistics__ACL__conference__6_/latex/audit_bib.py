import re
from collections import defaultdict

def parse_bib(content):
    entries = []
    # Match entries like @type{key, body}
    for match in re.finditer(r'@(\w+)\s*\{\s*([^,]+),', content):
        entry_type = match.group(1).lower()
        key = match.group(2).strip()
        
        start_pos = match.end()
        brace_count = 1
        end_pos = start_pos
        while brace_count > 0 and end_pos < len(content):
            if content[end_pos] == '{':
                brace_count += 1
            elif content[end_pos] == '}':
                brace_count -= 1
            end_pos += 1
        
        body = content[start_pos:end_pos-1]
        entries.append((key, entry_type, body))
    
    return {key: (etype, body) for key, etype, body in entries}

def normalize_title(title):
    if not title: return ""
    return re.sub(r'[\s\W_]+', '', title.lower().strip('{}'))

def audit():
    provided_path = r'd:\Survey_Multilingual_ GAME_LLM\Association_for_Computational_Linguistics__ACL__conference__6_\latex\provided_citations.bib'
    local_path = r'd:\Survey_Multilingual_ GAME_LLM\Association_for_Computational_Linguistics__ACL__conference__6_\latex\custom.bib'

    with open(provided_path, 'r', encoding='utf-8') as f:
        provided_content = f.read()
    with open(local_path, 'r', encoding='utf-8') as f:
        local_content = f.read()

    provided_entries = parse_bib(provided_content)
    local_entries = parse_bib(local_content)

    updates = []
    new_entries = []
    conflicts = []
    missing_from_provided = []

    for key, (p_type, p_body) in provided_entries.items():
        p_title_match = re.search(r'title\s*=\s*\{+([^}]+)\}+', p_body, re.IGNORECASE)
        p_title = p_title_match.group(1) if p_title_match else ""
        
        if key in local_entries:
            l_type, l_body = local_entries[key]
            l_title_match = re.search(r'title\s*=\s*\{+([^}]+)\}+', l_body, re.IGNORECASE)
            l_title = l_title_match.group(1) if l_title_match else ""

            is_l_arxiv = 'arxiv' in l_body.lower() or l_type == 'article' and 'journal' not in l_body.lower()
            is_p_arxiv = 'arxiv' in p_body.lower()
            
            if is_l_arxiv and not is_p_arxiv:
                updates.append(f"[UPDATE] {key}: ArXiv -> Published ({p_type})")
            elif p_body.strip() != l_body.strip():
                if normalize_title(p_title) == normalize_title(l_title):
                    updates.append(f"[REFINE] {key}: Details changed")
                else:
                    conflicts.append(f"[CONFLICT] {key}:\n  Local Title: {l_title}\n  Prov Title:  {p_title}")
        else:
            new_entries.append(f"[NEW] {key}: {p_title[:60]}...")

    for key in local_entries:
        if key not in provided_entries:
            missing_from_provided.append(key)

    print(f"--- MISSING FROM PROVIDED (Local only: {len(missing_from_provided)}) ---")
    print(", ".join(missing_from_provided))
    
    # Also check if any local keys are close to provided keys (potential spelling diffs)
    # TBD if needed.

if __name__ == "__main__":
    audit()
