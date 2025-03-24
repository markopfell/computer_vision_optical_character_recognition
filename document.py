from PyPDF2 import PdfWriter, PdfReader

document_file_name = "/Users/mark/computer_vision_optical_character_recognition/source/Sample 1/Sample 1.pdf"

document_name_and_extension = document_file_name.split('/')[-1]
document_name, extension = document_name_and_extension.split('.')
print(document_name)

inputpdf = PdfReader(open(document_file_name, "rb"))

for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    with open(str(document_name) + "-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)