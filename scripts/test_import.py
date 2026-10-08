"""Offline importer smoke tests using synthetic tokens (NOT biblical source data)."""
from pathlib import Path
import tempfile,subprocess,sys,shutil,json
root=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as temp:
    sandbox=Path(temp)/'repo';(sandbox/'scripts').mkdir(parents=True)
    shutil.copy(root/'scripts/import_morphgnt.py',sandbox/'scripts/import_morphgnt.py')
    source=Path(temp)/'fixture.txt'
    source.write_text(''.join(f'6203{v:02d} N- ---- ΔΟΚΙΜΗ ΔΟΚΙΜΗ ΔΟΚΙΜΗ δοκιμή\n' for v in range(22,31)),encoding='utf-8')
    result=subprocess.run([sys.executable,str(sandbox/'scripts/import_morphgnt.py'),str(source)],capture_output=True,text=True)
    assert result.returncode==0,(result.stdout,result.stderr)
    data=json.loads((sandbox/'data/tokens/SBLGNT-MRK-003-022-030.json').read_text())
    assert len(data['tokens'])==9
    assert len(data['source_sha256'])==64
    source.write_text('620322 N- ---- ΔΟΚΙΜΗ ΔΟΚΙΜΗ ΔΟΚΙΜΗ δοκιμή\n',encoding='utf-8')
    result=subprocess.run([sys.executable,str(sandbox/'scripts/import_morphgnt.py'),str(source)],capture_output=True,text=True)
    assert result.returncode!=0
print('PASS: synthetic importer smoke tests (complete input, incomplete input rejected)')
