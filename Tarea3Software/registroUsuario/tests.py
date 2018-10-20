from django.test import TestCase
from registroUsuario.seguridad import Seguridad

class registrarUsuarioTester(TestCase):

    def setUp(self):
        self.clasePrueba = Seguridad()
    
    # Primera prueba: Prueba base
    def testFirstRegister(self):
        self.assertTrue(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "OOlabraa23", "OOlabraa23"))

    # Prueba de caso borde: Clave y su confirmacion no coinciden
    def testNoMatchingPasswords(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "OOlabraaaaa23", "OOlabraaa223"))
    
    # Prueba de caso borde: Clave tiene un caracter especial
    def testCaracteresEspeciales(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "hola-chao2H", "hola-chao2H"))
        
    # Prueba de caso borde: Correo invalido
    def testNotValidEmail(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("pepitogonzales@", "OOlabraa2", "OOlabraa2"))
    
    # Prueba de caso frontera: Clave no tiene digitos numericos
    def testZeroDigitsPassword(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "OOlabraaa", "OOlabraaa"))
        
    # Prueba de caso frontera: Clave tiene al menos un digito numerico
    def testOneDigitValidPassword(self):
        self.assertTrue(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "OOlabraa2", "OOlabraa2"))
    
    # Prueba de caso frontera: Clave tiene 3 letras
    def testThreeLetterPassword(self):
        self.assertTrue(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "Oll222222", "Oll222222"))
        
    # Prueba de caso frontera: Clave no tiene letras mayusculas
    def testZeroUpperCaseLettersPassword(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "sssll222222", "sssll222222"))
    
    # Prueba de caso frontera: Clave no tiene letras minusculas
    def testZeroLowerCaseLettersPassword(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "AAAAA222222", "AAAAA222222"))
    
    # Prueba de caso frontera: Clave tiene el minimo caracteres (8)
    def testHasLengthEight(self):
        self.assertTrue(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "ssAsOO23", "ssAsOO23"))
        
    # Prueba de caso frontera: Clave tiene elmaximo de caracteres (16)
    def testHasLengthSixteen(self):
        self.assertTrue(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "ssAsOO23ssAsOO23", "ssAsOO23ssAsOO23"))
    
    # Prueba de caso frontera: Clave tiene menos del minimo de caracteres (8)
    def testDebajoMin(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "Abcd123", "Abcd123"))

    # Prueba de caso frontera: Clave tiene mas del maximo de caracteres (17)
    def testEncimaMax(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "Abcdefgh123456789", "Abcdefgh123456789"))
    
    # Prueba de esquina: Clave tiene una letra mayuscula, una minuscula, pero no tiene el minimo de letras necesario
    def testTwoLettersPassword(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "Ol22222", "Ol22222"))
    
    # Prueba de esquina: Clave tiene tres letras, una es mayuscula
    def testHasOneUpperLetterAndThreeLetters(self):
        self.assertTrue(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "Abc123124", "Abc123124"))
    
    # Prueba de esquina: Correo invalido, y clave y verificacion no coinciden
    def testInvalidEmailNotMatchingPassword(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("pepitogonzales@gmailcom", "Abc12312", "Abc123124"))
        
    # Prueba de esquina: Clave tiene dos letras y ninguna mayuscula
    def testHasZeroUpperLetterAndTwoLetters(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "bc123124", "bc123124"))
    
    # Prueba de esquina: Clave tiene un digito numerico y una mayuscula
    def testOneDigitAndOneUpperCase(self):
        self.assertTrue(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "Abcbcsdgf1", "Abcbcsdgf1"))
    
    # Prueba de esquina: Clave tiene un digito numerico y una minuscula
    def testOneDigitAndOneLowerCase(self):
        self.assertTrue(self.clasePrueba.registrarUsuario("pepitogonzales@gmail.com", "AAAAAAb1", "AAAAAAb1"))
        
    # Prueba de malicia: Correo solo posee "@."
    def testSoloCaracteresEspecialesEmail(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("@.", "AAAAAAb1", "AAAAAAb1"))
        
    # Prueba de malicia: Correo solo posee "@.com"
    def testSoloCom(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("@.com", "AAAAAAb1", "AAAAAAb1"))
        
    # Prueba de malicia: Correo esta escrito al reves
    def testReverseEmail(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("moc.liamg@selaz", "AAAAAAb1", "AAAAAAb1"))
        
    # Prueba de malicia: Confirmacion de la clave esta escrita al reves de la clave
    def testReversePassword(self):
        self.assertFalse(self.clasePrueba.registrarUsuario("moc.liamg@selaz", "AAAAAAb1", "1bAAAAAA"))
        
    
class IngresarUsuarioTester(TestCase):

    def setUp(self):
        self.clasePrueba = Seguridad()
        self.clasePrueba.my_dict =    {
              "pepitogonzales@gmail.com" : "32aarbalOO",
              "pepitomater@gmail.com" :"2aarbalOO",
              "andreacolliani@hotmail.com": "432rereeA"
            }
    
    # Primera prueba de ingreso
    def testPrimerIngreso(self):
        self.assertTrue(self.clasePrueba.IngresarUsuario("pepitogonzales@gmail.com", "OOlabraa23"))

    # Prueba de caso borde: Positivo
    def testIngresoPositivo(self):
        self.assertTrue(self.clasePrueba.IngresarUsuario("pepitomater@gmail.com" ,"OOlabraa2"))

    # Prueba de caso borde: Negativo
    def testIngresoNegativo(self):
        self.assertFalse(self.clasePrueba.IngresarUsuario("pepitogonzales@gmail.com", "OOlabraa"))
    
    
    
