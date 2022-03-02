#Vamos a crear una lista doblemente enlazada para los pisos 
class ListaPisos():
    def __init__ (self):
        self.first = None #apuntador cabecera
        self.last = None #apuntador al final 
        self.size = 0 #para ir definiendo el tamaño de mi lista 
        
    #acá vamos a verificar si la lista está vacía 
    def vacia (self ):
        return self.first == None
        