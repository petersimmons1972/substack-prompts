import json,re,sys,collections
rows=[json.loads(l) for l in open('per_run.jsonl')]
def walk(o,acc):
    if isinstance(o,dict):
        t=o.get('type')
        if t in('tool_use','custom_tool_call','function_call'):
            acc.append(json.dumps(o.get('input',o.get('arguments',o))))
        for v in o.values(): walk(v,acc)
    elif isinstance(o,list):
        for v in o: walk(v,acc)
# write-target patterns: redirection, tee, Write/Edit file_path, apply_patch headers, open(...,'w'), touch, mkdir, cp/mv dest
pat=re.compile(r"(?:>>?\s*|tee\s+(?:-a\s+)?|\"file_path\":\s*\"|\*\*\* (?:Add|Update) File: |open\(\s*['\"]|touch\s+|mkdir\s+(?:-p\s+)?|mktemp[^\n]*?)(/[^\s'\"\\)]+)")
out=collections.defaultdict(list)
for r in rows:
    wd=f"runs/workdirs/{r['run_id']}"
    acc=[]
    for line in open(r['session_log']):
        try: walk(json.loads(line),acc)
        except Exception: pass
    for s in acc:
        s=s.encode().decode('unicode_escape',errors='ignore')
        for m in pat.finditer(s):
            p=m.group(1)
            if wd in p or p.startswith('/dev/'): continue
            out[r['run_id']].append(p)
        if 'mktemp' in s or 'tempfile' in s or 'TemporaryDirectory' in s: out[r['run_id']].append('<tempfile-api>')
cells=collections.Counter(); hit=collections.Counter()
for r in rows:
    k=(r['requested_model'],r['requested_effort'],r.get('arm'))
    cells[k]+=1
    if out[r['run_id']]: hit[k]+=1
for k in cells: print(k, f"{hit[k]}/{cells[k]}")
for rid,ps in out.items():
    if ps: print(rid, sorted(set(ps))[:6])
