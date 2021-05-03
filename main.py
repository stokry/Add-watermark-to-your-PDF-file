from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

pdf_file = r'C:\Users\Stokry\Desktop\python\pdf\test1.pdf'
watermark = r'C:\Users\Stokry\Desktop\python\pdf\logopdf.pdf'
merged = r'C:\Users\Stokry\Desktop\python\pdf\merged.pdf'

with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
    input_pdf = PdfFileReader(input_file)
    watermark_pdf = PdfFileReader(watermark_file)
    watermark_page = watermark_pdf.getPage(0)

    output = PdfFileWriter()

    for i in range(input_pdf.getNumPages()):
        pdf_page = input_pdf.getPage(i)
        pdf_page.mergePage(watermark_page)
        output.addPage(pdf_page)

    with open(merged, "wb") as merged_file:
        output.write(merged_file)