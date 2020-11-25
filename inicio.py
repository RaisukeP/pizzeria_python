import pedido
import os
import platform

def limpiar(): #Funcion encargada de limpiar la terminal
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def main():

    pedidos = list()
    terminar = False

    while terminar == False:
        limpiar()
        respuesta = ''

        print('||==> Bienvenido a Pizzeria UCAB <==||')
        print()
        print('1. Realizar un pedido')
        print('2. Mostrar los pedidos que se han realizado para la sesion')
        print('3. Salir')
        print('___________________________________________________________')

        #Inicio de la aplicacion
        while respuesta != '1' and respuesta != '2' and respuesta != '3':
            respuesta = input('Opcion #')

            #Opcion 1
            if respuesta == '1':
                limpiar()
                pedidos.append(dict(pedido.start()))

            #Opcion 2
            elif respuesta == '2':
                limpiar()
                seleccion = 'x'

                if len(pedidos) == 0: #Envia mensaje de que no existe ningun registro
                    print('No existe ningun pedido registrado')
                    print('=> Presione ENTER')
                    input()
                    seleccion = ''


                if seleccion != '': #En caso de que exista por lo menos 1, sigue
                    print('Que pedido desea ver? ||ENTER para salir||')
                    print('Existentes: ' + str(len(pedidos)))
                    existentes = []

                    for i in range(1,len(pedidos)+1): #Para asegurar que escriba una opcion valida
                        existentes.append(str(i))
                
                    while seleccion != '': #Muestra los pedidos dependiendo de los ya existentes
                        print(50*'_')
                        seleccion = input('Pedido #:')

                        #Input correcto, se comienza a mostrar el pedido
                        if seleccion in existentes:
                            orden = dict(pedidos[int(seleccion)-1])
                            total = 0

                            for x in range(1,len(orden)+1):
                                aux = orden.get(x)
                                print(20*'*')
                                print('Pizza #'+ str(x))
                                print('Tamaño: '+ pedido.TAM.get(aux.get('tamaño')))

                                if aux.get('nombre') != '':
                                    print('Nombre: '+ aux.get('nombre'))
                                if aux.get('ingredientes') != []:
                                    print('Ingredientes: ',end='')
                                    num = 0
                                    for x in aux.get('ingredientes'):
                                        num += 1
                                        if num < len(aux.get('ingredientes')):
                                            print(pedido.ING.get(x), end=', ')
                                        else:
                                            print(pedido.ING.get(x))

                                print('Monto: '+ str(aux.get('monto')))
                                print(20*'*')
                                total += aux.get('monto')

                            print('Total a pagar: '+ str(total))
                            orden.clear()

                        elif seleccion == '': #En caso de no ingresar nada, finaliza
                            pass

                        else: #Se muestra un mensaje si introdujo una input invalida
                            print('=> Seleccione un pedido existente o regrese con ENTER!!')


            elif respuesta == '3': #Sale de la aplicacion
                terminar = True
                print()
                print('Hasta pronto!!!')
            else:
                print('=> Input invalido, seleccione la opcion 1, 2 o 3!!')

        

if __name__ == '__main__':
    main()