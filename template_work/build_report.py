from copy import deepcopy
from pathlib import Path
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import hashlib, shutil

TEMPLATE = Path(r'C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx')
OUTPUT = Path(r'C:\Users\HilyaNtinda\Documents\ChatGPT\AdaireDigital\StudentStay_Room_Inventory_QA_Report.docx')
EXPECTED_HASH = '875c23459cda5b607f5c43290c5e060ae32fcbfbb0e1774e4807d80cbf90b67c'
actual = hashlib.sha256(TEMPLATE.read_bytes()).hexdigest()
if actual != EXPECTED_HASH:
    raise RuntimeError(f'Template changed; expected {EXPECTED_HASH}, got {actual}')
shutil.copy2(TEMPLATE, OUTPUT)
doc = Document(OUTPUT)

# Replace runs in place to retain the template's direct formatting.
def paragraph_text(p, text):
    if p.runs:
        p.runs[0].text = text
        for r in p.runs[1:]:
            r.text = ''
    else:
        p.add_run(text)

updates = {
    1: 'Quality Assurance Test Report',
    2: 'Student Stay',
    3: 'Room Inventory Verification',
    6: '1. Executive Summary',
    7: 'The room inventory review is a partial pass. Workbook bed totals match the portal for Villa Verdi and Mercury House and for all eight blocks. The two workbooks list 366 physical room locations across 67 units and 661 bed records. The portal showed 647 beds available and 14 occupied.',
    8: 'The aggregate capacity is consistent: Villa Verdi has 377 beds and Mercury House has 284. This confirms the building and block bed totals only. The workbooks do not include an availability field or named occupants, so the 14 occupied beds cannot be treated as errors from this comparison.',
    9: 'Room and unit counts were calculated from unique Building + Block + Unit + Room combinations in the workbooks. The portal views reviewed showed bed totals, but the detailed room identifiers were not reconciled individually. Room-level matching therefore remains unverified.',
    10: 'The next checks are to confirm the 14 occupied beds against the current tenancy register and compare every workbook bed identifier and room location with the portal detail. No item-level result is claimed in this report.',
    11: '2. Status at a Glance',
    12: 'Status definitions. PASS: counts agree. PASS*: aggregate bed capacity agrees; availability and occupants were not verified. NOT VERIFIED: evidence was insufficient to confirm the check. NOT ASSERTED: the source data does not define an expected result. NOT RUN: the comparison was not performed.',
    13: 'Portal availability is recorded as observed data only. Neither workbook includes availability status or named occupants, so occupancy is not used as an expected pass/fail value.',
    14: '3. Room and Bed Counts by Block',
    15: '4. Executed QA Checks',
    16: '5. Findings and Follow-up',
    17: 'The workbook and portal agree on aggregate bed capacity. The following follow-up is needed before room-level inventory or occupancy can be confirmed.',
    18: 'Villa Verdi shows 367 of 377 beds available (97.3%), with 10 occupied: 8 in block A and 2 in block C. Mercury House shows 280 of 284 available (98.6%), with 4 occupied, all in block A.',
    19: 'The workbooks leave Student Name and PMS ID blank and contain no availability column. The 14 occupied beds are not proven to be errors. Confirm the occupancy against the current tenancy register.',
    20: 'A room-level pass/fail still requires matching each workbook bed identifier and room location with the portal\'s detailed unit and room records. This comparison was not completed.',
    21: 'The portal views reviewed showed bed totals rather than a verified room or unit count. The workbook room and unit counts should not be presented as portal-verified counts.',
    22: '6. Recommendations',
    23: 'Confirm the 14 occupied beds against the current tenancy register before classifying them as inventory discrepancies.',
    24: 'Compare every workbook bed identifier and room location against the portal\'s detailed unit and room records, then record item-level matches and exceptions.',
    25: 'Verify room and unit totals directly in the portal if those counts are required as acceptance criteria.',
    26: 'Keep the aggregate bed-count results separate from availability and occupant validation; the workbooks do not provide expected values for those fields.',
    27: 'Record the outcome of the tenancy-register check and item-level reconciliation as separate follow-up evidence.',
    28: 'Use the source status labels consistently: PASS*, NOT VERIFIED, NOT ASSERTED, and NOT RUN.',
    29: '7. Scope and Evidence',
    30: 'The review covered the 2026 building inventory for Villa Verdi and Mercury House using the workbook tabs Verdi (2), rows 3-379, and Mercury (2), rows 3-286. Portal pages reviewed were All buildings, Villa Verdi, and Mercury House. Portal availability figures were observed on 20 November 2026. Individual room and bed identifiers were not compared against the portal. Availability and occupant names could not be reconciled because the workbooks contain no corresponding fields.',
    32: 'Prepared by: Not stated in the source report.',
}
for idx, text in updates.items():
    paragraph_text(doc.paragraphs[idx], text)

# Update title and source metadata table.
meta = [
    ['Field','Detail','Field','Detail'],
    ['System','Student Stay','Report type','Room Inventory QA Summary'],
    ['Modules tested','Admin Portal inventory','Test status','Partial pass; follow-up required'],
    ['Prepared by','Not stated in source','Execution date','20 November 2026'],
    ['Distribution','Not specified','Client ready','Not assessed'],
]

# Summary table: 5 columns and three inventory totals.
summary = [
    ['Building','Physical rooms','Units','Workbook beds','Portal beds / result'],
    ['Villa Verdi','207','40','377','377 - PASS*'],
    ['Mercury House','159','27','284','284 - PASS*'],
    ['Total','366','67','661','661 - PASS*'],
]

blocks = [
    ['Building / block','Physical rooms','Workbook beds','Portal beds / availability'],
    ['Villa Verdi / A','82','163','163 total; 155 available; 8 occupied'],
    ['Villa Verdi / B','42','48','48 total; 48 available; 0 occupied'],
    ['Villa Verdi / C','8','16','16 total; 14 available; 2 occupied'],
    ['Villa Verdi / D','75','150','150 total; 150 available; 0 occupied'],
    ['Mercury House / A','24','38','38 total; 34 available; 4 occupied'],
    ['Mercury House / B','47','86','86 total; 86 available; 0 occupied'],
    ['Mercury House / C','47','86','86 total; 86 available; 0 occupied'],
    ['Mercury House / D','41','74','74 total; 74 available; 0 occupied'],
]

checks = [
    ['Test ID','Check','Expected / source result','Observed portal result / status'],
    ['INV-01','Villa Verdi total beds','377 workbook beds','377 beds; 367 available; 10 occupied - PASS*'],
    ['INV-02','Mercury House total beds','284 workbook beds','284 beds; 280 available; 4 occupied - PASS*'],
    ['BLK-01','Villa Verdi block totals','A 163 / B 48 / C 16 / D 150','163 / 48 / 16 / 150 - PASS'],
    ['BLK-02','Mercury House block totals','A 38 / B 86 / C 86 / D 74','38 / 86 / 86 / 74 - PASS'],
    ['ROOM-01','Physical room and unit counts','Workbook: VV 207 rooms / 40 units; MH 159 rooms / 27 units','Portal view showed bed totals, not a verified room/unit count - NOT VERIFIED'],
    ['AVAIL-01','Availability reconciliation','Neither workbook contains an expected availability field','VV 10 occupied; MH 4 occupied - NOT ASSERTED'],
    ['ID-01','Individual room / bed identifier match','Workbook identifiers require item-level comparison','Not checked against individual portal room records - NOT RUN'],
]

def replace_table(table, rows, widths):
    # Keep existing formatted rows and remove only surplus rows.
    while len(table.rows) < len(rows):
        table._tbl.append(deepcopy(table.rows[-1]._tr))
    while len(table.rows) > len(rows):
        table._tbl.remove(table.rows[-1]._tr)
    for ci, width in enumerate(widths):
        table.columns[ci].width = Inches(width)
        for row in table.rows:
            row.cells[ci].width = Inches(width)
    for ri, values in enumerate(rows):
        row = table.rows[ri]
        for ci, value in enumerate(values):
            cell = row.cells[ci]
            p = cell.paragraphs[0]
            paragraph_text(p, str(value))
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.size = Inches(0.066) # approximately 4.75 pt, replaced below
                r.font.size = __import__('docx').shared.Pt(9.5)
                if ri == 0:
                    r.bold = True
                    r.font.color.rgb = __import__('docx').shared.RGBColor(255,255,255)
        # mark the header row to repeat on page breaks
        if ri == 0:
            trPr = row._tr.get_or_add_trPr()
            if trPr.find(qn('w:tblHeader')) is None:
                trPr.append(OxmlElement('w:tblHeader'))
    # Explicit widths keep the adapted report within the template's 6.5-inch text area.
    table.autofit = False

replace_table(doc.tables[0], meta, [1.53,1.67,1.53,1.77])
replace_table(doc.tables[1], summary, [1.45,1.05,0.65,1.15,2.20])
replace_table(doc.tables[2], blocks, [1.50,0.95,1.00,3.05])
replace_table(doc.tables[3], checks, [0.70,1.45,2.05,2.30])

# Keep table header runs white and bold, and update header label while preserving the footer page fields.
for sec in doc.sections:
    if sec.header.paragraphs:
        paragraph_text(sec.header.paragraphs[0], 'Adaire  |  Student Stay Room Inventory QA')

# Ensure table widths total the template's 6.5 inch content width.
for ti, widths in enumerate(([1.53,1.67,1.53,1.77],[1.45,1.05,0.65,1.15,2.20],[1.50,0.95,1.00,3.05],[0.70,1.45,2.05,2.30])):
    for ci,w in enumerate(widths):
        doc.tables[ti].columns[ci].width=Inches(w)
        for row in doc.tables[ti].rows: row.cells[ci].width=Inches(w)

doc.core_properties.title = 'Student Stay Room Inventory Quality Assurance Test Report'
doc.core_properties.subject = '2026 building inventory verification for Villa Verdi and Mercury House'
doc.save(OUTPUT)
print('WROTE',OUTPUT,'bytes',OUTPUT.stat().st_size)
print('TEMPLATE_SHA256',hashlib.sha256(TEMPLATE.read_bytes()).hexdigest())
