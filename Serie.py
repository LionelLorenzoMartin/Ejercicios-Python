class Serie:
    def __init__(self, titulo, nTemporadas, entregado, genero, autor):
        self.titulo=titulo
        self.nTemporadas=nTemporadas
        self.entregado=entregado
        self.genero=genero
        self.autor=autor

    def getTitulo(self):
        return self.titulo

    def getNTemporadas(self):
        return self.nTemporadas

    def getGenero(self):
        return self.genero

    def getAutor(self):
        return self.autor

    def setTitulo(self, titulo):
        self.titulo=titulo

    def setNTemporadas(self, nTemporadas):
        self.nTemporadas=nTemporadas

    def setGenero(self, genero):
        self.genero=genero

    def setCreador(self, autor):
        self.autor=autor

    def entregar(self):
        self.entregado=True

class Videojuego:
    def __init__(self, titulo, horasEstimadas, entregado, genero, compania):
        self.titulo=titulo
        self.horasEstimadas=horasEstimadas
        self.entregado=entregado
        self.genero=genero
        self.compania=compania

    def getTitulo(self):
        return self.titulo

    def getHorasEstimadas(self):
        return self.horasEstimadas

    def getGenero(self):
        return self.genero

    def getCompania(self):
        return self.compania

    def setTitulo(self, titulo):
        self.titulo=titulo

    def setHorasEstimadas(self, horasEstimadas):
        self.horasEstimadas=horasEstimadas

    def setGenero(self, genero):
        self.genero=genero

    def setCompania(self, compania):
        self.compania=compania

    def entregar(self):
        self.entregado=True