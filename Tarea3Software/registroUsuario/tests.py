from django.test import TestCase
from registroUsuario.seguridad import VerificarRegistro

# Create your tests here.
class FunctionsTester(TestCase):
    
    
    # primera prueba de test
    def testFirstRegister(self):
        self.assertTrue(VerificarRegistro("pepitogonzales@gmail.com", "OOlabraa23", "OOlabraa23"))

    #prueba de borde: claves no coinciden
    def testNoMatchingPasswords(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmail.com", "OOlabraaaaa23", "OOlabraaa223"))
    
    #Borde Falla al tener un caracter especial
    def testCaracteresEspeciales(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmail.com", "hola-chao2H", "hola-chao2H"))
        
    #Borde:email no valido
    def testNotValidEmail(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@", "OOlabraa2", "OOlabraa2"))
    
    #frontera: tiene 0 digitos la contrasena
    def testZeroDigitsPassword(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmail.com", "OOlabraaa", "OOlabraaa"))
        
    #frontera: clave tiene 1 digito
    def testOneDigitValidPassword(self):
        self.assertTrue(VerificarRegistro("pepitogonzales@gmail.com", "OOlabraa2", "OOlabraa2"))
    
    #frontera: clave tiene 3 letras
    def testThreeLetterPassword(self):
        self.assertTrue(VerificarRegistro("pepitogonzales@gmail.com", "Oll222222", "Oll222222"))
        
    #frontera: clave tiene 0 mayusculas
    def testZeroUpperCaseLettersPassword(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmail.com", "sssll222222", "sssll222222"))
    
    #frontera: clave tiene 0 minusculas
    def testZeroLowerCaseLettersPassword(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmail.com", "AAAAA222222", "AAAAA222222"))
    
    #frontera: clave tiene 8 caracteres
    def testHasLengthEight(self):
        self.assertTrue(VerificarRegistro("pepitogonzales@gmail.com", "ssAsOO23", "ssAsOO23"))
        
    #frontera: clave tiene 16 caracteres
    def testHasLengthSixteen(self):
        self.assertTrue(VerificarRegistro("pepitogonzales@gmail.com", "ssAsOO23ssAsOO23", "ssAsOO23ssAsOO23"))
    
    # frontera: Falla al tener longitud 7
    def testDebajoMin(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmail.com", "Abcd123", "Abcd123"))

    # frontera: Falla al tener longitud 17
    def testEncimaMax(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmail.com", "Abcdefgh123456789", "Abcdefgh123456789"))
    
    #esquina: clave tiene 2 letras, una mayus y una minus
    def testTwoLettersPassword(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmail.com", "Ol22222", "Ol22222"))
    
    # esquina: Esquina tiene 1 mayus y 3 letras
    def testHasOneUpperLetterAndThreeLetters(self):
        self.assertTrue(VerificarRegistro("pepitogonzales@gmail.com", "Abc123124", "Abc123124"))
    
    # esquina: Email invalido y contrasena invalida
    def testInvalidEmailNotMatchingPassword(self):
        self.assertFalse(VerificarRegistro("pepitogonzales@gmailcom", "Abc12312", "Abc123124"))
    
    
    
    
