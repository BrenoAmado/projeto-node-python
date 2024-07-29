import docx2pdf
import PyPDF2


def converter_docx_para_pdf(docx_path, pdf_path):
    try:
        # Converte o arquivo DOCX para PDF
        docx2pdf.convert(docx_path, pdf_path)
        return True
    except Exception as e:
        return str(e)


def ler_paginas_pdf(pdf_path):
    try:
        texto_das_paginas = []
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                texto = page.extract_text()
                texto_das_paginas.append(texto)
        return texto_das_paginas
    except Exception as e:
        return str(e)


def extract_data_docx(caminho):
    try:
        # Converter DOCX para PDF
        pdf_path = caminho.replace('.docx', '.pdf')
        if converter_docx_para_pdf(caminho, pdf_path):
            # Ler todas as páginas do PDF
            paginas_do_pdf = ler_paginas_pdf(pdf_path)

            if len(paginas_do_pdf) > 10:
                # Dividir as páginas em grupos de 4
                grupos_de_paginas = [paginas_do_pdf[i:i+4] for i in range(0, len(paginas_do_pdf), 4)]

            else:
                # Dividir as páginas em grupos de 8
                grupos_de_paginas = [paginas_do_pdf[i:i + 8] for i in range(0, len(paginas_do_pdf), 8)]

            grupos_de_paginas_format = [[''.join(texto.split('\n')).strip() for texto in grupo] for grupo in grupos_de_paginas]

            return grupos_de_paginas_format

        else:
            return f'Falha ao converter {caminho} para PDF.'
    except Exception as e:
        return str(e)
