#!/usr/bin/env python3
"""Import MorphGNT Mark 3:22–30 from a locally supplied upstream file.
Run: python scripts/import_morphgnt.py /path/to/62-Mk-morphgnt.txt
No network access; never substitutes fabricated verses.
"""
import collections, hashlib, json, pathlib, re, sys
if len(sys.argv) != 2: sys.exit(__doc__)
source = pathlib.Path(sys.argv[1])
if not source.is_file(): sys.exit("ERROR: input file missing")
root = pathlib.Path(__file__).resolve().parents[1]
records=[]; verse_counts=collections.Counter(); bad=[]
for line_number,line in enumerate(source.read_text(encoding="utf-8-sig").splitlines(),1):
    parts=line.split()
    if not parts: continue
    ref=parts[0]
    if not re.fullmatch(r"6203(?:2[2-9]|30)",ref): continue
    if len(parts)!=7:
        bad.append(line_number);continue
    ref,pos,morph,display,surface,normalized,lemma=parts
    verse=int(ref[-2:]);verse_counts[verse]+=1;idx=verse_counts[verse]
    records.append({"id":f"TOK-SBLGNT-MRK-003-{verse:03d}-{idx:03d}","edition":"ED-SBLGNT","annotation":"MorphGNT", "reference":f"MRK.3.{verse}","verse":verse,"position":idx,"pos":pos,"morphology_code":morph,"display":display,"surface":surface,"normalized":normalized,"lemma":lemma,"tags":["TAG-MARK"]})
if bad:sys.exit(f"ERROR: malformed rows at lines {bad[:10]}; no output written")
if set(verse_counts)!=set(range(22,31)):sys.exit(f"ERROR: missing verses {sorted(set(range(22,31))-set(verse_counts))}; no output written")
sha=hashlib.sha256(source.read_bytes()).hexdigest()
payload={"id":"TOKSET-SBLGNT-MRK-003-022-030","type":"token_set","status":"imported_unreviewed","tags":["TAG-MARK"],"edition":"ED-SBLGNT","annotation":"MorphGNT","source_sha256":sha,"tokens":records}
counts=collections.Counter(r['lemma'] for r in records)
report={"id":"COUNT-SBLGNT-MRK-003-022-030","type":"lemma_count","status":"imported_unreviewed","tags":["TAG-MARK"],"edition":"ED-SBLGNT","annotation":"MorphGNT","source_sha256":sha,"verse_count":9,"token_count":len(records),"unique_lemmas":len(counts),"lemma_counts":dict(sorted(counts.items()))}
for folder,name,obj in [('tokens','SBLGNT-MRK-003-022-030.json',payload),('counts','SBLGNT-MRK-003-022-030.json',report)]:
    target=root/'data'/folder/name;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f"PASS: imported {len(records)} tokens / {len(counts)} lemmas, sha256={sha}")
