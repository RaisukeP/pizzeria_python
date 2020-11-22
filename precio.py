tamaño = {"personal":280, "mediana":430, "grande": 580}
ingredientes = {
    "jamon":40, 
    "champiñones":35, 
    "pimenton":30, 
    "doble queso":40, 
    "aceitunas":57.5, 
    "pepperoni":38.5, 
    "salchichon":65.5
}

def calcular_precio (tam,ing):
    total=0
    for nombre in ing:
        total += ingredientes.get(nombre)
    total += tamaño.get(tam)
    return total