from docx import Document
from pathlib import Path
import hashlib, zipfile
files = [Path(r'C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx'), Path(r'C:\Users\HilyaNtinda\Desktop\Student Stay\Hilya SS\StudentStay_Room_Inventory_QA_Summary.docx')]
for p in files:
    print('\n===',p,'===')
    print('size',p.stat().st_size,'sha256',hashlib.sha256(p.read_bytes()).hexdigest())
    d=Document(p)
    print('sections',len(d.sections))
    for s in d.sections: print('page',s.page_width.inches,s.page_height.inches,'margins',s.top_margin.inches,s.bottom_margin.inches,s.left_margin.inches,s.right_margin.inches)
    print('paragraphs')
    for i,x in enumerate(d.paragraphs):
        if x.text.strip(): print(f'P{i} [{getattr(x.style,"name","")}] {x.text}')
    print('tables',len(d.tables))
    for ti,t in enumerate(d.tables):
        print('TABLE',ti,'rows',len(t.rows),'cols',len(t.columns))
        for ri,r in enumerate(t.rows): print('ROW',ri,[c.text.replace('\n',' | ') for c in r.cells])
    for si,s in enumerate(d.sections): print('header',si,[x.text for x in s.header.paragraphs],'footer',[x.text for x in s.footer.paragraphs])
    z=zipfile.ZipFile(p); print('media',[n for n in z.namelist() if n.startswith('word/media/')])
