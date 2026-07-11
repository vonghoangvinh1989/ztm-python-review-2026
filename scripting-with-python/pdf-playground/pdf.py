import pypdf

with open("dummy.pdf", "rb") as file:
    reader = pypdf.PdfReader(file)
    print(reader.get_num_pages())
    page = reader.get_page(0)
    page.rotate(90)

    writer = pypdf.PdfWriter()
    writer.add_page(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)


# template = pypdf.PdfReader(open('superduper.pdf', 'rb'))
# watermark = pypdf.PdfReader(open('water.pdf', 'rb'))
# output = pypdf.PdfWriter()

# for i in range(len(template.pages)):
#     page = template.pages[i]
#     page.merge_page(watermark.pages[0])
#     output.add_page(page)

# with open('watermaked_output.pdf', 'wb') as outputFile:
#     output.write(outputFile)
