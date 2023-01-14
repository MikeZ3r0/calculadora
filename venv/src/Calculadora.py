
import numpy as np
import os

class Calculadora:

    def menu(self):
        self.clear()
        operaciones = ["Salir","Suma","Resta", "Multiplicacion", "Division", "Raiz", "Exponente", "Seno", "Coseno", "Tangente"]
        print("Seleccione el número de la opción deseada:\n")
        for n in range(len(operaciones)):
            print(f"{n}.-{operaciones[n]}\n")
        opc = input("Selecciona una opción: ")
        try:
            sel = int(opc)
        except TypeError:
            raise TypeError(f"La opción debe ser un número entero, pero ingresó: '{opc}'")
        except ValueError:
           sel = -1
        if sel == 1:
            self.suma()
        elif sel == 2:
            self.resta()
        elif sel == 3:
            self.multiplica()
        elif sel == 4:
            self.divide()
        elif sel == 5:
            self.raizn()
        elif sel == 6:
            self.expn()
        elif sel == 7:
            self.seno()
        elif sel == 8:
            self.coseno()
        elif sel == 9:
            self.tangente()
        elif sel == 0:
            return False
        else:
            print("La opción seleccionada no es válida")
        input("\nPresione enter para continuar...")
        return True

    def clear(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "ce" or os.name == "nt" or os.name ==  "dos":
            os.system("cls")

    def suma(self):
        self.clear()
        print("Modulo suma\n")
        num_1 = input("Ingrese primera cifra")

    def resta(self):
        print("Modulo resta")
    
    def multiplica(self):
        print("Modulo multiplicación")
    
    def divide(self):
        print("Modulo divición")
    
    def raizn(self):
        print("Modulo raiz n")

    def expn(self):
        print("Modulo exponente n")

    def seno(self):
        print("Modulo seno")

    def coseno(self):
        print("Modulo coseno")

    def tangente(self):
        print("Modulo tangente")




def main():
    salir = True
    cal = Calculadora()
    while(salir):
        salir = cal.menu()

if __name__ == "__main__":
    main()