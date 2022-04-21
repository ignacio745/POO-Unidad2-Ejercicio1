from ClaseManejadorEmails import ManejadorEmails
from ClaseEmail import Email
from Menu import Menu
from os import system

unMenu = Menu(["Elija una opcion", "Crear cuenta de email", "Modificar contraseña de la cuenta", "Crear cuenta a partir de direccion", "Leer csv", "Mostrar emails del csv", "Salir"])


unManejadorEmails = ManejadorEmails()

opcion = 0

while opcion != 6:
    opcion = unMenu.input()
    system("clear")
    if opcion == 1:
        nombre = input("Ingrese su nombre: ")
        identificador = input("Ingrese el identificador de la cuenta: ")
        dominio = input("Ingrese el dominio: ")
        tipoDominio = input("Ingrese el tipo de dominio: ")
        contraseña = input("Ingrese la contraseña: ")
        unEmail = Email(identificador, dominio, tipoDominio, contraseña)
        print ("Estimado {0}, te enviaremos tus mensajes a la direccion {1}".format(nombre, unEmail.retornaEmail()))
    
    elif opcion == 2:
        contraseñaActual = input("Ingrese la contraseña actual: ")
        contraseñaNueva = input("Ingrese la contraseña nueva: ")
        if unEmail.cambiarContraseña(contraseñaActual, contraseñaNueva):
            print ("Contraseña cambiada exitosamente")
        else:
            print ("No se pudo cambiar la contraseña")  
    elif opcion == 3:
        direccion = input("Ingrese la direccion para crear la cuenta: ")
        contraseña = input("Ingrese la contraseña: ")
        otroEmail = Email()
        if otroEmail.crearCuenta(direccion, contraseña):
            print ("Email creado")
        else:
            print ("[ERROR] Email no creado")


    elif opcion == 4:
        unManejadorEmails.cargarCSV("emails.csv")
        print("Emails cargados")
        identificador = input("Ingrese un identificador para comprobar si esta repetido o no: ")
        if unManejadorEmails.comprobarIdentificadoresIguales(identificador):
            print ("Hay más de un mail con ese identificador")
        else: print ("No hay más de un mail con ese identificador")
    
    elif opcion == 5:
        print(unManejadorEmails.listarEmails())
    
    if opcion != 6:
        input ("Presione Enter para continuar")