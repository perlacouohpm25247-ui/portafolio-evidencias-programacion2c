import unittest

from cuenta import Cuenta
from banco import Banco

class TestIntegracionBanco(unittest.TestCase):

    def setUp(self):
        self.cuenta1 = Cuenta("Fulanito Perez", "001", 1000)
        self.cuenta2 = Cuenta("Perezcila Sanchez", "002")

        self.banco = Banco()

    def test_transferencia_exitosa(self):
        resultado = self.banco.transferir(self.cuenta1, self.cuenta2, 350)
        self.assertTrue(resultado, "Deberia reslizarce de manera correcta la transferencia")
        self.assertEqual(self.cuenta1.saldo, 650, "El saldo de la cuenta 1 deberia ser 650")
        self.assertEqual(self.cuenta2.saldo, 350, "El saldo de la cuenta destino deberia ser 350")

    def test_transferencia_saldo_insuficiente(self):
        result = self.banco.transferir(self.cuenta1, self.cuenta2, 1200)
        self.assertFalse(result, "La transferencia")
        self.assertEqual(self.cuenta1.saldo, 1000, "El saldo deberia mantenerse sin cambios")
        self.assertEqual(self.cuenta2, 0, "El saldo de la cuenta destino deberia de ser 0")