# Rotate the dummy.pdf to 90 degrees clockwise

import PyPDF2

with open('dummy.pdf','rb') as file:
    # Initialize PDFFileReader object
    reader = PyPDF2.PdfFileReader(file)
    
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)

    # Initialize PDFFileWriter object
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("dummyrotated.pdf",'wb') as new_file:
        writer.write(new_file)