
from os import remove


listaClientes = []


def guardar_cliente():
    lista = []
    nombre = input("nombre completo: ")
    Celular = int(input("numero celular: "))
    cuenta = int(input("cuenta: "))

    lista.append(nombre)
    lista.append(Celular)
    lista.append(cuenta)
    listaClientes.append(lista)


def listar():
    if len(listaClientes) > 0:
        for lista in listaClientes:
            print(lista)
    else:
        print("lista vasia")


def buscar_cliente():
    encontrado = False
    nombre = input("ingrese el nombre: ")

    for i in range(len(listaClientes)):
        if (nombre == listaClientes[i][0]):
            encontrado = True
            pos = i
            break
    if(encontrado):
        print("")
        print("datos del usuario")
        print(listaClientes[pos])


def actualizar_Cliente():
    encontrado = False
    nombre = input("ingrese el nombre: ")

    for i in range(len(listaClientes)):
        if (nombre == listaClientes[i][0]):
            encontrado = True
            pos = i

            break
    if(encontrado):
        print("1 para modificar nombre: ")
        print("2 para modificar celular: ")
        print("3 para modificar cuenta: ")

        opcion2 = int(input("ingrese la opcion de actualizar: "))
        if opcion2 == 1:
            listaClientes[pos].remove(nombre)
            nuevonombre = input("ingrese el nuevo nombre:")
            listaClientes[pos].insert(0, nuevonombre)
        if opcion2 == 2:
            listaClientes[pos].remove(listaClientes[pos][1])
            nueCelular = int(input("ingrese el nuevo celular:"))
            listaClientes[pos].insert(1, nueCelular)
        if opcion2 == 3:
            print("1 para sumarle a la cuenta 2 para restarle a cuenta")
            opcion3 = int(
                input("ingrese la opcion para realizar la operacion: "))
            if opcion3 == 1:
                cuenta = int(input("ingrese la cuenta: "))
                resultado = int(listaClientes[pos][2]+cuenta)
                listaClientes[pos].remove(listaClientes[pos][2])
                listaClientes[pos].insert(2, resultado)
                print("la cuenta va en ", listaClientes[pos][2])

            if opcion3 == 2:
                cuenta = int(input("ingrese la cuenta: "))
                resultado = int(listaClientes[pos][2]-cuenta)
                listaClientes[pos].remove(listaClientes[pos][2])
                listaClientes[pos].insert(2, resultado)
                print("la cuenta va en: ", listaClientes[pos][2])


def menu():
    ("1 para ingresar ")
    print("1 para ingresar ")
    print("2 para listar ")
    print("3 para buscar cliente")
    print("4 actualizar al cliente ")
    print("5 para salir del sistema")

    print("ingrese la opcion")
    opcion = int(input())

    if opcion == 1:
        guardar_cliente()

    if opcion == 2:
        listar()
    if opcion == 3:
        buscar_cliente()
    if opcion == 4:
        actualizar_Cliente()
    if opcion == 5:
        exit()
    menu()


menu()
