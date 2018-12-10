# Classe Filme para criação de instâncias com caracteristicas de um filme
class Filme():
    def __init__(self, titulo, imagem_url, trailer_youtube_url):
        self.titulo = titulo
        self.imagem_url = imagem_url
        self.trailer_youtube_url = trailer_youtube_url

