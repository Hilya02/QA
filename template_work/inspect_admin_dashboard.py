from docx import Document
from pathlib import Path
import hashlib, zipfile
p=Path(r'C:\Users\HilyaNtinda\Downloads\Admin user dashboard updated.docx')
print('SOURCE',p,'exists',p.exists(),'size',p.stat().st_size if p.exists() else None)
print('SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
d=Document(p)
print('SECTIONS',len(d.sections))
for s in d.sections: print('PAGE',s.page_width.inches,s.page_height.inches,'MARGINS',s.top_margin.inches,s.bottom_margin.inches,s.left_margin.inches,s.right_margin.inches)
print('PARAGRAPHS')
for i,p in enumerate(d.paragraphs):
    if p.text.strip(): print(f'P{i} [{getattr(p.style,"name","")}] {p.text}')
print('TABLES',len(d.tables))
for ti,t in enumerate(d.tables):
    print('TABLE',ti,'rows',len(t.rows),'cols',len(t.columns))
    for ri,row in enumerate(t.rows): print('ROW',ri,[c.text.replace('\n',' | ') for c in row.cells])
for si,s in enumerate(d.sections): print('HEADER',si,[p.text for p in s.header.paragraphs],'FOOTER',[p.text for p in s.footer.paragraphs])
print('MEDIA',[n for n in zipfile.ZipFile(p).namelist() if n.startswith('word/media/')])
