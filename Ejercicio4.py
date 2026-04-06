class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor