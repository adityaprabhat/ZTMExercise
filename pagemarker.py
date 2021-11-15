import PyPDF2

# Grab the pdf to be watermarked
source = PyPDF2.PdfFileReader(open('merged.pdf','rb'))

# Grab the pdf consisting of the watermark
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))

output = PyPDF2.PdfFileWriter()

for page_num in range(source.getNumPages()):        #loop through the pages in source pdf
    page = source.getPage(page_num)                 #get a page from the source pdf
    page.mergePage(watermark.getPage(0))            #merge the content stream of both pages
    output.addPage(page)                            #Add the page to output object

with open("Watermarked_Page.pdf",'wb') as file:
    output.write(file)

