class Casilla():
    def __init__(self, x, y, bow):
        self.coox=x
        self.cooy=y
        self.color=bow
        self.siguiente=None 
        self.anterior=None
    
        
    def getSiguiente(self):
        return self.siguiente
    
    def setSiguiente(self, casilla):
        self.siguiente = casilla

    def getAnterior(self):
        return self.anterior
    
    def setAnterior(self, casilla):
        self.anterior = casilla