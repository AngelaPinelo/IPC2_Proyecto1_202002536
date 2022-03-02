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
        #cada node de este tipo "piso" contiene una lista de patrones que almacena la cadena de cada piso 
        #self.pattern = ListaPatrones()
        #self.casillas=Matriz()