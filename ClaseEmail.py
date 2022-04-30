import re

class Email:
    __idCuenta = ""
    __dominio = ""
    __tipoDominio = ""
    __contraseña = ""

    def __init__(self, idCuenta="", dominio="", tipoDominio="", contraseña=""):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contraseña = contraseña

    def retornaEmail(self):
        email = self.__idCuenta + "@" + self.__dominio + "." + self.__tipoDominio
        return email
    
    def getIdentificador(self):
        return self.__idCuenta

    def getDominio(self):
        return self.__dominio

    def getTipoDominio(self):
        return self.__tipoDominio

    def cambiarContraseña(self, contraseña, nuevaContraseña):
        band = False
        if isinstance(nuevaContraseña, str):
            if self.__contraseña == contraseña:
                self.__contraseña = nuevaContraseña
                band = True
        return band

    def crearCuenta(self, direccion:str, contraseña, antiguaContraseña=""):
        band = False
        if isinstance(direccion, str):
            expresion = "[A-Za-z0-9\.\-\_]+@[a-z]+\.[a-z]{2,5}"
            if re.match(expresion, direccion) and self.cambiarContraseña(antiguaContraseña, contraseña):
                partes = direccion.split("@")
                idCuenta = partes[0]
                partes = partes[1].split(".")
                dominio = partes[0]
                tipoDominio = partes[1]
                self.__idCuenta = idCuenta
                self.__dominio = dominio
                self.__tipoDominio = tipoDominio
                band = True
        return band

    
    def __str__(self):
        return "Identificador: {0}\nDominio: {1}\nTipo de dominio {2}\nDireccion completa: {3}".format(self.getIdentificador(), self.getDominio(), self.getTipoDominio(), self.retornaEmail())
