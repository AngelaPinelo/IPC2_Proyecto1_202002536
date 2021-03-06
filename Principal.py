#Todas las importaciones necesarias 
import xml.etree.ElementTree as ET
from PisosList import ListaPisos
from PatronesList import ListaPatrones
from ListaCasillas import CasillasList
from tkinter import filedialog

lista_pisos=ListaPisos()
lista_patrones=ListaPatrones()
lista_casillas=CasillasList()


    
def LeerPisos():
    route=filedialog.askopenfilename(initialdir="c:/", title="Escoge un archivo", filetypes= (("xml files" ,"*.xml"),("all files", "*.*")))
    elementTree(route)

def elementTree(ruta):
    tree = ET.parse(ruta)
    piso = tree.getroot()
    #para mi nodo piso
    for n in piso:
        rows= n[0]
        fila=rows.text
        fila=int(fila)
        column= n[1]
        c=column.text
        c=int(c)
        flip=n[2]
        f=flip.text
        f=int(f)
        slide=n[3]
        s=slide.text
        s=int(s)
        pisoNode=lista_pisos.insertNodeLast(n.attrib['nombre'],fila,c,f,s)
        #para mi nodo patron
        patrones= n[4]
        for patron in patrones:
            code=patron.attrib['codigo'].replace('\n','')
            cadena=patron.text.replace('\n','')
            cadena=cadena.replace(' ','')
            patronNode=lista_patrones.insertarPatronLast(code,cadena)
            
            #para mis casillas 
            entrada=patron.text.replace(' ','')
            entrada=entrada.replace('\n','')
            '''if len(entrada)<= fila:
                coordenaday=fila 
            elif len(entrada)>fila:'''
            for char in entrada:  
                        '''if char[fila+1]:
                          coordenaday=fila+1
                        else:
                          coordenaday= fila '''

                        
                    #print (char)
            
        casillaNode=lista_casillas.InsertarCasillaFinal(c,fila,char)
        
        
    
#elementTree('pisos.xml')
LeerPisos()
#lista_pisos.OrdenamientoBurbuja2()
lista_pisos.mostrarPisos()
#lista_patrones.mostrarPatrones()
lista_casillas.showCasillas()