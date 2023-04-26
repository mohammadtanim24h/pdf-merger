import PyPDF2
import os

merger = PyPDF2.PdfMerger()

pdfFiles = []

# Adding the names of all pdf files (except the merged.pdf) located in current folder in pdfFiles list
for filename in os.listdir('.'):
    if filename.endswith('.pdf') and filename != 'merged.pdf':
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

print(pdfFiles)
