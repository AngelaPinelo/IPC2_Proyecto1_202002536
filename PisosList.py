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
        tempo= self.first
        while tempo != None:
            print('Nombre del piso:', tempo.name, 'Número de filas:', tempo.rows, 'Número de columnas', tempo.colums, 'Precio flip: Q', tempo.flip,'Precio del slide: Q', tempo.slide)
            tempo=tempo.getSiguiente()
            
    
    def OrdenamientoBurbuja2(self):
        if self.size > 1:
            while True:
                actual = self.first
                i = None  # anterior
                j = self.first.next  # siguiente
                batman = False
                while j != None:
                    if actual.name > j.name:
                        batman = True
                        if i != None:
                            tempo = j.next
                            i.next = j
                            j.next = actual
                            actual.next = tempo
                        else:
                            tempo2 = j.next
                            self.first = j
                            j.next = actual
                            actual.next = tempo2
                        i = j
                        j = actual.next
                    else:
                        i = actual
                        actual = j
                        j = j.next
                if not batman:
                    break
            