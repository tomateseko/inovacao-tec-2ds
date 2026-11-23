# test_calculadora.py
import unittest
from calculadora import soma, subtrai, multiplica, divide


class TestCalculadora(unittest.TestCase):

    def confirmar(self, mensagem):
        print(f"✔ [OK] {mensagem}")

    def test_soma(self):
        self.assertEqual(soma(1, 2), 3)
        self.confirmar("Soma de positivos: 1 + 2 = 3")

        self.assertEqual(soma(-1, 1), 0)
        self.confirmar("Soma de negativo com positivo: -1 + 1 = 0")

        self.assertEqual(soma(-1, -1), -2)
        self.confirmar("Soma de negativos: -1 + (-1) = -2")

    def test_subtrai(self):
        self.assertEqual(subtrai(10, 5), 5)
        self.confirmar("Subtração de positivos: 10 - 5 = 5")

        self.assertEqual(subtrai(-1, -1), 0)
        self.confirmar("Subtração de negativos iguais: -1 - (-1) = 0")

        self.assertEqual(subtrai(0, 1), -1)
        self.confirmar("Subtração com zero: 0 - 1 = -1")

    def test_multiplica(self):
        self.assertEqual(multiplica(3, 7), 21)
        self.confirmar("Multiplicação de positivos: 3 * 7 = 21")

        self.assertEqual(multiplica(-1, 1), -1)
        self.confirmar("Multiplicação com sinal negativo: -1 * 1 = -1")

        self.assertEqual(multiplica(0, 10), 0)
        self.confirmar("Multiplicação por zero: 0 * 10 = 0")

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.confirmar("Divisão exata: 10 / 2 = 5")

        self.assertEqual(divide(-10, 2), -5)
        self.confirmar("Divisão com dividendo negativo: -10 / 2 = -5")

        with self.assertRaises(ValueError):
            divide(10, 0)
        self.confirmar("Divisão por zero bloqueada com ValueError")


if __name__ == '__main__':
    unittest.main(verbosity=2)
