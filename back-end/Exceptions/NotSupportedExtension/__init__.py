class NotSupportedExtension(Exception):
    def __init__(self, extensao):
        self.extensao = extensao
        super().__init__(f"Extensão de arquivo não suportada: {extensao}")
