from os import system


class Menu:
    opciones = []
    
    def __init__(self, opciones = []):
        if (type(opciones) == list):
            todoOraciones = True
            for i in opciones:
                if (type(i) != str):
                    todoOraciones = False
                    break
            if(todoOraciones):
                self.opciones = opciones
            else:
                print("ERROR en creacion de menu, una de las opciones no era un string")
        else:
            print("ERROR en creacion de menu, debe ingresar una lista de strings como parámetro")

    def __str__(self):
        texto = self.opciones[0]+"\n"
        for i in range(1, len(self.opciones)):
            texto += "[" + str(i) + "]" + " " + self.opciones[i] + "\n"
        texto += "--> "
        return(texto)

    def input(self):
            system("clear")
            opcion = 0
            while((opcion <= 0) or (opcion > len(self.opciones)-1)):
                opcionIngresada = input(self)
                if opcionIngresada.isnumeric():
                    opcion = int(opcionIngresada)
                    if ((opcion <= 0) or (opcion > len(self.opciones)-1)):
                        print("Numero invalido")
                        input("Presione Enter para continuar")
                else:
                    print("No se ingreso un numero")
                    input("Presione Enter para continuar")
            return(opcion)