from docx import Document
from pathlib import Path
import hashlib, zipfile
p=Path(r'C:\Users\HilyaNtinda\Documents\ChatGPT\AdaireDigital\StudentStay_Room_Inventory_QA_Report.docx')
d=Document(p)
print('OUTPUT',p,'bytes',p.stat().st_size,'sha256',hashlib.sha256(p.read_bytes()).hexdigest())
print('GEOMETRY',len(d.sections),[(s.page_width.inches,s.page_height.inches,s.top_margin.inches,s.bottom_margin.inches,s.left_margin.inches,s.right_margin.inches) for s in d.sections])
print('TABLES',[(len(t.rows),len(t.columns)) for t in d.tables])
for ti,t in enumerate(d.tables):
 print('TABLE',ti)
 for row in t.rows: print(' | '.join(c.text.replace('\n',' / ') for c in row.cells))
print('HEADINGS',[p.text for p in d.paragraphs if p.style and p.style.name=='Heading 1'])
print('HEADER',[p.text for p in d.sections[0].header.paragraphs])
print('FOOTER',[p.text for p in d.sections[0].footer.paragraphs])
text='\n'.join(p.text for p in d.paragraphs)+'\n'+'\n'.join(c.text for t in d.tables for r in t.rows for c in r.cells)
for v in ['INV-01','INV-02','BLK-01','BLK-02','ROOM-01','AVAIL-01','ID-01','PASS*','NOT VERIFIED','NOT ASSERTED','NOT RUN','661','647','14']:
 print('CHECK',v,v in text)
print('TEMPLATE ORIGINAL UNCHANGED HASH',hashlib.sha256(Path(r'C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx').read_bytes()).hexdigest())
print('ZIP PARTS',zipfile.ZipFile(p).namelist())
