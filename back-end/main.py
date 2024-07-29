from flask import Flask, request
from flask_cors import CORS
from GeneralFunctions import ReadingFiles

app = Flask(__name__)
CORS(app)


@app.route('/getCompare', methods=['POST'])
def run_compare():
    file1 = request.files['file1']
    file2 = request.files['file2']

    if file1 and file2:
        filename1 = file1.filename
        file_ext1 = filename1.rsplit('.', 1)[1].lower()

        filename2 = file2.filename
        file_ext2 = filename2.rsplit('.', 1)[1].lower()

        if file_ext1 in {'pdf', 'mp4', 'wav'} and file_ext2 in {'pdf', 'mp4', 'wav'}:
            temp_pdf_path1 = f'temp1.{file_ext1}'
            temp_pdf_path2 = f'temp2.{file_ext2}'
            file1.save(temp_pdf_path1)
            file2.save(temp_pdf_path2)

            x = ReadingFiles()
            result = x.run(temp_pdf_path1, temp_pdf_path2, '')

            return str(result)

        else:
            return "Formato de arquivo não suportado. Use .pdf, .mp4 ou .wav para ambos os arquivos."

    else:
        return "Arquivos não recebidos na requisição."


@app.route('/getResumo', methods=['POST'])
def run_resumo():
    file1 = request.files['file1']
    question = request.form.get('question')

    if file1:
        filename = file1.filename
        file_ext = filename.rsplit('.', 1)[1].lower()

        if file_ext in {'pdf', 'mp4', 'wav'}:
            temp_file_path = f'temp.{file_ext}'
            file1.save(temp_file_path)

            x = ReadingFiles()
            result = x.run(temp_file_path, '', question)

            return str(result)

        else:
            return "Formato de arquivo não suportado. Use .pdf, .mp4 ou .wav."

    else:
        return "Arquivo não recebido na requisição."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)


    # x = ReadingFiles()
    #comparação
    # print(x.run(r'C:\Users\breno.amado\Documents\GitHub\ultra-mvp-back\Files\Apresentaçao 1T23.pdf', r'C:\Users\breno.amado\Documents\GitHub\ultra-mvp-back\Files\Apresentaçao 2T23.pdf', ''))
    # print(x.run(r'C:\Users\breno.amado\Documents\GitHub\algar\algar-mvp-back\Files\audio_teste.mp4', r'C:\Users\breno.amado\Documents\GitHub\algar\algar-mvp-back\Files\teste_audio_en.wav', ''))

    #analise/resumo
    # print(x.run(r'C:\Users\breno.amado\Documents\GitHub\algar\algar-mvp-back\Files\Apresentaçao 1T23.pdf', '', 'Do que se trata o conteudo a seguir'))
    # print(x.run(r'C:\Users\breno.amado\Documents\GitHub\ultra-mvp-back\Files\Transcriçao Ultrapar Port 2T23.pdf', '', 'Quais os destaques do texto?'))
    # print(x.run(r'C:\Users\breno.amado\Documents\GitHub\ultra-mvp-back\Files\Release 4Q21.docx', '', 'Quais foram os Highlights que o texto se refere, em pt-BR?'))
    # print(x.run(r'C:\Users\breno.amado\Documents\GitHub\algar\algar-mvp-back\Files\Apresentaçao 2T23.pdf', '', 'Procure e extraia o numero de postos da rede Ipiranga'))
