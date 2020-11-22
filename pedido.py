import itertools as it

#Diccionario para comprobar los codigos y mostrar los nombres en pantalla
ING = { 'ja': 'Jamon', 
        'ch': 'Champiñon', 
        'pi': 'Pimentón', 
        'dq': 'Doble Queso', 
        'ac': 'Aceitunas', 
        'pp': 'Pepperoni', 
        'sa': 'Salchichón'
}

TAM = { 'p': 'Personal',
        'm': 'Mediana',
        'g': 'Grande'
}

print(23*'*')
print('*    PIZZERIA UCAB    *')
print(23*'*')

for conteo_pizzas in it.count(1,1): #Loop infinito para tomar las pizzas del pedido
    print('Pizza numero '+ str(conteo_pizzas))
    print()
    print('Opciones:')

    #INICIA EL PROCESO DE RECOLECCION DE DATOS

    tamaño = ''
    nombre = ''
    while (tamaño != 'p' and tamaño != 'm' and tamaño != 'g'):
        tamaño = input('Tamaños: Personal ( p ) Mediana ( m ) Grande ( g ): ')
        if (tamaño == 'p'):
            print('Tamaño seleccionado: Personal')
            print()
        elif (tamaño == 'm'):
            print('Tamaño seleccionado: Mediana')
            print()
        elif (tamaño == 'g'):
            print('Tamaño seleccionado: Grande')
            print()
        else:
            print('=> Debe seleccionar el tamaño correcto!!')

    print('Ingredientes:')
    print('Jamon           (ja)')
    print('Champiñones     (ch)')
    print('Pimentón        (pi)')
    print('Doble Queso     (dq)')
    print('Aceitunas       (ac)')
    print('Pepperoni       (pp)')
    print('Salchichón      (sa)')
    print()
    ingredientes = []
    ing_sel = 'x'

    while (ing_sel != ''):
        ing_sel = input('Indique ingrediente (ENTER para terminar): ')

        if ing_sel in ING:
            ingredientes.append(ing_sel)
        elif ing_sel == '':
            pass
        else:
            print('=> Debe seleccionar algun ingrediente o finalizar con ENTER')

    ingredientes = list(set(ingredientes))
    if ingredientes == []:
        nombre = 'Margarita'
        print('Usted selecciono una pizza '+ TAM.get(tamaño) + ' tipo ' + nombre)
    else:
        nombre = ''
        print('Usted selecciono una pizza '+ TAM.get(tamaño) + ' con', end=' ')
        aux = 0
        for x in ingredientes:
            aux += 1
            if aux < len(ingredientes):
                print(ING.get(x), end=', ')
            else:
                print(ING.get(x))