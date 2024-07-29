import PyPDF2
import re


def ler_paginas_pdf(pdf_path):
    try:
        texto_das_paginas = []
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                texto = page.extract_text()
                texto_formatado = ' '.join(re.sub(r'\s+', ' ', texto).split('\n')).strip()
                texto_das_paginas.append(texto_formatado)
        return texto_das_paginas
    except Exception as e:
        return str(e)


def extract_data_pdf(arquivo):
        paginas_do_pdf = ler_paginas_pdf(arquivo)

        if len(paginas_do_pdf) > 10:
            # Dividir as páginas em grupos de 3
            grupos_de_paginas = [paginas_do_pdf[i:i + 3] for i in range(0, len(paginas_do_pdf), 3)]

        else:
            # Dividir as páginas em grupos de 6
            grupos_de_paginas = [paginas_do_pdf[i:i + 6] for i in range(0, len(paginas_do_pdf), 6)]

        return grupos_de_paginas
