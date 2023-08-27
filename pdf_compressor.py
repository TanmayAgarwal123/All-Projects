import PyPDF2

def compress_pdf(input_path, output_path, quality=60):
    with open(input_path, 'rb') as input_file:
        reader = PyPDF2.PdfFileReader(input_file)
        writer = PyPDF2.PdfFileWriter()

        for i in range(reader.getNumPages()):
            page = reader.getPage(i)
            writer.addPage(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

if __name__ == '__main__':
    input_path = input("Enter path of the PDF to be compressed: ")
    output_path = input("Enter path to save the compressed PDF: ")
    compress_pdf(input_path, output_path)
    print(f"Compressed file saved at {output_path}")
