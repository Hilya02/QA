from pathlib import Path
from openpyxl import load_workbook
p=Path(r'C:\Users\HilyaNtinda\Downloads\Student_Accommodation_Fee_Test_Matrix 1.xlsx')
for data_only in (False,True):
    wb=load_workbook(p,read_only=True,data_only=data_only)
    print('\nDATA_ONLY',data_only,'SHEETS',wb.sheetnames)
    for ws in wb.worksheets:
        print('\nSHEET',ws.title,'DIM',ws.max_row,ws.max_column)
        for row in ws.iter_rows(min_row=1,max_row=min(ws.max_row,30),values_only=True):
            print(row)
    wb.close()
