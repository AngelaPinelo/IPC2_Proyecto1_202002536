#Mi nodo de tipo patrón 
class Patron():
    def __init__ (self,code,cadena):
        self.code = code
        #cadena se refiere al WBBW 
        self.cadena = cadena
        self.siguiente=None
        
    def getSiguiente(self):
        return self.siguiente
    
    def setSiguiente(self, patron):
        self.siguiente = patron

    def getAnterior(self):
        return self.anterior
    
    def setAnterior(self, patron):
        self.anterior = patron