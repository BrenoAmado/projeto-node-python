import os.path
from Exceptions.NotSupportedExtension import NotSupportedExtension
from GeneralFunctions.ChatGpt import GptResponse
from GeneralFunctions.IdentifyType import identify_type
from GeneralFunctions.ReadDocx import extract_data_docx
from GeneralFunctions.ReadPdf import extract_data_pdf
from GeneralFunctions.ReadAudio import audio_para_texto


class ReadingFiles:
    def read_file(self, name):
        extension = self.identify_type(name)
        if extension == 'pdf':
            return self.read_pdf(name)
        elif extension == 'docx':
            return self.read_word(name)
        elif extension == 'wav' or extension == 'mp4':
            return self.read_audio(name)
        else:
            raise NotSupportedExtension(extension)

    def identify_type(self, name):
        return identify_type(name)

    def read_word(self, name):
        return extract_data_docx(name)

    def read_pdf(self, name):
        return extract_data_pdf(name)

    def read_audio(self, name):
        return audio_para_texto(name)

    def run(self, name, name2 = '', question = ''):

        if has_both(name, name2):
            content1 = self.read_file(name)
            content2 = self.read_file(name2)

            if isinstance(content1, str):
                lista_unica_content1 = [content1]
            else:
                lista_unica_content1 = content1

            if isinstance(content2, str):
                lista_unica_content2 = [content2]
            else:
                lista_unica_content2 = content2

            if len(lista_unica_content1) and len(lista_unica_content2) > 10:
                result1 = []
                for texto in lista_unica_content1:
                    result = GptResponse.analyse_extract(texto, 'Faça um resumo do texto a seguir')
                    result1.append(result)

                result2 = []
                for texto in lista_unica_content2:
                    result = GptResponse.analyse_extract(texto, 'Faça um resumo do texto a seguir')
                    result2.append(result)

                return GptResponse.compare(result1, result2)

            else:
                return GptResponse.compare(lista_unica_content1, lista_unica_content2)

        else:
            content1 = self.read_file(name)

            if isinstance(content1, str):
                lista_unica_content1 = [content1]
            else:
                lista_unica_content1 = content1

            if len(lista_unica_content1) >= 5:
                results = []
                for texto in lista_unica_content1:
                    result = GptResponse.analyse_extract(texto, 'Traga todas as informações mais relevantes do texto a seguir')
                    results.append(result)
                return GptResponse.analyse_extract(results, question)
            else:
                return GptResponse.analyse_extract(lista_unica_content1, question)


def has_both(file1, file2 = ''):
    if file1 and file2 != '':
        return True
    return False
