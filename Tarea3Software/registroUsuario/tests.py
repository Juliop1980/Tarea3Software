from django.test import TestCase
from registroUsuario.seguridad import VerificarRegistro

# Create your tests here.
class FunctionsTester(TestCase):
    
    
    # primera prueba de test
    def testFirstRegister(self):
        self.assertTrue(VerificarRegistro("pepitogonzales@gmail.com", "Olabraa2", "Olabraa2"))
    
    #frontera: tiene 0 digitos la contrasena
    def testDigitsPassword(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmail.com", "Olabraa", "Olabraa"))
        
    
