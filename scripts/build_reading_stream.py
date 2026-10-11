#!/usr/bin/env python3
"""Build the standalone reading stream from its template and canonical study data."""
import json
import pathlib
import runpy

ROOT = pathlib.Path(__file__).resolve().parents[1]
# Reuse the existing canonical projection, including attribution-bearing annotations.
study = runpy.run_path(str(ROOT / 'scripts/build_prototype.py'))['data']
template = (ROOT / 'app/reading-stream/template.html').read_text(encoding='utf-8')
marker = '/*__MARKUS__*/null'
assert template.count(marker) == 1
payload = json.dumps(study, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
(ROOT / 'app/reading-stream/index.html').write_text(template.replace(marker, payload), encoding='utf-8')
print('PASS: reading stream built with Markus 3:20–35 study data.')
