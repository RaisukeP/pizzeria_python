import pedido
import os
import platform

pedidos = []

def limpiar():
    if (platform.system() == "Windows"):
        os.system('cls')
    else:
        os.system('clear')

def main():

    terminar = False
    conteo_pedidos = 0
    while (terminar != False):
        limpiar()
        conteo_pedidos += 1
        respuesta = ''
        print('||==> Bienvenido a Pizzeria UCAB <==||')
        print()
        print('1. Realizar un pedido')
        print('2. Mostrar los pedidos que se han realizado para la sesion')
        print('3. Salir')
        print('___________________________________________________________')
        while (respuesta != '1' and respuesta != '2' and respuesta != '3'):
            respuesta = input('Opcion #')
            if (respuesta == '1'):
                limpiar()
                pedidos.append(pedido.start())
            elif (respuesta == '2'):
                
                print()
            elif (respuesta == '3'):
                terminar = True
                print()
                print('Hasta pronto!!!')
            else:
                print('=> Input invalido, seleccione la opcion 1, 2 o 3!!')

        

if __name__ == '__main__':
    main()