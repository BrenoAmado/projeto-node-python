import os.path

import speech_recognition as sr
from moviepy.editor import AudioFileClip

def audio_para_texto(arquivo):
    reconhecer = sr.Recognizer()

    extensao = os.path.splitext(arquivo)[1].lower()

    if extensao == '.wav':
        # Se a extensão for .wav, não precisa realizar a transformação
        with sr.AudioFile(arquivo) as source:
            audio = reconhecer.record(source)
    elif extensao == '.mp4':
        # Se a extensão for .mp4, extrair o áudio do vídeo
        audio_clip = AudioFileClip(arquivo)
        audio_temp = "temp.wav"
        audio_clip.write_audiofile(audio_temp, codec='pcm_s16le')
        with sr.AudioFile(audio_temp) as source:
            audio = reconhecer.record(source)
        # Remover o arquivo temporário
        os.remove(audio_temp)
    else:
        raise f"Extensão de arquivo não suportada: {extensao}"

    try:
        texto = reconhecer.recognize_google(audio, language='pt-BR')
        return texto
    except sr.UnknownValueError:
        return "Não foi possível identificar a fala"
    except sr.RequestError as e:
        return f"Erro ao fazer a solicitação ao Google Web Speech API; {e}"
