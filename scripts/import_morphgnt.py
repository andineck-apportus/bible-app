#!/usr/bin/env python3
"""Import MorphGNT SBLGNT Mark 3:22–30 from a locally downloaded upstream file.
Usage: python scripts/import_morphgnt.py path/to/62-Mk-morphgnt.txt
"""
import collections, hashlib, json, pathlib, sys
if len(sys.argv)!=2: sys.exit(__doc__)
source=pathlib.Path(sys.argv[1]); lines=source.read_text(encoding="utf-8-sig").splitlines()
root=pathlib.Path(__file__).resolve().parents[1]
records=[]
for line in lines:
 parts=line.split()
 if len(parts)!=7: continue
 ref,pos,morph,display,surface,normalized,lemma=parts
 if not (ref.startswith("6203") and ref[4:].isdigit() and 22<=int(ref[4:])<=30): continue
 verse=int(ref[4:]);idx=sum(r["verse"]==verse for r in records)+1
 records.append({"id":f"TOK-SBLGNT-MRK-003-{verse:03d}-{idx:03d}","edition":"SBLGNT","annotation":"MorphGNT 6.12", "reference":f"MRK.3.{verse}","verse":verse,"position":idx,"pos":pos,"morphology_code":morph,"display":display,"surface":surface,"normalized":normalized,"lemma":lemma,"tags":["TAG-MARK"]})
if not records or len(set(r["verse"] for r in records))!=9: sys.exit("ERROR: missing verse(s) or unexpected input layout; no output written")
out=root/'data'/'tokens'/'SBLGNT-MRK-003-022-030.json';out.parent.mkdir(exist_ok=True)
payload={"id":"TOKSET-SBLGNT-MRK-003-022-030","source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),"tokens":records}
out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
counts=collections.Counter(r['lemma'] for r in records)
report={"edition":"SBLGNT","annotation":"MorphGNT 6.12","verses":9,"tokens":len(records),"unique_lemmas":len(counts),"lemma_counts":dict(sorted(counts.items()))}
(root/'data'/'counts').mkdir(exist_ok=True)
(root/'data'/'counts'/'SBLGNT-MRK-003-022-030.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f"Imported {len(records)} tokens, {len(counts)} lemmas across nine verses")
