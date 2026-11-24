from docx import Document
import zipfile
p = r'C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx'
d = Document(p)
print('BODY:')
for i, x in enumerate(d.paragraphs):
    if x.text.strip(): print(i, repr(x.text), getattr(x.style, 'name', '(no style)'))
print('TABLES', len(d.tables))
for ti, t in enumerate(d.tables):
    print('TABLE', ti, 'rows', len(t.rows), 'cols', len(t.columns))
    for ri, row in enumerate(t.rows): print('ROW', ri, [c.text.replace('\n', ' | ') for c in row.cells])
print('HEADER/FOOTER')
for si, s in enumerate(d.sections):
    print('H', si, [p.text for p in s.header.paragraphs])
    print('F', si, [p.text for p in s.footer.paragraphs])
print('PARTS', zipfile.ZipFile(p).namelist())
