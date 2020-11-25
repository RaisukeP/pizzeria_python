import itertools as it
import precio
import time

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


def start():
    orden = {}
    print(23*'*')
    print('*    PIZZERIA UCAB    *')
    print(23*'*')

    total = 0
    for conteo_pizzas in it.count(1,1): #Loop infinito para tomar las pizzas del pedido
        print('Pizza numero '+ str(conteo_pizzas))
        print()
        print('Opciones:')

        #INICIA EL PROCESO DE RECOLECCION DE DATOS

        tamaño = ''
        nombre = ''
        while (tamaño != 'p' and tamaño != 'm' and tamaño != 'g'): #Seleccionar tamaño

            tamaño = input('Tamaños: Personal 280$ ( p ) Mediana 430$ ( m ) Grande 580$ ( g ): ')
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
        print('Jamon 40$            (ja)')
        print('Champiñones 35$      (ch)')
        print('Pimentón 30$         (pi)')
        print('Doble Queso 40$      (dq)')
        print('Aceitunas 57,5$      (ac)')
        print('Pepperoni 35,5$      (pp)')
        print('Salchichón 65,5$     (sa)')
        print()
        ingredientes = []
        ing_sel = 'x'
        confirmar = False

        while confirmar == False:

            while ing_sel != '': #Seleccionar ingredientes adicionales

                print('Actualmente: '+ str(ingredientes))
                ing_sel = input('Indique ingrediente (ENTER para terminar): ').lower()

                if ing_sel in ING:
                    if ing_sel in ingredientes:
                        ingredientes.remove(ing_sel)
                    else:
                        ingredientes.append(ing_sel)
                elif ing_sel == '':
                    pass
                else:
                    print('=> Debe seleccionar algun ingrediente o finalizar con ENTER')

            if ingredientes == []: #Agrega el nombre de la pizza en caso de ser uno predeterminado
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
                        print()

            respuesta =''
            while respuesta != 's' and respuesta != 'n':

                respuesta = input('Es correcto? [s/n]: ').lower()
                if respuesta != 's' and respuesta != 'n':
                    print('=> Input invalida')
            if respuesta == 's':
                confirmar = True
                break
            else:
                ing_sel = 'x'
        print()

        #Calculo del precio con el modulo precio.py
        subtotal = precio.calcular_precio(tamaño, ingredientes)
        total += subtotal
        print('Subtotal a pagar por la pizza: ' + str(subtotal))

        #Se guardan las pizzas del pedido en una lista para luego ser almacenadas como un recibo
        orden[conteo_pizzas] = {
            'tamaño': tamaño,
            'ingredientes': ingredientes,
            'nombre': nombre,
            'monto': subtotal
        }
        print()

        #Pregunta para continuar con el pedido o no
        continuar = ''
        while continuar.lower() != 'n' and continuar.lower() != 's':
            continuar = input('Desea agregar otra pizza al pedido? s/n: ')
            if continuar.lower() != 'n' and continuar.lower() != 's':
                print('=> Seleccione una opcion valida!!! [s/n]')
        
        if continuar.lower() == 'n':
            print('El pedido tiene un total de '+ str(conteo_pizzas) +' por un total de '+ str(total))
            print()
            print('Gracias por su compra, regrese pronto!!')
            time.sleep(2)
            break

        print(42 * '*')
        
    return orden