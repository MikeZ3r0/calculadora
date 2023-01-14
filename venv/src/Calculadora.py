
import numpy as np
import os

class Calculadora:

    def menu(self):
        self.clear()
        entrada = [1, 1]
        resultado = 0
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
            self.clear()
            print("Modulo de Suma\n")
            entrada[0] = input("Ingresa la primera cifra: ")
            entrada[1] = input("Ingresa la segunda cifra: ")
            resultado = self.suma(entrada[0], entrada[1])
        elif sel == 2:
            self.clear()
            print("Modulo de Resta\n")
            entrada[0] = input("Ingresa la primera cifra: ")
            entrada[1] = input("Ingresa la segunda cifra: ")
            resultado = self.resta(entrada[0], entrada[1])
        elif sel == 3:
            self.clear()
            print("Modulo de Multiplicación\n")
            entrada[0] = input("Ingresa la primera cifra: ")
            entrada[1] = input("Ingresa la segunda cifra: ")
            resultado = self.multiplica(entrada[0], entrada[1])
        elif sel == 4:
            self.clear()
            print("Modulo de División\n")
            entrada[0] = input("Ingresa el dividendo: ")
            entrada[1] = input("Ingresa el divisor: ")
            resultado = self.divide(entrada[0], entrada[1])
        elif sel == 5:
            self.clear()
            print("Modulo de Raiz\n")
            entrada[0] = input("Ingresa la base: ")
            entrada[1] = input("Ingresa el exponente de la raiz: ")
            resultado = self.raizn(entrada[0], entrada[1])
        elif sel == 6:
            self.clear()
            print("Modulo de Exponente\n")
            entrada[0] = input("Ingresa la base: ")
            entrada[1] = input("Ingresa el exponente: ")
            resultado = self.expn(entrada[0], entrada[1])
        elif sel == 7:
            self.clear()
            print("Modulo de Seno en grados\n")
            entrada[0] = input("Ingresa el ángulo: ")
            resultado = self.seno(entrada[0])
        elif sel == 8:
            self.clear()
            print("Modulo de Coseno en grados\n")
            entrada[0] = input("Ingresa el ángulo: ")
            resultado = self.coseno(entrada[0])
        elif sel == 9:
            self.clear()
            print("Modulo de Tangente en grados\n")
            entrada[0] = input("Ingresa el ángulo: ")
            resultado = self.tangente(entrada[0])
        elif sel == 0:
            return False
        else:
            print("La opción seleccionada no es válida")
        print(f"El resultado es: {resultado}")
        input("\nPresione enter para continuar...")
        return True

    def clear(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "ce" or os.name == "nt" or os.name ==  "dos":
            os.system("cls")

    def suma(self, x, y):
        try:
            x = float(x)
            y = float(y)
            resultado = x + y
        except Exception as err:
            print("Error detectado: ", err)
        return resultado


    def resta(self, x, y):
        try:
            x = float(x)
            y = float(y)
            resultado = x - y
        except Exception as err:
            print("Error detectado: ", err)
        return resultado
    
    def multiplica(self, x, y):
        try:
            x = float(x)
            y = float(y)
            resultado = x * y
        except Exception as err:
            print("Error detectado: ", err)
        return resultado
    
    def divide(self, x, y):
        try:
            x = float(x)
            y = float(y)
            resultado = x / y
        except Exception as err:
            print("Error detectado: ", err)
        return resultado
    
    def raizn(self, base, exp):
        try:
            base = float(base)
            exp = float(exp)
            resultado = np.power(base, (1/exp))
        except Exception as err:
            print("Error detectado: ", err)
        return resultado

    def expn(self, base, exp):
        try:
            base = float(base)
            exp = float(exp)
            resultado = np.power(base, exp)
        except Exception as err:
            print("Error detectado: ", err)
        return resultado

    def seno(self, angulo, degree=True):
        try:
            angulo = float(angulo)
            if degree:
                angulo = np.pi/180 * angulo
            resultado = np.sin(angulo)
        except Exception as err:
            print("Error detectado: ", err)
        return np.round(resultado,2)

    def coseno(self, angulo, degree=True):
        try:
            angulo = float(angulo)
            if degree:
                angulo = np.pi/180 * angulo
            resultado = np.cos(angulo)
        except Exception as err:
            print("Error detectado: ", err)
        return np.round(resultado,2)

    def tangente(self, angulo, degree=True):
        try:
            angulo = float(angulo)
            if degree:
                angulo = np.pi/180 * angulo
            resultado = np.tan(angulo)
        except Exception as err:
            print("Error detectado: ", err)
        return np.round(resultado,2)




def main():
    salir = True
    cal = Calculadora()
    while(salir):
        salir = cal.menu()

if __name__ == "__main__":
    main()