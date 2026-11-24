from pathlib import Path
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import hashlib, shutil

TEMPLATE=Path(r'C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx')
SOURCE=Path(r'C:\Users\HilyaNtinda\Desktop\Student Stay\Hilya SS\Studentspace user dashboard - updated feedback.docx')
OUTPUT=Path(r'C:\Users\HilyaNtinda\Documents\ChatGPT\AdaireDigital\StudentStay_Student_Portal_Feedback_QA_Report_2026-11-23.docx')
EXPECTED_TEMPLATE_HASH='875c23459cda5b607f5c43290c5e060ae32fcbfbb0e1774e4807d80cbf90b67c'
if hashlib.sha256(TEMPLATE.read_bytes()).hexdigest()!=EXPECTED_TEMPLATE_HASH:
    raise RuntimeError('Template changed; review before building.')
if not SOURCE.exists(): raise FileNotFoundError(SOURCE)

cases=[
('STU-01','Social media source options','Source selection offers named channels such as Facebook, TikTok, and Instagram for application attribution.'),
('STU-02','Student-count claim on landing page','The unverified “1.3K students” claim was updated as requested.'),
('STU-03','Wording on related application screen','The opening phrase on the related screen was updated.'),
('STU-04','Related screen wording and student-count claim','The wording and “1.3K” reference on the additional screen were updated.'),
('STU-05','Applicant application archive control','Applicants no longer have an option to archive an application.'),
('STU-06','Current dates and prices','Displayed dates and prices reflect the updated information.'),
('STU-07','Application submission destination','The submission destination and handling were confirmed and updated per the client feedback.'),
('STU-08','Accommodation wording','The wording reflects the available male and female accommodation arrangement.'),
('STU-09','Residence choice wording','The related screen no longer implies a choice among unavailable residences.'),
('STU-10','Applicant category options','Applicant category options are Local Students and Foreign Students.'),
('STU-11','Move-in and move-out date validation','Move-out date is not requested; move-in date cannot be later than the contract start date.'),
('STU-12','Applicant category labels in application','The application uses Local Students and Foreign Students.'),
('STU-13','Date of birth eligibility range','Date of birth selection is limited to the allowed age range of 18–32.'),
('STU-14','Cell phone number and country validation','The field is labelled Cell phone number and a country must be selected before continuing.'),
('STU-15','Study year options','Study year options begin at the current year and update as agreed for subsequent years.'),
('STU-16','Study Faculty and Study Program selection','Study Faculty and Study Program can be selected from the requested lists.'),
('STU-17','FAQ content and placement','The FAQ content and placement were updated to suit the application flow.'),
('STU-18','Room preference choices','Obsolete residence options were removed; room preferences reflect Mercury House and Villa Verdi.'),
('STU-19','Income and expense form and document completion','The income and expense sheet can be opened, edited, and saved; applicants cannot continue with required documents missing.'),
('STU-20','Required document indicators','All listed documents are marked as required rather than optional.'),
('STU-21','Application fee payment instructions','Instructions identify the non-refundable application fee, reference format, and correct bank payment information.'),
('STU-22','Application fee amount and payment details','The fee is shown as N$1,000, non-refundable; the approved test-payment details and bank information are displayed, with guidance not to make a bank transfer.'),
]

def set_text(p,text):
    if p.runs:
        p.runs[0].text=text
        for run in p.runs[1:]: run.text=''
    else: p.add_run(text)

shutil.copy2(TEMPLATE,OUTPUT)
doc=Document(OUTPUT)
paras={
1:'Quality Assurance Test Report', 2:'Student Stay', 3:'Student Portal Client Feedback Retest',
6:'1. Executive Summary',
7:'This report records QA retesting of the Student Stay student portal feedback documented by the client. The client-raised items listed in the source feedback document have been resolved and tested. All 22 checks in this report passed, as confirmed by QA for client review.',
8:'Coverage includes portal wording and marketing claims, application controls, accommodation and room preferences, student eligibility and profile fields, study selections, document requirements, and application fee instructions.',
9:'The source document contains “Not done” notes that no longer reflect the final state. For this report, the final outcome follows the supplied QA confirmation: every listed client issue has been resolved and passed.',
10:'The source feedback document does not include a separate execution log or actual-versus-expected results. The report records the completed pass outcome provided for this retest and retains the client feedback as the basis for each check.',
11:'2. Status at a Glance',
12:'Status definition. PASS: the client-raised requirement was retested and passed, based on QA completion confirmation from Hilya T Ntinda.',
13:'A total of 22 client feedback checks passed. No failed or blocked checks are reported. The report is ready for client review.',
14:'3. Portal Content and Application Flow Results',
15:'4. Applicant Details, Documents, and Payment Results',
16:'5. Overall Findings',
17:'The retest confirms that the client feedback recorded in the source document has been addressed and passed in QA.',
18:'Portal wording, social media attribution options, student-count claims, and accommodation descriptions were updated to reflect the agreed content.',
19:'Application controls and validations cover archiving, applicant categories, move-in and move-out dates, age eligibility, contact details, and study selections.',
20:'Room preferences, document requirements, the editable income and expense sheet, and application fee guidance were included in the retest.',
21:'All 22 checks are marked PASS and the report is ready for client review.',
22:'6. Client Review Readiness',
23:'All 22 client feedback checks passed QA. The report is ready for client review.',
24:'No failed or blocked checks are reported for the listed scope.',
25:'Client-raised issues are presented in the results tables with their retest status.',
26:'QA completed by Hilya T Ntinda.',
27:'The “Not done” labels in the source are treated as outdated status notes in light of the supplied final QA confirmation.',
28:'No additional open items were identified in the supplied completion update.',
29:'7. Scope and Evidence',
30:'Source reviewed: Studentspace user dashboard - updated feedback.docx. The report covers 22 distinct feedback checks extracted from the document. Some comments combine related requirements and are represented as a single test case. The source document includes stale “Not done” labels; the final PASS statuses are based on the user’s confirmation that all listed client bugs were resolved and QA tested. The source file does not contain a separate execution log or recorded actual values. Client review status: Ready. QA completed by: Hilya T Ntinda. Report date: 23 November 2026.',
32:'QA completed by Hilya T Ntinda, Adaire.'
}
for i,t in paras.items(): set_text(doc.paragraphs[i],t)
for i in (14,15): doc.paragraphs[i].paragraph_format.page_break_before=True
for i in (14,15,16,22,29): doc.paragraphs[i].paragraph_format.keep_with_next=True

metadata=[
['Field','Detail','Field','Detail'],
['System','Student Stay','Report type','Student Portal Feedback Retest'],
['Modules tested','Student portal application flow','Test status','22 passed; client review'],
['QA completed by','Hilya T Ntinda','Date','23 November 2026'],
['Distribution','Client review','Client ready','Yes'],
]
summary=[
['Test area','Checks','Passed','Failed','Status'],
['Portal content and application flow','11','11','0','PASS'],
['Applicant details, documents, and payment','11','11','0','PASS'],
['Total','22','22','0','Ready for client review'],
]

def replace_table(table,data,widths):
    while len(table.rows)<len(data):
        ix=len(table.rows)
        template_ix=1 if ix%2 else min(2,len(table.rows)-1)
        table._tbl.append(__import__('copy').deepcopy(table.rows[template_ix]._tr))
    while len(table.rows)>len(data): table._tbl.remove(table.rows[-1]._tr)
    table.autofit=False
    for ci,w in enumerate(widths): table.columns[ci].width=Inches(w)
    for ri,values in enumerate(data):
        for ci,value in enumerate(values):
            cell=table.rows[ri].cells[ci]; cell.width=Inches(widths[ci])
            p=cell.paragraphs[0]; set_text(p,str(value))
            p.alignment=WD_ALIGN_PARAGRAPH.CENTER if ci in (0,len(values)-1) else WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.size=Pt(9.5)
                if ri==0: run.bold=True; run.font.color.rgb=RGBColor(255,255,255)
        if ri==0:
            trPr=table.rows[ri]._tr.get_or_add_trPr()
            if trPr.find(qn('w:tblHeader')) is None: trPr.append(OxmlElement('w:tblHeader'))

replace_table(doc.tables[0],metadata,[1.53,1.67,1.53,1.77])
replace_table(doc.tables[1],summary,[1.75,1.15,0.85,0.85,1.65])
headers=['Test ID','Client feedback / test case','Retest result','Status']
def report_row(case):
    case_id,title,requirement=case
    return [case_id,f'{title}: {requirement}','Resolved and QA tested.','PASS']
replace_table(doc.tables[2],[headers]+[report_row(c) for c in cases[:11]],[0.72,2.55,2.55,0.68])
replace_table(doc.tables[3],[headers]+[report_row(c) for c in cases[11:]],[0.72,2.55,2.55,0.68])
for sec in doc.sections:
    if sec.header.paragraphs: set_text(sec.header.paragraphs[0],'Adaire  |  Student Stay Student Portal QA  |  Client Review')
doc.core_properties.title='Student Stay Student Portal Client Feedback QA Report'
doc.core_properties.subject='Retest of client-raised student portal feedback; 22 cases passed'
doc.core_properties.author='Hilya T Ntinda'
doc.save(OUTPUT)
print('WROTE',OUTPUT,'BYTES',OUTPUT.stat().st_size,'SHA256',hashlib.sha256(OUTPUT.read_bytes()).hexdigest())
print('TEST_CASES',len(cases),'TABLE_COUNTS',[len(t.rows) for t in Document(OUTPUT).tables])
