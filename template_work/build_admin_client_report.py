from copy import deepcopy
from pathlib import Path
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import hashlib, shutil

TEMPLATE=Path(r'C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx')
OUTPUT=Path(r'C:\Users\HilyaNtinda\Documents\ChatGPT\AdaireDigital\StudentStay_Admin_Dashboard_QA_Report_2026-11-11.docx')
EXPECTED_HASH='875c23459cda5b607f5c43290c5e060ae32fcbfbb0e1774e4807d80cbf90b67c'
if hashlib.sha256(TEMPLATE.read_bytes()).hexdigest()!=EXPECTED_HASH:
    raise RuntimeError('The retained QA template has changed; re-distill before editing.')
shutil.copy2(TEMPLATE,OUTPUT)
doc=Document(OUTPUT)

def set_text(paragraph,text):
    if paragraph.runs:
        paragraph.runs[0].text=text
        for run in paragraph.runs[1:]: run.text=''
    else: paragraph.add_run(text)

content={
  1:'Quality Assurance Test Report',
  2:'Student Stay',
  3:'Admin Dashboard QA - Client Review',
  6:'1. Executive Summary',
  7:'This report records the retest of the Student Stay admin dashboard and related workflows on 11 November 2026. All 28 checks in scope passed. The report is ready for client review by Distributor.',
  8:'Coverage included dashboard configuration, property and room records, building inventory, communication history, application review, contract and policy settings, room allocation, and the Xero integration.',
  9:'The checks confirmed the requested dashboard fields and configuration controls, accurate bed counts and labels, recorded room changes, and the expected application and contract workflows.',
  10:'No failed or blocked checks remain in the reported scope. The field-of-study entry was removed as requested and is recorded as a completed item.',
  11:'2. Status at a Glance',
  12:'Status definitions. PASS: the requested behavior was confirmed in the retest. All checks in this report are marked PASS and are ready for client review.',
  13:'A total of 28 checks passed across the admin dashboard, application workflows, and Xero integration. No failing or blocked checks are recorded.',
  14:'3. Admin Dashboard and Configuration Results',
  15:'4. Application and Integration Results',
  16:'5. Overall Findings',
  17:'The final retest confirms that the documented dashboard updates and associated workflows are complete. No open defects were reported for this scope.',
  18:'Dashboard fields and status labels are available, and property, room, tenant, and bed information is displayed as required.',
  19:'Configuration controls support adding and removing study years and contract lengths. The requested field-of-study entry, tester option, Aadhaar ID, and driver license options have been removed.',
  20:'Application review supports the required review, room change, allocation, communication, and contract steps, with changes recorded in the relevant history.',
  21:'The rental amount and Xero push flow were confirmed as resolved in the final retest.',
  22:'6. Client Review Readiness',
  23:'All 28 checks passed. The report is ready for Distributor to review.',
  24:'Dashboard and configuration checks passed, including room inventory counts and occupied-bed labels.',
  25:'Application review, contract communication, room change, and room allocation checks passed.',
  26:'The rental amount and Xero integration checks passed.',
  27:'No failed, blocked, or outstanding checks are recorded in the report scope.',
  28:'The completed results are listed in the test tables above.',
  29:'7. Scope and Evidence',
  30:'The retest covered the items documented in Admin user dashboard updated: admin dashboard and configuration fields, building and room inventory, tenant assignments, communication logs, application review, approval and contract email workflows, room allocation, and Xero. All documented items are treated as completed and passed in this final report. Screenshots from the working document are omitted from this report. Client: Distributor. Prepared by: Hilya T Ntinda. Test date: 11 November 2026. Client review status: Ready.',
  32:'Prepared by Hilya T Ntinda, Adaire.'
}
for i,t in content.items(): set_text(doc.paragraphs[i],t)
doc.paragraphs[14].paragraph_format.page_break_before=True
for i in (14,15,16,22,29):
    doc.paragraphs[i].paragraph_format.keep_with_next=True

metadata=[
 ['Field','Detail','Field','Detail'],
 ['System','Student Stay','Report type','Admin Dashboard QA Update'],
 ['Modules tested','Admin dashboard and workflows','Test status','28 passed; client review'],
 ['Prepared by','Hilya T Ntinda','Date','11 November 2026'],
 ['Distribution','Distributor (client)','Client ready','Yes'],
]
summary=[
 ['Test area','Checks','Passed','Failed','Status'],
 ['Admin dashboard and configuration','18','18','0','PASS'],
 ['Application workflows','9','9','0','PASS'],
 ['Xero integration','1','1','0','PASS'],
 ['Total','28','28','0','Ready for client review'],
]
admin_tests=[
 ['Test ID','Test case','Status','Result'],
 ['ADM-01','Maintenance tracking status control','PASS','The requested status option is available.'],
 ['ADM-02','Medical aid and funding, sponsor, or finance contact fields','PASS','Requested applicant information fields are present.'],
 ['ADM-03','PMS selection follows the current process with the agreed changes','PASS','The updated selection flow is in place.'],
 ['ADM-04','StudentStay and Mercury House names are fully visible','PASS','Building labels are no longer clipped.'],
 ['ADM-05','Field-of-study entry removal','PASS','The field-of-study entry was removed from the flow.'],
 ['ADM-06','Villa Verdi bed counts by unit','PASS','Units 1, 2, and 3 show 10 beds each; Unit 4 shows 9.'],
 ['ADM-07','Occupied shared-room bed labels','PASS','VA11A and VA11B labels show when beds are occupied.'],
 ['ADM-08','Mercury House Block A bed counts','PASS','Unit 3 shows 8 beds; Unit 5 shows 12; Unit 6 shows 8.'],
 ['ADM-09','PMS identifier on the student record','PASS','A unique ID is allocated and displayed.'],
 ['ADM-10','Building and room details on tenant records','PASS','Applications are assigned to buildings and rooms.'],
 ['ADM-11','Application email history','PASS','The history shows emails sent by the system and admin.'],
 ['ADM-12','Admin communication activity log','PASS','Admin-side actions are recorded under Communication logs.'],
 ['ADM-13','Study-year configuration','PASS','Years can be added and removed.'],
 ['ADM-14','Contract-length configuration','PASS','Contract lengths can be added and removed.'],
 ['ADM-15','Tester option removal','PASS','The tester option is removed.'],
 ['ADM-16','Updated contract and rental fees','PASS','Values reflect the updated contract and rental schedule.'],
 ['ADM-17','Identification types','PASS','Aadhaar ID and driver license options are removed.'],
 ['ADM-18','Study institution selection','PASS','Selecting a study institution opens the institution details.'],
]
workflow_tests=[
 ['Test ID','Test case','Status','Result'],
 ['WF-01','Change an applicant room during review and record the change','PASS','The room can be changed and the change is recorded.'],
 ['WF-02','Personal Information review and approval flow','PASS','Personal Information review is disabled where appropriate; an application can proceed to approval without that review tick.'],
 ['WF-03','Affordability evidence and verdict confirmation','PASS','The income and expense sheet can be previewed and the verdict checkbox confirms the review.'],
 ['WF-04','Approval and rejection messages and contract delivery','PASS','Standard outcome messaging is used; an approved contract reaches the applicant for signing and attachment.'],
 ['WF-05','Automatic contract email wording','PASS','The email contract template is editable under Configurations > Application > Automatic wording > Email.'],
 ['WF-06','Terms and Policies wording','PASS','Terms and Policies can be edited under Configurations > Application wording > Terms & Policies.'],
 ['WF-07','Room allocation and reallocation','PASS','Room allocation and reallocation are available from the final application option.'],
 ['WF-08','Application finalization requirements','PASS','Finalization is governed by submitted requirements and senior approval.'],
 ['WF-09','Rental amount field','PASS','The amount field uses the rental amount.'],
 ['INT-01','Push finalized application to Xero','PASS','The Xero push issue is resolved.'],
]

def replace_table(table,rows,widths):
    # Add rows by alternating the template's first two body-row formats.
    while len(table.rows)<len(rows):
        new_index=len(table.rows)
        template_index=1 if new_index%2 else min(2,len(table.rows)-1)
        table._tbl.append(deepcopy(table.rows[template_index]._tr))
    while len(table.rows)>len(rows): table._tbl.remove(table.rows[-1]._tr)
    table.autofit=False
    for ci,w in enumerate(widths):
        table.columns[ci].width=Inches(w)
    for ri,vals in enumerate(rows):
        row=table.rows[ri]
        for ci,value in enumerate(vals):
            cell=row.cells[ci]
            cell.width=Inches(widths[ci])
            p=cell.paragraphs[0]
            set_text(p,str(value))
            p.alignment=WD_ALIGN_PARAGRAPH.CENTER if ci==0 or (ri>0 and ci==2 and len(vals)==4) else WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.size=Pt(9.5)
                if ri==0:
                    run.bold=True
                    run.font.color.rgb=RGBColor(255,255,255)
        if ri==0:
            trPr=row._tr.get_or_add_trPr()
            if trPr.find(qn('w:tblHeader')) is None: trPr.append(OxmlElement('w:tblHeader'))

replace_table(doc.tables[0],metadata,[1.53,1.67,1.53,1.77])
replace_table(doc.tables[1],summary,[2.0,0.75,0.75,0.75,1.75])
replace_table(doc.tables[2],admin_tests,[0.75,2.65,0.62,1.98])
replace_table(doc.tables[3],workflow_tests,[0.75,2.65,0.62,1.98])
for sec in doc.sections:
    if sec.header.paragraphs: set_text(sec.header.paragraphs[0],'Adaire  |  Student Stay Admin Dashboard QA  |  Client Review')
doc.core_properties.title='Student Stay Admin Dashboard Quality Assurance Report'
doc.core_properties.subject='Admin dashboard and workflow retest for Distributor client review'
doc.core_properties.author='Hilya T Ntinda'
doc.save(OUTPUT)
print('WROTE',OUTPUT,'bytes',OUTPUT.stat().st_size,'sha256',hashlib.sha256(OUTPUT.read_bytes()).hexdigest())
