import os.path


def identify_type(file):
    nome_sem_extensao, extensao = os.path.splitext(file)
    extensao_sem_ponto = extensao.lstrip('.')
    return extensao_sem_ponto
