import sys
import PyPDF2
from PyPDF2 import pdf

input = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('merged.pdf')

pdf_combiner(input)