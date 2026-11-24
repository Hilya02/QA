from docx import Document
from docx.oxml.ns import qn
p=r'C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx'
d=Document(p)
for ti,t in enumerate(d.tables):
 print('TABLE',ti,'style',getattr(t.style,'name',None),'grid',[(int(x.get(qn('w:w')))/1440 if x.get(qn('w:w')) else None) for x in t._tbl.tblGrid.gridCol_lst])
 for ri in range(min(2,len(t.rows))):
  print('ROW',ri)
  for ci,c in enumerate(t.rows[ri].cells):
   pr=c._tc.tcPr
   shd=pr.find(qn('w:shd'))
   print(ci,'width',c.width.inches if c.width else None,'text',repr(c.text),'fill',shd.get(qn('w:fill')) if shd is not None else None,'pars',[(p.style.name if p.style else None,[(r.text,r.font.size.pt if r.font.size else None,r.bold,r.font.color.rgb if r.font.color else None) for r in p.runs]) for p in c.paragraphs])
