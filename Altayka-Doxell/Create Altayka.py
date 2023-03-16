import xlrd
import openpyxl


# Открываем файл Excel для чтения с помощью xlrd
workbook = xlrd.open_workbook('altayka.xls')

# Получаем ссылку на лист, на котором находятся данные, которые мы хотим скопировать
source_sheet = workbook.sheet_by_name('1')

# Создаем новый файл Excel и добавляем в него новый лист, на который мы будем копировать данные
workbook_new = openpyxl.Workbook()
target_sheet = workbook_new.active
target_sheet.title = '2'

# Выбираем диапазон ячеек, который нужно скопировать
start_row = 13
end_row = 55
start_col = 0
end_col = 2

# Копируем значения ячеек в новый диапазон на листе "NewSheet"
for row in range(start_row, end_row):
    for col in range(start_col, end_col):
        target_sheet.cell(row=row+1, column=col+1, value=source_sheet.cell_value(row, col))

# Сохраняем изменения в новом файле Excel
workbook_new.save('altayka.xlsx')
