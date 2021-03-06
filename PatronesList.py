from patron import Patron

class ListaPatrones():
    def __init__ (self):
        self.primero= None
        self.ultimo = None 
        self.size = 0 
        
    def insertarPatronLast(self, code, cadena):
        nuevo_patron = Patron(code, cadena) 
        self.size += 1
        if self.primero is None:
            self.primero = nuevo_patron
            self.ultimo = nuevo_patron 
        else: 
            self.ultimo.setSiguiente(nuevo_patron)
            nuevo_patron.setAnterior(self.ultimo)
            self.ultimo = nuevo_patron
            
    def mostrarPatrones(self):
        #para que guarde temporalmente el "primer Nodo" y así ir mostrándolo a medida que se agregan más 
        batman= self.primero
        while batman != None:
            print('Código del piso:', batman.code, 'Cadena:', batman.cadena)
            batman=batman.getSiguiente()