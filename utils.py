from docx2pdf import convert

def convert_to_pdf(input_path, output_path):
    # docx2pdf só funciona no Windows diretamente com caminho de saída
    convert(input_path, output_path)
