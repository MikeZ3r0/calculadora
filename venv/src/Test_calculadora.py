import unittest
from src.Calculadora import *


class TestClaculadora(unittest.TestCase):
    
    def test_suma_numeros(self):
        self.assertEqual(Calculadora.suma(self,5,8), 13)
        self.assertEqual(Calculadora.suma(self,10.5,0.7), 11.2)
        self.assertEqual(Calculadora.suma(self,5,0.7), 5.7)
        self.assertEqual(Calculadora.suma(self,-5.5, -4.5), -10)
        self.assertEqual(Calculadora.suma(self,10,-1), 9)

    def test_resta_numeros(self):
        self.assertEqual(Calculadora.resta(self,15,8), 7)
        self.assertEqual(Calculadora.resta(self,10.5,0.7), 9.8)
        self.assertEqual(Calculadora.resta(self,5,0.7), 4.3)
        self.assertEqual(Calculadora.resta(self,-5.5, -4.5), -1)
        self.assertEqual(Calculadora.resta(self,10,-1), 11)

    def test_multiplica_numeros(self):
        self.assertEqual(Calculadora.multiplica(self,5,8), 40)
        self.assertEqual(Calculadora.multiplica(self,1.5,0.5), 0.75)
        self.assertEqual(Calculadora.multiplica(self,5,0.7), 3.5)
        self.assertEqual(Calculadora.multiplica(self,-5, -4.), 20)
        self.assertEqual(Calculadora.multiplica(self,10,-1), -10)

    def test_divide_numeros(self):
        self.assertEqual(Calculadora.divide(self, 40, 8), 5)
        self.assertEqual(Calculadora.divide(self,1.8,0.2), 9.0)
        self.assertEqual(Calculadora.divide(self,10,0.5), 20)
        self.assertEqual(Calculadora.divide(self,-50, -2.), 25)
        self.assertEqual(Calculadora.divide(self,10,-1), -10)

    def test_exponente_numeros(self):
        self.assertEqual(Calculadora.expn(self,2,8), 256)
        self.assertEqual(Calculadora.expn(self,80,0), 1)
        self.assertEqual(Calculadora.expn(self,9,0.5), 3)
        self.assertEqual(Calculadora.expn(self,-5, 2), 25)
        self.assertEqual(Calculadora.expn(self,10,-1), 0.1)

    def test_raiz_numeros(self):
        self.assertEqual(Calculadora.raizn(self,40,1), 40)
        self.assertEqual(Calculadora.raizn(self,81,2), 9.0)
        self.assertEqual(Calculadora.raizn(self,10,0.5), 100)
        self.assertEqual(Calculadora.raizn(self,100,-2), 0.1)

    def test_seno_notable(self):
        self.assertEqual(Calculadora.seno(self,0), 0)
        self.assertEqual(Calculadora.seno(self,30), 0.5)
        self.assertEqual(Calculadora.seno(self,90), 1)
        self.assertEqual(Calculadora.seno(self,180), 0)
        self.assertEqual(Calculadora.seno(self,270), -1)
        self.assertEqual(Calculadora.seno(self,360), 0)

    def test_coseno_notable(self):
        self.assertEqual(Calculadora.coseno(self,0), 1)
        self.assertEqual(Calculadora.coseno(self,60), 0.5)
        self.assertEqual(Calculadora.coseno(self,90), 0)
        self.assertEqual(Calculadora.coseno(self,180), -1)
        self.assertEqual(Calculadora.coseno(self,270), 0)
        self.assertEqual(Calculadora.coseno(self,360), 1)

    def test_tangente_notable(self):
        self.assertEqual(Calculadora.tangente(self,0), 0)
        self.assertEqual(Calculadora.tangente(self,45), 1)
        self.assertEqual(Calculadora.tangente(self,180), 0)
        self.assertEqual(Calculadora.tangente(self,360), 0)

    @unittest.skip('Falta implementacion de errores')
    def test_suma_TypeError(self):
        with self.assertRaises(TypeError):
            Calculadora.suma(self,"a",-1)

if __name__ == '__main__':
    unittest.main()