from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
records = []
for path in sorted((root / 'data').rglob('*.json')):
    record = json.loads(path.read_text(encoding='utf-8'))
    assert all(k in record for k in ('id','type','status','tags')), path
    assert len(record['tags']) == len(set(record['tags'])), path
    records.append(record)
ids = [r['id'] for r in records]
assert len(ids) == len(set(ids)), 'Duplicate IDs'
tags = {r['id'] for r in records if r['type'] == 'tag'}
for r in records:
    assert set(r['tags']) <= tags, f"Unknown tags in {r['id']}"
print(f'PASS: {len(records)} records, {len(tags)} defined tags, unique IDs and valid tag references')
