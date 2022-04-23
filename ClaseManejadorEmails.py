from ClaseEmail import Email
import re
import csv

class ManejadorEmails:
    __emails = []
    
    def __init__(self):
        self.__emails = []

    def agregarEmail(self, unEmail):
        if isinstance(unEmail, Email):
            self.__emails.append(unEmail)
    
    def agregarEmailAPartiDeDatos(self, idCuenta, dominio, tipoDominio, contraseña):
        unEmail = Email(idCuenta, dominio, tipoDominio, contraseña)
        self.agregarEmail(unEmail)


    def agregarEmailAPartirDeDireccion(self, direccion, contraseña):
        unEmail = Email()
        if (unEmail.crearCuenta(direccion, contraseña)):
            self.agregarEmail(unEmail)
        else:
            print("[ERROR] Email no agregado")

    

    def cargarCSV(self, nombreArchivo):
        self.__emails = []
        if isinstance(nombreArchivo, str) and re.match("[0-9a-zA-Z]+\.csv", nombreArchivo):
            archivo = open(nombreArchivo)
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                unEmail = Email()
                if unEmail.crearCuenta(fila[0], fila[1]):
                    self.agregarEmail(unEmail)
            archivo.close()



    def listarEmails(self):
        cadena = ""
        for unEmail in self.__emails:
            cadena += unEmail.retornaEmail() + "\n"
        return cadena
    
    def comprobarIdentificadoresIguales(self, identificador:str):
        cont = 0
        for unEmail in self.__emails:
            if unEmail.getIdentificador() == identificador:
                cont += 1
            if cont > 1:
                break

        return cont > 1