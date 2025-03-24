import fitz # PyMuPDF

document_file_name = '/Users/mark/computer_vision_optical_character_recognition/source/Sample 1/Sample 1.pdf'
split_document_images_folder = '/Users/mark/computer_vision_optical_character_recognition/source/Sample 1/Sample 1 split images/'
document_title, document_extension = (document_file_name.split('/')[-1]).split('.')
dpi = 300 # guess ... it's slow though

pdffile = document_file_name
doc = fitz.open(pdffile)

for i, _ in enumerate(doc.pages()):
    page = doc.load_page(i)

    text = page.get_text()

    pix = page.get_pixmap(dpi=dpi)
    output_pixels = f'{split_document_images_folder}{document_title}-page{i}.png'
    pix.save(output_pixels)
doc.close()

