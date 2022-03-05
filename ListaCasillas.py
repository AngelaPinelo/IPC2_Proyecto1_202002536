from casilla import Casilla 
class CasillasList():
    def __init__(self):
        self.first= None
        self.last=None 
        self.size= 0 
        
        
    def vacia(self):
        return self.first == None 
    
    
    def InsertarCasillaFinal (self,x,y,bow):
        new_casilla= Casilla(x,y,bow)
        self.size +=1
        if self.vacia():
            self.first = new_casilla 
            self.last =new_casilla 
            self.first.next= self.first
            self.first.next= self.last
        else:
            self.last.setSiguiente(new_casilla)
            new_casilla.setAnterior(self.last)
            self.last=new_casilla 
    
    def showCasillas (self):
        tmp= self.first
        while tmp is not None:
            print('Coordenada en x:', tmp.coox, 'Coordenada en y:', tmp.cooy, 'Color del Azulejo:', tmp.color)
            tmp=tmp.getSiguiente()
            