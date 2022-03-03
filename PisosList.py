from piso import Piso
#Vamos a crear una lista doblemente enlazada para los pisos 
class ListaPisos():
    def __init__ (self):
        self.first = None #apuntador cabecera
        self.last = None #apuntador al final 
        self.size = 0 #para ir definiendo el tamaño de mi lista 
        
    #acá vamos a verificar si la lista está vacía 
    def vacia (self):
        return self.first == None
    
    #insertar al final de la lista 
    def insertNodeLast (self,name, r, c, f,s):
        new_piso = Piso(name, r, c, f,s)
        #para saber el tamaño de mi lista 
        self.size+=1
        #si la lista está vacía 
        if self.vacia():
            self.first = new_piso 
            self.last = self.first
            self.first.next = self.first 
            self.first.next = self.last
        else:
            #al último nodo se le asigna el apuntador siguiente hacia  al nuevo nodo piso
            self.last.setSiguiente(new_piso)
            #al nuevo piso se le asigna el apuntador anterior al nodo que estaba de último
            new_piso.setAnterior(self.last)
            #ahora el apuntador del final de la lista apunta el nuevo nodo piso recién agregado
            self.last = new_piso
    
    def mostrarPisos (self):
        tmp= self.first
        while tmp is not None:
            print('Nombre del piso:', tmp.name, 'Número de filas:', tmp.rows, 'Número de columnas', tmp.colums, 'Precio flip: Q', tmp.flip,'Precio del slide: Q', tmp.slide)
            tmp=tmp.getSiguiente()
            
            