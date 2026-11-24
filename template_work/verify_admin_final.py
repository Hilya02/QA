from docx import Document
from pathlib import Path
from zipfile import ZipFile
import hashlib
p=Path(r'C:\Users\HilyaNtinda\Documents\ChatGPT\AdaireDigital\StudentStay_Admin_Dashboard_QA_Report_2026-11-11.docx')
d=Document(p)
all_text='\n'.join(x.text for x in d.paragraphs)+'\n'+'\n'.join(c.text for t in d.tables for row in t.rows for c in row.cells)
statuses=[]
for ti in (2,3):
    t=d.tables[ti]
    statuses.extend(row.cells[2].text for row in t.rows[1:])
print('FILE',p,'SIZE',p.stat().st_size,'SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
print('PAGE',d.sections[0].page_width.inches,d.sections[0].page_height.inches,'MARGINS',d.sections[0].top_margin.inches,d.sections[0].bottom_margin.inches,d.sections[0].left_margin.inches,d.sections[0].right_margin.inches)
print('TABLE SHAPES',[(len(t.rows),len(t.columns)) for t in d.tables])
print('TOTAL CHECKS',len(statuses),'ALL PASS',all(x=='PASS' for x in statuses),'MEDIA',sum(n.startswith('word/media/') for n in ZipFile(p).namelist()))
print('KEY TEXT',[(x,x in all_text) for x in ['Hilya T Ntinda','Distributor (client)','11 November 2026','28 passed','Ready for client review']])
print('NO FAILURE LABELS',not any(x.lower() in all_text.lower() for x in ['Not done','Blocked','Failed']))
print('TEMPLATE HASH',hashlib.sha256(Path(r'C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx').read_bytes()).hexdigest())
