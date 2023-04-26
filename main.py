import PyPDF2
import os

merger = PyPDF2.PdfMerger()

pdfFiles = []

# Adding the names of all pdf files (except the merged.pdf) located in current folder in pdfFiles list
for filename in os.listdir('.'):
    if filename.endswith('.pdf') and filename != 'merged.pdf':
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()

merger.write('merged.pdf')
