import xml.etree.ElementTree as ET


def elementTree(ruta):
    tree = ET.parse(ruta)
    piso = tree.getroot()
    for n in piso:
        patrones= n[4]
        print(n.attrib['nombre'])
        for r in n:
            print(r.text)
        for patron in patrones:
            print(patron.attrib['codigo'])
            print(patron.text)


    
elementTree('pisos.xml')