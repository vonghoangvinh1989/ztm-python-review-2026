import pypdf

watermake_file = pypdf.PdfReader("wtr.pdf").pages[0]
writer = pypdf.PdfWriter(clone_from="dummy.pdf")

for page in writer.pages:
    page.merge_page(watermake_file, over=False)

with open("output_watermark.pdf", "wb") as file:
    writer.write(file)
