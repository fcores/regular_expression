import PyPDF2
import re


pdf_file = open(r'C:\Users\facucores\Desktop\prueba.pdf', mode='rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

#Hola


####################################
###################3




# Obtenga todas las páginas del archivo pdf
number_of_pages = read_pdf.getNumPages()
# print('total_page: ', number_of_pages)
line_list = []
        # Recorrer cada página
for i in range(0, number_of_pages):
                # Leer el contenido de cada página
    page = read_pdf.getPage(i)
    page_content = page.extractText()
    print(page_content)
                # Divida el contenido de esta página en una lista y agregue todo el contenido de la página
    line_list += page_content.split()
    regex=r'[a-zA-Z]{1,4}[0-9]{1,5}[a-zA-Z_0-9.]+'
    a = re.findall(regex, line_list)
    print(a)
    
        # Cerrar archivo pdf
pdf_file.close()
# line_buf = ''
# for buf in line_list:
#     line_buf = line_buf+' '+buf
#         # Datos de coincidencia: la primera y la segunda columna, como: 000069.sz y 100
# print(line_buf)
# regex=r'[0-9]'
# a = re.findall(regex, line_buf)
# print(a)
# # b = re.findall('[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+.[a-z]+[a-z].([0-9,]+)', line_buf)
# # # print(b)
# # for i in range(0, len(a)):
# #     a[i] = a[i].upper()
# # for i in range(0, len(b)):
# #     b[i] = int(b[i].replace(',', ''))
# # # print(b)
# #         # Haz un diccionario
# # results = dict(zip(a, b))