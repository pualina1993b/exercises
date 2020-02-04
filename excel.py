import openpyxl as xl

#open excel file
wb = xl.load_workbook("file2.xlsx")

#choose sheet
sheet = wb["Arkusz1"]

#choose cell
cell = sheet['a1']
print(cell.value)

