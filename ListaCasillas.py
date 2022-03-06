from casilla import Casilla 
#from graphviz import Digraph

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
    
    def graficarPisito(self,x,nuNodos):
        print("Graficando lista...")
        
        dot = Digraph('G', filename='process.dot', engine='dot', format='svg')
        dot.attr(rankdir = "TB")
        dot.node_attr.update(shape="box")
        dot.node_attr['style'] = 'filled'

        nodoTemporal = Nodo("",0,0)
        nodoTemporal = self.head

        flag = False
        contador = 0
        contSubgrap = 1
        c = Digraph('child')
        c.attr(rank='same')
        while nodoTemporal != None:

            if flag:   
                c = Digraph('child'+str(contSubgrap))
                contSubgrap += 1            
                c.attr(rank='same')
                flag = False

            contador += 1
            #depende si el nodo es 'B' o 'W'
            if nodoTemporal.color == 'B':
                c.node(str(contador), "black", color="black", group=str(contador%(x)))

            else:
                c.node(str(contador), "", fillcolor="white", group=str(contador%(x)))
            
            if contador%x == 0:
                dot.subgraph(c)
                flag = True
                

            nodoTemporal = nodoTemporal.siguiente

        #ahora trabajamos con el contador de 0 -> contador
        for i in range(1,contador):
            if i+x <= nuNodos:
                dot.edge(str(i), str(i+x))

            if i%x != 0:
                dot.edge(str(i), str(i+1))

        dot.view()
            