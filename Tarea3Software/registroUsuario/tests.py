from django.test import TestCase
from registroUsuario.seguridad import VerificarRegistro

# Create your tests here.
class FunctionsTester(TestCase):
    
    
    # primera prueba de test
    def testFirstRegister(self):
        self.assertTrue(VerificarRegistro("pepitogonzales@gmail.com", "OOlabraa23", "OOlabraa23"))
    
    #frontera: tiene 0 digitos la contrasena
    def testZeroDigitsPassword(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmail.com", "OOlabraa", "OOlabraa"))
    
    #frontera: clave no valida falta .
    def testNotValidPassword(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@", "OOlabraa2", "OOlabraa2"))
        
    #frontera: clave tiene 1 digito
    def testOneDigitValidPassword(self):
        self.assertTrue(VerificarRegistro("pepitogonzales@gmail.com", "OOlabraa2", "OOlabraa2"))
        
    #frontera: clave tiene 2 letras
    def testTwoLettersPassword(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmail.com", "Ol22222", "Ol22222"))
    
    #frontera: clave tiene 3 letras
    def testThreeLetterPassword(self):
        self.assertTrue(VerificarRegistro("pepitogonzales@gmail.com", "Oll222222", "Oll222222"))
    
    
    
    
