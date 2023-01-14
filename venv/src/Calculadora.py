
import numpy as np
import os

class Calculadora:

    def menu(self):
        print("Seleccione el número de la opción deseada\n1.-Suma\n2.-Resta\n3.-Multiplicación\n4.-División\n5.-Raiz\n6.-Exponente\n7.-Seno\n8.-Coseno\n9.-Tangente\n0.-Salir")

    def clear(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "ce" or os.name == "nt" or os.name ==  "dos":
            os.system("cls")

    def suma(self):
        print("Modulo suma")

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
        cal.clear()
        cal.menu()
        opc = input("Selecciona una opción: ")
        try:
            sel = int(opc)
        except TypeError:
            raise TypeError(f"La opción debe ser un número entero, pero ingresó: '{opc}'")
        except ValueError:
            print("\nNo se seleccionó ningun valor")
            input("\nPresione enter para continuar...")
            continue
        if sel == 1:
            cal.suma()
        elif sel == 2:
            cal.resta()
        elif sel == 3:
            cal.multiplica()
        elif sel == 4:
            cal.divide()
        elif sel == 5:
            cal.raizn()
        elif sel == 6:
            cal.expn()
        elif sel == 7:
            cal.seno()
        elif sel == 8:
            cal.coseno()
        elif sel == 9:
            cal.tangente()
        elif sel == 0:
            salir = False
            break
        else:
            print("La opción seleccionada no es válida")
        input("\nPresione enter para continuar...")


if __name__ == "__main__":
    main()