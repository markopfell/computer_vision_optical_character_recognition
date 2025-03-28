import fitz # PyMuPDF
import numpy

def template_numbers(_raw_flat_table_text):

    end_key = 'Comments'
    template_number_column_key = '#'
    template_number_column = 0
    number_of_columns = 0
    number_of_templates = 0

    raw_flat_table_text_no_whitespace = _raw_flat_table_text.split('\n')
    # print(raw_flat_table_text_no_whitespace)

    for i, text in enumerate(raw_flat_table_text_no_whitespace):

        if end_key in text:
            number_of_columns = i + 1
            # print(text, end_key, number_of_columns)
        if template_number_column_key in text and template_number_column == 0:
            template_number_column = i

    table_text = [raw_flat_table_text_no_whitespace[x:x + number_of_columns] for x in
                  range(0, len(raw_flat_table_text_no_whitespace), number_of_columns)]

    template_numbers = []
    for j, row in enumerate(table_text):
        if len(row) >= template_number_column + 1 and j > 0 and row[template_number_column].isnumeric() == True:
            # print(template_number_column, '|',repr(row[template_number_column]),'|')
            template_numbers.append(int(row[template_number_column]))
            # print(template_numbers)

    return max(template_numbers)


document_file_name = '/Users/mark/computer_vision_optical_character_recognition/source/Sample 2/Sample 2.pdf'
split_document_images_folder = '/Users/mark/computer_vision_optical_character_recognition/source/Sample 2/Sample 2 split images/'
document_title, document_extension = (document_file_name.split('/')[-1]).split('.')
dpi = 300 # guess ... it's slow though
key_character = '#'
maximum_number_of_templates = 0
maximum_number_of_templates_page = 0

pdffile = document_file_name
doc = fitz.open(pdffile)

for i, _ in enumerate(doc.pages()):
    page = doc.load_page(i)

    text = page.get_text("blocks")
    # print(text)
    for block in text:
        x0, y0, x1, y1, text_lines, block_number, block_type = block
        if key_character in text_lines:
            # print(text_lines)
            if template_numbers(text_lines) > maximum_number_of_templates:
                maximum_number_of_templates = template_numbers(text_lines)
                maximum_number_of_templates_page = i



    # with open(f'{split_document_images_folder}{document_title}-page{i}.txt', 'w') as output:
    #     output.write(text)

    pix = page.get_pixmap(dpi=dpi)
    output_pixels = f'{split_document_images_folder}{document_title}-page{i}.jpg'
    pix.save(output_pixels)

doc.close()
# [[11, 0], [16, 1], [17, 2], [13, 3], [15, 4], [17, 5], [7, 6], [4, 7], [3, 8], [9, 9], [4, 10]]
print('maximum number of templates and page: ', maximum_number_of_templates, maximum_number_of_templates_page)


