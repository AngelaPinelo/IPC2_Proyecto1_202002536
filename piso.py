#Mi nodo de tipo Piso 
class Piso ():
    def __init__(self,name, r, c, f,s):
        self.name = name
        self.rows = r
        self.colums= c
        #para guardar el costo del flip y del slide
        self.flip = f
        self.slide= s
        self.next = None
        self.anterior= None
        #cada node de este tipo "piso" contiene una lista de patrones que almacena la cadena de cada piso 
        #self.pattern = ListaPatrones()
        #self.casillas=Matriz()
                
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name   
           
    def getSiguiente(self):
        return self.next
    
    def setSiguiente(self, piso):
        self.next = piso

    def getAnterior(self):
        return self.anterior
    
    def setAnterior(self, piso):
        self.anterior = piso