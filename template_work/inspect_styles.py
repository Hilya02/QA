from docx import Document
from pathlib import Path
p=Path(r'C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx')
d=Document(p)
for pi in [0,1,2,3,6,7,11,12,14,17,22,32]:
    q=d.paragraphs[pi]
    print('P',pi,'alignment',q.alignment,'before',q.paragraph_format.space_before,'after',q.paragraph_format.space_after,'line',q.paragraph_format.line_spacing,'keep_next',q.paragraph_format.keep_with_next)
    for r in q.runs: print(' RUN',repr(r.text),'font',r.font.name,'size',r.font.size.pt if r.font.size else None,'bold',r.bold,'italic',r.italic,'color',r.font.color.rgb if r.font.color else None)
for ti,t in enumerate(d.tables):
    print('TABLE',ti,'style',getattr(t.style,'name',None),'autofit',t.autofit)
    for ri in range(min(2,len(t.rows))):
        row=t.rows[ri]
        print(' row',ri,'height',row.height,'cells widths',[round(c.width.inches,2) if c.width else None for c in row.cells])
        for ci,c in enumerate(row.cells):
            print('  c',ci,'text',repr(c.text),'shade',c._tc.tcPr.shd.fill if c._tc.tcPr.shd is not None else None,'borders?',bool(c._tc.tcPr.tcBorders))
