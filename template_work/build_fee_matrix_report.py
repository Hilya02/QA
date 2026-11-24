from copy import deepcopy
from pathlib import Path
from collections import Counter
from openpyxl import load_workbook
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import hashlib, shutil

SOURCE=Path(r'C:\Users\HilyaNtinda\Downloads\Student_Accommodation_Fee_Test_Matrix 1.xlsx')
TEMPLATE=Path(r'C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx')
OUTPUT=Path(r'C:\Users\HilyaNtinda\Documents\ChatGPT\AdaireDigital\StudentStay_Fee_Matrix_QA_Report_2026-11-17.docx')
EXPECTED_TEMPLATE_HASH='875c23459cda5b607f5c43290c5e060ae32fcbfbb0e1774e4807d80cbf90b67c'
if hashlib.sha256(TEMPLATE.read_bytes()).hexdigest()!=EXPECTED_TEMPLATE_HASH:
    raise RuntimeError('The retained QA template changed; re-distill before editing.')

# Read-only extraction. The source workbook is not modified.
wb=load_workbook(SOURCE,read_only=True,data_only=False)
ws=wb['Test Matrix']
headers=[c.value for c in ws[1]]
idx={name:i for i,name in enumerate(headers)}
required=['Test ID','Property','Applicant Origin','Applicant Type','Room','Term (months)','Rate Tier','Exp. Application Fee','Exp. Deposit','Exp. Monthly Rent','Result']
if any(name not in idx for name in required): raise RuntimeError('Unexpected Test Matrix headers.')
rows=[]
for raw in ws.iter_rows(min_row=2,values_only=True):
    if raw[idx['Test ID']] is None: continue
    rows.append({name:raw[idx[name]] for name in required})
wb.close()
if len(rows)!=48: raise RuntimeError(f'Expected 48 populated source IDs, found {len(rows)}')
counts=Counter(r['Property'] for r in rows)
if counts!=Counter({'Mercury House':24,'Villa Verdi':24}): raise RuntimeError(f'Unexpected property case counts: {counts}')
if any(r['Exp. Application Fee'] is None or r['Exp. Deposit'] is None or r['Exp. Monthly Rent'] is None for r in rows):
    raise RuntimeError('An expected fee, deposit or rent value is missing.')
rows.sort(key=lambda r:r['Test ID'])
mercury=[r for r in rows if r['Property']=='Mercury House']
villa=[r for r in rows if r['Property']=='Villa Verdi']

shutil.copy2(TEMPLATE,OUTPUT)
doc=Document(OUTPUT)
def set_text(p,text):
    if p.runs:
        p.runs[0].text=text
        for run in p.runs[1:]: run.text=''
    else: p.add_run(text)
def amount(v):
    return f'{int(v):,}' if float(v).is_integer() else f'{v:,.2f}'
def row_test(r):
    scenario=f"{r['Applicant Origin']} / {r['Applicant Type']} / {r['Room']} / {r['Term (months)']} mo"
    expected=f"Fee {amount(r['Exp. Application Fee'])}; deposit {amount(r['Exp. Deposit'])}; rent {amount(r['Exp. Monthly Rent'])}/mo"
    return [r['Test ID'],scenario,expected,'PASS']

paragraphs={
  1:'Quality Assurance Test Report',
  2:'Student Stay',
  3:'Rental Fee Matrix Retest',
  6:'1. Executive Summary',
  7:'This report records the Student Stay accommodation fee matrix retest dated 17 November 2026. All 48 populated test cases in the source matrix are reported as passed. Testing covers Mercury House and Villa Verdi across the listed applicant origins, applicant types, room types, and lease terms.',
  8:'Each case compares the expected application fee, deposit, and monthly rent for one property and applicant scenario. The expected amounts in the tables below are copied from the source matrix. No currency is stated in that workbook.',
  9:'The cases are grouped by property so the 48 recorded test IDs can be reviewed against their expected amounts. The report is marked Internal and Client ready Yes.',
  10:'The workbook notes describe a 72-case design, but only 48 test IDs are populated in the matrix. The missing scenarios are identified in Scope and Limitations.',
  11:'2. Status at a Glance',
  12:'Status definition. PASS: the case was performed and passed, as confirmed for this report. Amounts shown are the expected fee, deposit, and monthly rent from the source matrix.',
  13:'All 48 populated IDs are marked PASS in this report: 24 for Mercury House and 24 for Villa Verdi. The source workbook does not contain recorded actual values for comparison.',
  14:'3. Mercury House Fee Test Results',
  15:'4. Villa Verdi Fee Test Results',
  16:'5. Pricing Rules and Coverage',
  17:'The source matrix defines the following pricing relationships and scenario dimensions.',
  18:'Application fees vary by property and by whether the applicant is new or returning.',
  19:'Deposits vary by room type. The expected fee, deposit, and rent for each recorded scenario appear beside its test ID.',
  20:'The source note says the Foreign rate tier applies to both African and Non-African applicants and that both origins should return identical amounts.',
  21:'The listed cases vary lease terms across 12, 11, and 10 months, with Single and Shared room options.',
  22:'6. Readiness and Follow-up',
  23:'All 48 populated cases are reported passed, with no failed cases reported for those IDs.',
  24:'Distribution is Internal. Client ready is Yes, as requested.',
  25:'The expected values in this report are shown without a currency symbol because the source matrix does not specify currency.',
  26:'The workbook notes refer to a 72-case design. The additional 24 case rows are not populated in the attached matrix.',
  27:'The source workbook does not record actual fee, deposit, or rent values for the runs; the PASS status is based on the test completion confirmation provided for this report.',
  28:'The source Result formulas contain broken references, so this report records the supplied pass outcome directly rather than using those formula results.',
  29:'7. Scope and Limitations',
  30:'Source reviewed: Student_Accommodation_Fee_Test_Matrix 1.xlsx, Test Matrix and Summary & Notes sheets. The Test Matrix contains 48 populated IDs: TC-001 to TC-024 for Mercury House and TC-037 to TC-060 for Villa Verdi. The Summary & Notes sheet describes 72 cases and mentions African and Non-African applicants, but 24 corresponding rows are not present (TC-025 to TC-036 and TC-061 to TC-072). Result formulas in the populated rows contain #REF! references, and the workbook has no separate actual-value fields. The report marks the 48 populated cases PASS based on the execution outcome provided by Hilya T Ntinda. Expected amounts are reproduced from the workbook; currency is not specified.',
  32:'Prepared by Hilya T Ntinda, Adaire.'
}
for i,t in paragraphs.items(): set_text(doc.paragraphs[i],t)
doc.paragraphs[14].paragraph_format.page_break_before=True
doc.paragraphs[15].paragraph_format.page_break_before=True
for i in (14,15,16,22,29): doc.paragraphs[i].paragraph_format.keep_with_next=True

metadata=[
 ['Field','Detail','Field','Detail'],
 ['System','Student Stay','Report type','Accommodation Fee Matrix QA'],
 ['Modules tested','Rental pricing matrix','Test status','48 passed; no failures reported'],
 ['Prepared by','Hilya T Ntinda','Date','17 November 2026'],
 ['Distribution','Internal','Client ready','Yes'],
]
summary=[
 ['Property','Recorded cases','Passed','Failed','Status'],
 ['Mercury House','24','24','0','PASS'],
 ['Villa Verdi','24','24','0','PASS'],
 ['Total','48','48','0','PASS'],
]

def replace_table(table,data,widths):
    while len(table.rows)<len(data):
        new_index=len(table.rows)
        template_index=1 if new_index%2 else min(2,len(table.rows)-1)
        table._tbl.append(deepcopy(table.rows[template_index]._tr))
    while len(table.rows)>len(data): table._tbl.remove(table.rows[-1]._tr)
    table.autofit=False
    for ci,w in enumerate(widths): table.columns[ci].width=Inches(w)
    for ri,values in enumerate(data):
        row=table.rows[ri]
        for ci,value in enumerate(values):
            cell=row.cells[ci]
            cell.width=Inches(widths[ci])
            p=cell.paragraphs[0]
            set_text(p,str(value))
            p.alignment=WD_ALIGN_PARAGRAPH.CENTER if ci in (0,len(values)-1) else WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.size=Pt(9.5)
                if ri==0:
                    run.bold=True
                    run.font.color.rgb=RGBColor(255,255,255)
        if ri==0:
            trPr=row._tr.get_or_add_trPr()
            if trPr.find(qn('w:tblHeader')) is None: trPr.append(OxmlElement('w:tblHeader'))

replace_table(doc.tables[0],metadata,[1.53,1.67,1.53,1.77])
replace_table(doc.tables[1],summary,[1.75,1.15,0.85,0.85,1.65])
header=['Test ID','Scenario','Expected fee / deposit / rent','Status']
replace_table(doc.tables[2],[header]+[row_test(r) for r in mercury],[0.70,2.10,3.05,0.65])
replace_table(doc.tables[3],[header]+[row_test(r) for r in villa],[0.70,2.10,3.05,0.65])
for sec in doc.sections:
    if sec.header.paragraphs: set_text(sec.header.paragraphs[0],'Adaire  |  Student Stay Fee Matrix QA  |  Internal')
doc.core_properties.title='Student Stay Accommodation Fee Matrix QA Report'
doc.core_properties.subject='Accommodation pricing test matrix retest dated 17 November 2026'
doc.core_properties.author='Hilya T Ntinda'
doc.save(OUTPUT)
print('WROTE',OUTPUT,'BYTES',OUTPUT.stat().st_size,'SHA256',hashlib.sha256(OUTPUT.read_bytes()).hexdigest())
print('CASE_COUNTS',dict(counts),'TOTAL',len(rows))
print('ID_FIRST_LAST',rows[0]['Test ID'],rows[-1]['Test ID'])
print('MERCURY_SAMPLE',row_test(mercury[0]))
print('VILLA_SAMPLE',row_test(villa[0]))
