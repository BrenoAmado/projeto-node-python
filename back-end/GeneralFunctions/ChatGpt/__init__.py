import threading
import openai


class GptResponse:
    @staticmethod
    def compare(file1, file2):
        return gpt_response(f'Compare os 2 textos a seguir: Texto 1: {file1}    Texto2: {file2}')

    @staticmethod
    def analyse_extract(file1, question):
        return gpt_response(f'{question}: {file1}')


def call_openai_api(text, result_holder):
    try:
        # Fazendo a chamada à API com o motor gpt-4
        resposta = openai.ChatCompletion.create(
            model="gpt-4",  # Modelo de chat gpt-4
            messages=[
                {"role": "system", "content": "Você é um assistente de chat."},
                {"role": "user", "content": text}
            ]
        )

        # Acessando a resposta do modelo
        gpt_response = resposta['choices'][0]['message']['content']
        result_holder[0] = gpt_response

    except openai.error.OpenAIError as e:
        result_holder[0] = None  # Marcar como None em caso de exceção


def gpt_response(question, max_attempts=3, timeout_per_attempt=120):
    openai.api_key = "nelson"
    print(question)
    for attempt in range(max_attempts):
        result = [None]
        api_thread = threading.Thread(target=call_openai_api, args=(question, result))
        api_thread.start()
        api_thread.join(timeout_per_attempt)

        if api_thread.is_alive():
            print(f"Tentativa {attempt + 1} excedeu o tempo limite.")
        else:
            if result[0] is not None:
                return result[0]
            else:
                print(f"Tentativa {attempt + 1} teve erro.")

    print("Todas as tentativas esgotadas. Não foi possível obter uma resposta.")
    raise Exception('Api não responde.')
