import xlrd
from openpyxl import Workbook


# Открываем файл Excel для чтения с помощью xlrd
book = Workbook(filename="E:/PYTHON/EXEL/altayka.xls")

# Получаем ссылку на лист, на котором находятся данные, которые мы хотим скопировать
sheet = workbook['1']

# Создаем новый файл Excel и добавляем в него новый лист, на который мы будем копировать данные
workbook_new = openpyxl.Workbook()
for i in range(1, 30):
    print(sheet['A' + str(i)].value)