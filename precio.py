tamaño = {'p':280, 'm':430, 'g': 580}
ingredientes = {
    'ja':40, 
    'ch':35, 
    'pi':30, 
    'dq':40, 
    'ac':57.5, 
    'pp':38.5, 
    'sa':65.5
}

def calcular_precio (tam,ing):
    total=0
    for nombre in ing:
        total += ingredientes.get(nombre)
    total += tamaño.get(tam)
    return total