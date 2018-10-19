from django.test import TestCase
from registroUsuario.seguridad import VerificarRegistro

# Create your tests here.
class FunctionsTester(TestCase):
    
    def testFirstRegister(self):
        self.assertTrue(VerificarRegistro("pepitogonzales@gmail.com", "Olabraa2", "Olabraa2"))
