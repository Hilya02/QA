from pathlib import Path
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import hashlib, shutil

TEMPLATE=Path(r'C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx')
OUTPUT=Path(r'C:\Users\HilyaNtinda\Documents\ChatGPT\AdaireDigital\StudentStay_Jira_Assigned_Tasks_QA_Report_2026-11-23.docx')
EXPECTED='875c23459cda5b607f5c43290c5e060ae32fcbfbb0e1774e4807d80cbf90b67c'
if hashlib.sha256(TEMPLATE.read_bytes()).hexdigest()!=EXPECTED: raise RuntimeError('Template hash changed')

# Entries contain the issue summary and Hilya's most relevant QA comment/result recovered from Jira.
# Comment/status conflicts are kept explicit; Jira workflow status is not treated as a test pass.
done=[
('ACSS-269','[SSQA-10] Document access, previews, downloads and exposed secrets','Document Review Submission: fixed, retested and passed; detailed retest steps recorded.'),
('ACSS-310','Next of Kin Age Limit','Resolved.'),
('ACSS-304','Fix the FAQ','PASS; FAQ accordion and admin configuration tested successfully.'),
('ACSS-307','Property Management broken logo/image display on staff cards','PASS; staff card images render correctly.'),
('ACSS-294','Remove old residence room offers','PASS; outdated offers removed.'),
('ACSS-292','Application fee: 1000 new / 500 returning','PASS.'),
('ACSS-295','Payslip mandatory','PASS.'),
('ACSS-296','Income/Expense sheet mandatory','PASS.'),
('ACSS-297','Income/Expense template download, fill and upload instructions','PASS; clear instructions confirmed.'),
('ACSS-293','Study field picker in application','PASS.'),
('ACSS-303','Remove archive option and toggle','PASS.'),
('ACSS-331','Contract Length Add not working','Contract length can be added and removed.'),
('ACSS-329','Grammar on Profile','Resolved.'),
('ACSS-319','Admin Email and admin logs','Done.'),
('ACSS-332','Room assignment for all tenants','Fixed.'),
('ACSS-313','Admin Audience statistics','PASS.'),
('ACSS-325','Admin Application wording settings','Retest done; email contract template is under Configurations > Application > Automatic wording > E-mail.'),
('ACSS-323','Admin edit application room preference','Room can be changed; change recorded.'),
('ACSS-321','Admin remove obsolete choices','PASS; obsolete ID choices no longer available for new submissions; historical records retained.'),
('ACSS-318','Admin Tenant identification and allocation display','Task done; comment refers to student ID and pending capture, so completion evidence is partial.'),
('ACSS-278','[SSQA-19] Xero sandbox sync account mapping','QA Status: QA Done; Testing Status: Passed.'),
('ACSS-283','Bug 4: proof-of-payment upload card overflow','Resolved.'),
('ACSS-272','[SSQA-13] Review verdicts, comments and validation','QA Status: QA Done; Testing Status: Passed.'),
('ACSS-301','Social media options signup','PASS; Facebook, TikTok and Instagram added.'),
('ACSS-302','Auth page >1.3k wording','PASS; promotional copy updated and student stats removed.'),
('ACSS-289','Move-in/out dates','PASS; move-in constrained to contract date and move-out removed.'),
('ACSS-290','DOB limit','PASS; ages 18–32 enforced.'),
('ACSS-312','Admin Dashboard support statistics','PASS.'),
('ACSS-315','Admin Property staff cards','Resolved.'),
('ACSS-314','Admin Navigation','No explicit QA result in Hilya’s latest non-empty comment.'),
('ACSS-322','Admin correct 2027 fee matrices','Jira is Done; the latest thread comment asks partial pass?; pass status is not confirmed.'),
('ACSS-330','Align X on Configuration','Resolved.'),
('ACSS-298','Correct wording on application fee step','Resolved.'),
('ACSS-306',"Remove Let's find your home near X",'No explicit QA result recorded in the latest visible comment.'),
('ACSS-299','Auto-generate EFT reference','PASS; selected reference ID/student number/full name displayed per instructions.'),
('ACSS-270','[SSQA-11] Application fee, credit checks and finance handoff','QA Done; Testing Passed.'),
('ACSS-287','Bug 2: short-term rental application confirmation email','Resolved.'),
('ACSS-285','Start application button not working','Resolved.'),
('ACSS-268','[SSQA-09] Admin queues/counts/filters/expiry dashboard','QA Done; Testing Passed.'),
('ACSS-267','[SSQA-08] Student draft/progress/resume/submitted behavior','QA Done; Testing Passed.'),
('ACSS-266','[SSQA-07] Terms/privacy/submission consent','Comment says the checkbox is now checked on entry; explicit PASS not recorded.'),
('ACSS-265','[SSQA-06] Safe uploads and useful validation','QA Done; Testing Passed.'),
('ACSS-264','[SSQA-05] Required docs/funding paths/retained uploads','QA Done; Testing Passed, with minor issues noted.'),
('ACSS-263','[SSQA-04] Kin, medical aid, guarantor and age-policy fields','Comment says guardian was added to next of kin/medical aid; no explicit PASS.'),
('ACSS-262','[SSQA-03] Applicant type, identity and immigration requirements','Comment reports the missing nationality error appearing four times.'),
('ACSS-261','[SSQA-02] Personal and academic data validation/reference lists','Two test cases recorded PASS; overall QA status PASS.'),
('ACSS-286','Bug 1: Create Short-Term Rental Application (UI Issues)','Jira is Done, but Hilya commented that this task is still pending; linked fix was ACSS-287.'),
('ACSS-300','Remove unnecessary text in application fee section','Comments request removing point 3; no explicit QA result captured.'),
('ACSS-273','[SSQA-14] Real contract templates, generation and delivery preparation','Hilya’s comment says “QA” and includes screenshots; no explicit PASS in comment text.'),
('ACSS-320','Admin: Configuration layout and lists','Jira status is Done; no separate detailed Hilya QA result was recovered in the extracted comment text.'),
('ACSS-280','Jira issue with no comments in returned Jira data','No comment returned by Jira.'),
('ACSS-282','Jira issue with no comments in returned Jira data','No comment returned by Jira.'),
('ACSS-281','Jira issue with no comments in returned Jira data','No comment returned by Jira.'),
]
review=[
('ACSS-305','Contact support form','Latest Hilya update: Resolved. Earlier QA note recorded partial pass and a failed email-details finding; closure comment does not explicitly state retest PASS.'),
('ACSS-316','Admin: Pushes to Xero','Latest Hilya comment: “Not working.” QA remains open.'),
('ACSS-309','Bug: Incorrect Placeholder Text for Passport Number Field','Hilya recorded PASS after correction (“Fixed”); issue remains in Jira Review.'),
('ACSS-311','Contract Renewal Flow','Comment contains a broad renewal workflow test checklist. No explicit final PASS visible in the latest extracted text.'),
('ACSS-326','Admin: Payment amounts and finalisation','No explicit QA outcome was confirmed in the retrieved comment text.'),
('ACSS-324','Admin: Review and standard decisions','No explicit QA outcome was confirmed in the retrieved comment text.'),
('ACSS-291','Fix country code in the phone number input','No explicit QA outcome was confirmed in the retrieved comment text.'),
('ACSS-288','Consolidate African and Non-African into Foreign','No explicit QA outcome was confirmed in the retrieved comment text.'),
('ACSS-271','[SSQA-12] Editable rental defaults, independent deposits and payment records','No explicit final PASS was confirmed in the retrieved comment text.'),
('ACSS-317','Admin: Bed totals and labels',"Hilya's latest visible note says still pending; follow-up asks whether anything is needed from Hilya."),
('ACSS-328','Admin Dashboard Alignment of Tabs',"Hilya's comments report remaining pending differences in font color/size, spacing, and layout."),
]

def set_text(p,text):
    if p.runs:
        p.runs[0].text=text
        for r in p.runs[1:]: r.text=''
    else: p.add_run(text)

shutil.copy2(TEMPLATE,OUTPUT)
doc=Document(OUTPUT)
para={
1:'Quality Assurance Test Report',2:'Student Stay',3:'Jira Assigned Tasks – Done and QA Review',
6:'1. Executive Summary',
7:'This report consolidates ACSS Jira tasks assigned to Hilya T Ntinda that are in Done or appear in the board’s QA-Testing column. Jira records the QA-column items with status “Review.” The report includes issue keys, direct Jira links, Hilya’s QA comments where available, and any test result stated in those comments.',
8:'Scope captured 23 November 2026: 53 issues in Jira status Done and 11 issues in Jira status Review (shown in the board’s QA-Testing lane). All assigned issues are listed, including three Done issues for which the returned Jira data had no comment.',
9:'Jira workflow status and comment-reported test status are reported separately. A Done status is not treated as proof of a test pass when the comment says pending, partial pass, fail, or does not give a clear QA outcome.',
10:'Only comments authored by Hilya T Ntinda are summarized where available. The results column uses the latest relevant Hilya QA comment found in the retrieved Jira comments; links open the issue for full comment history and attachments.',
11:'2. Status at a Glance',
12:'Jira status: the workflow state returned by Jira. Comment result: the latest Hilya QA statement found in Jira comments. “Not stated” means no explicit PASS/FAIL was identifiable in that comment.',
13:'64 assigned issues are in scope: 53 Done and 11 Review (board QA-Testing). The comment evidence includes several open or unclear QA findings despite a Done workflow status; see the flagged findings below.',
14:'3. Jira Done Issues',15:'4. Jira Review Issues (Board QA-Testing)',
16:'5. Findings and Status Discrepancies',
17:'The Jira status Done conflicts with comments indicating pending or incomplete testing on ACSS-286, ACSS-322, ACSS-262, ACSS-263, ACSS-266, ACSS-318, ACSS-300 and ACSS-273. These remain reported as Jira Done while the comment-based result is shown as unclear or pending.',
18:'In Jira Review, ACSS-316 is explicitly marked “Not working”; ACSS-317 and ACSS-328 include Hilya comments that say issues remain pending. ACSS-305 has a later “Resolved” comment, but earlier detailed QA text included partial pass/fail findings and the closure note does not explicitly record a retest PASS.',
19:'ACSS-309 contains a PASS after the passport placeholder fix, though its Jira workflow status is still Review. ACSS-311 contains a renewal test checklist but no explicit final pass was identifiable in the extracted comment text.',
20:'Three Jira Done issues (ACSS-280, ACSS-282 and ACSS-281) returned no comments in the requested Jira data view. They are retained in scope and marked accordingly.',
21:'The report does not infer a pass from a workflow transition or from a comment that only says “Resolved” where a full retest result is not stated.',
22:'6. Overall QA Readiness',23:'The Jira board contains 53 assigned Done issues and 11 assigned Review issues. Comment evidence is mixed, so this consolidated report does not declare the entire scope passed.',
24:'Open QA or comment/status discrepancies are highlighted for review. Jira issue links provide access to complete comments and screenshot attachments.',
25:'The assigned Jira scope is fully listed; three issues have no comment returned in Jira.',
26:'Report compiled by Hilya T Ntinda.',
27:'Comment summaries are excerpts or concise paraphrases. They preserve the author’s stated result and do not turn incomplete evidence into a pass.',
28:'3 items in Review include explicit unresolved/pending feedback; additional Done items also have incomplete or conflicting QA evidence.',
29:'7. Scope and Evidence',
30:'Source: ACSS Jira board 814, Assigned to me quick filter, with issues in Done and the board’s QA-Testing lane. Jira’s underlying status for the latter is “Review.” Issue keys and summaries were retrieved from Jira; comment result text is limited to Hilya T Ntinda’s QA comments where available. Report date: 23 November 2026. Jira status values and comments were captured through the logged-in browser session.',
32:'Prepared by Hilya T Ntinda, Adaire.'
}
for i,t in para.items(): set_text(doc.paragraphs[i],t)
for i in (14,15): doc.paragraphs[i].paragraph_format.page_break_before=True
for i in (14,15,16,22,29): doc.paragraphs[i].paragraph_format.keep_with_next=True

meta=[['Field','Detail','Field','Detail'],['Project','ACSS / Student Stay','Source','Jira board 814'],['Scope','Assigned to Hilya T Ntinda','Jira statuses','Done and Review (QA lane)'],['Done issues','53','Review issues','11'],['Report date','23 November 2026','Prepared by','Hilya T Ntinda']]
summary=[['Jira status','Issues','Comment evidence','Interpretation','Report treatment'],['Done','53','Mixed: PASS, fixed/resolved, pending and unclear','Workflow state only','All listed'],['Review / board QA-Testing','11','Includes PASS, “Not working,” pending and unclear','Open workflow state','All listed'],['Total','64','Mixed evidence','Not an overall pass','Comment outcomes kept separate']]

def replace_table(table,data,widths):
    while len(table.rows)<len(data):
        ix=len(table.rows); ti=1 if ix%2 else min(2,len(table.rows)-1)
        table._tbl.append(__import__('copy').deepcopy(table.rows[ti]._tr))
    while len(table.rows)>len(data): table._tbl.remove(table.rows[-1]._tr)
    table.autofit=False
    for ci,w in enumerate(widths): table.columns[ci].width=Inches(w)
    for ri,row in enumerate(data):
        for ci,value in enumerate(row):
            cell=table.rows[ri].cells[ci]; cell.width=Inches(widths[ci])
            p=cell.paragraphs[0]; p.clear(); p.alignment=WD_ALIGN_PARAGRAPH.LEFT
            if isinstance(value,tuple) and value[0]=='link':
                add_hyperlink(p,value[1],value[2])
            else: p.add_run(str(value))
            for run in p.runs:
                run.font.size=Pt(8.2 if ri else 9)
                if ri==0: run.bold=True; run.font.color.rgb=RGBColor(255,255,255)
            if ri==0:
                trPr=table.rows[ri]._tr.get_or_add_trPr()
                if trPr.find(qn('w:tblHeader')) is None: trPr.append(OxmlElement('w:tblHeader'))

def add_hyperlink(paragraph,text,url):
    part=paragraph.part; rid=part.relate_to(url,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',is_external=True)
    h=OxmlElement('w:hyperlink'); h.set(qn('r:id'),rid)
    run=OxmlElement('w:r'); pr=OxmlElement('w:rPr'); color=OxmlElement('w:color'); color.set(qn('w:val'),'0563C1'); pr.append(color); u=OxmlElement('w:u'); u.set(qn('w:val'),'single'); pr.append(u); run.append(pr)
    tx=OxmlElement('w:t'); tx.text=text; run.append(tx); h.append(run); paragraph._p.append(h)

replace_table(doc.tables[0],meta,[1.53,1.67,1.53,1.77])
replace_table(doc.tables[1],summary,[1.6,0.75,1.05,1.25,1.2])
headers=['Jira ID / link','Task / test case','Hilya’s Jira QA comment / test result','Jira status']
def rows(items,status):
    data=[]
    for key,title,comment in items:
        url='https://helloadaire.atlassian.net/browse/'+key
        data.append([('link',key,url),title,comment,status])
    return data
replace_table(doc.tables[2],[headers]+rows(done[:27],'Done'),[0.8,1.65,3.35,0.65])
replace_table(doc.tables[3],[headers]+rows(done[27:],'Done')+rows(review,'Review'),[0.8,1.65,3.35,0.65])
for sec in doc.sections:
    if sec.header.paragraphs: set_text(sec.header.paragraphs[0],'Adaire  |  Student Stay Jira QA Report  |  Internal')
doc.core_properties.title='Student Stay Jira Assigned Tasks QA Report'
doc.core_properties.subject='Assigned ACSS Jira tasks in Done and board QA-Testing/Review'
doc.core_properties.author='Hilya T Ntinda'
doc.save(OUTPUT)
print('OUTPUT',OUTPUT,'SIZE',OUTPUT.stat().st_size,'HASH',hashlib.sha256(OUTPUT.read_bytes()).hexdigest())
print('DONE_ROWS',len(done),'REVIEW_ROWS',len(review),'REPORT_ROWS',len(done)+len(review),'TABLES',[len(t.rows) for t in Document(OUTPUT).tables])
