inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = pypdf.PdfWriter()
    print(merger)
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("super.pdf")


pdf_combiner(inputs)
