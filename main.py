import xml.etree.ElementTree as ET
from PisosList import ListaPisos

lista_pisos=ListaPisos()


def elementTree(ruta):
    tree = ET.parse(ruta)
    piso = tree.getroot()
   #para mi nodo piso
    for n in piso:
        nombre= n.attrib['nombre']
        name=nombre
        row= n[0]
        r=row.text
        r=int(r)
        column= n[1]
        c=column.text
        c=int(c)
        flip=n[2]
        f=flip.text
        f=int(f)
        slide=n[3]
        s=slide.text
        s=int(s)
        pisoNode=lista_pisos.insertNodeLast(name,r,c,f,s)
        #para mi nodo patron
        patrones= n[4]
        for patron in patrones:
            code=patron.attrib['codigo']
            cadena=patron.text
            print(code)
            print(cadena)
        

    
elementTree('pisos.xml')