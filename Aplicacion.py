import xml.etree.ElementTree as ET
from PisosList import ListaPisos
from PatronesList import ListaPatrones
from ListaCasillas import CasillasList
from tkinter import filedialog

lista_pisos=ListaPisos()
lista_patrones=ListaPatrones()
lista_casillas=CasillasList()

class Aplicacion():
    def __init__(self):
        self.app()
        self.routa=""
        
    def LeerPisos(self):
        route=filedialog.askopenfilename(initialdir="c:/", title="Escoge un archivo", filetypes= (("xml files" ,"*.xml"),("all files", "*.*")))
        self.routa=route
        self.elementTree()
        
    def elementTree(self):
        ruta= self.routa
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
                entrada=patron.text.replace(' ','')
                entrada=entrada.replace('\n','')
                for char in entrada:
                    casillaNode=lista_casillas.InsertarCasillaFinal(c,fila,char)
    def app(self):
        while True: 
            opcion = input('''
1. Cargar Pisos
2. Ver pisos
3. Ver pisos ordenados
4. Ver patrones
5. Ver Casillas
6. Salir
Selecciona una opcion: ''')
            if opcion =='1':
                self.LeerPisos()              
            elif opcion =='2':
                lista_pisos.mostrarPisos()
            elif opcion =='3': 
                lista_pisos.OrdenamientoBurbuja2()
                lista_pisos.mostrarPisos()
            elif opcion =='4':
                lista_patrones.mostrarPatrones()   
            elif opcion =='5': 
                lista_casillas.showCasillas()
            elif opcion =='6':
                print("Gracias por usar nuestro sistema :)") 
                break
            else:
                print("Por Favor ingrese una opción válida")  

a=Aplicacion()

        