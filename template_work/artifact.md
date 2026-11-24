# Template contract

- Reference DOCX: `C:\Users\HilyaNtinda\Desktop\Student Stay\Marvel TC\20260912.Student_Stay_QA_Report_Round 1.docx`
- SHA-256: `875c23459cda5b607f5c43290c5e060ae32fcbfbb0e1774e4807d80cbf90b67c`
- Reference render: attempted with the bundled `render_docx.py`; it could not run because `soffice.exe` is not installed in the bundled environment. Page count remains unresolved and will be checked in Microsoft Word.
- Page system: one US Letter portrait section, 8.5 x 11 inches; margins L/R 1 inch, T/B 0.75 inch. Header and footer are present; different first page is off.
- Title block: four left-aligned paragraphs: ADAIRE in 13 pt bold deep red (#B01116); report name in 10 pt bold gray (#595959); project label in 24 pt bold dark red (#7A0C10); report subtitle in 13 pt gray. No image/logo media was found.
- Body: 9.5 pt visually specified in direct formatting; Heading 1 section headings are numbered and use the template's existing heading style. Body paragraphs have 6 pt after spacing; heading 1 uses 14 pt before / 7 pt after.
- Tables: four direct-format tables with dark red (#B01116) header fills, bold white 9.5 pt header text, visible light gray grid lines, and 9.5 pt body text. Table 0 is a 4-column metadata table; Table 1 is a 5-column summary; Tables 2 and 3 are 4-column repeated record tables. Available content width is 6.5 inches.
- Header/footer: header currently contains the Adaire / Student Stay QA report label. Footer contains a page-number field phrase (`Page [PAGE] of [NUMPAGES]`). Preserve footer fields and change the header label to identify the inventory report.
- Content flow: title and metadata; executive summary; status at a glance; two findings tables; themes; recommendations; scope and limitations; author line.
- Slot map for this report: retain title block, metadata table, executive summary and section sequence. Reuse Table 1 for building inventory totals, Table 2 for block totals, and Table 3 for the executed checks. Rename the student/admin findings headings to room/block counts and executed QA checks. Reuse themes/recommendations/scope slots for the source report's findings, follow-up, evidence and limits. Preserve all source metrics and statuses; do not infer outcomes for unverified or unrun cases.
- Package: reference has no media files; it contains document, styles, numbering, header/footer, comments, notes, settings, font table, and relationships. Preserve page geometry, table treatment, header/footer fields, and original file bytes.
- Fidelity gate: render the final DOCX; inspect every page at 100%; check all table content and page breaks. Since LibreOffice is unavailable here, use Word's render/print view and capture every page for inspection. Compare final styles and section geometry to this contract.
