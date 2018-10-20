import re


class Seguridad:

    def __init__(self):
        self.my_dict = {}

    # Funcion que recibe el correo que se desea registrar, su clave asignada y la confirmacion de la clave
    def registrarUsuario(self,correo, clave1, clave2):
        resultado = self.VerificarClavesCoinciden(clave1, clave2) and self.ValidarCorreo(correo) and self.ValidarClave(clave1)
        clave_dict = clave1[::-1]
        if resultado == True:
            self.my_dict[correo] = clave_dict
        return resultado

    # Funcion que verifica que la clave cumple con los requisitos necesarios
    def ValidarClave(self,clave):
        validacion1 = self.ValidarLongitudClave(clave) 
        validacion2 = self.ValidarNoCaracteresEspeciales(clave)
        validacion3 = self.ContieneAlMenosTresLetras(clave)
        validacion4 = self.ContieneAlMenosUnaMayuscula(clave) 
        validacion5 = self.ContieneAlMenosUnaMinuscula(clave)
        validacion6 = self.ContieneAlMenosUnDigito(clave)
        resultado = validacion1 and validacion2 and validacion3 and validacion4 and validacion5 and validacion6
        if resultado == False:
            mensaje = "Clave Invalida"
            if validacion1 == False:
                mensaje = mensaje + ", longitud de clave incorrecta"

            if validacion2 == False:
                mensaje = mensaje + ", posee caracteres especiales"

            if validacion3 == False:
                mensaje = mensaje + ", posee menos de tres letras"

            if validacion4 == False:
                mensaje = mensaje + ", no posee mayusculas"

            if validacion5 == False:
                mensaje = mensaje + ", no posee minusculas"

            if validacion6 == False:
                mensaje = mensaje + ", no contiene digitos"
                
            print(mensaje)

        return resultado
    
    # Funcion que verifica que la clave original y su confirmacion son iguales
    def VerificarClavesCoinciden(self,clave1, clave2):
        return clave1==clave2
    
    # Funcion que verifica que el correo tenga un formato correcto
    def ValidarCorreo(self,correo):
        patron = "[^@]+@[^@]+\.[^@]+"
        Correo_REGEX = re.compile(patron)
        result = bool(Correo_REGEX.match(correo))
        if result == False:
            print("Correo electrónico inválido")
        return result
    
    # Funcion que verifica que la longitud de la clave esté entre los límites establecidos
    def ValidarLongitudClave(self,clave):
        longitudMinimaClave = 8
        longitudMaximaClave = 16
        longitudCorreo = len(clave)
        return longitudCorreo >= longitudMinimaClave and longitudCorreo <= longitudMaximaClave

    # Funcion que verifica que no existan caracteres especiales en la clave
    def ValidarNoCaracteresEspeciales(self, clave):
        return bool(re.match("^[a-zA-Z0-9_]*$", clave))

    # Funcion que verifica que la clave tenga un minimo de tres letras
    def ContieneAlMenosTresLetras(self,clave):
        return bool(re.match("(.*[a-zA-Z]){3}", clave))

    # Funcion que verifica que la clave tenga al menos una letra minuscula
    def ContieneAlMenosUnaMinuscula(self,clave):
        return any(x.islower() for x in clave)

    # Funcion que verifica que la clave tenga al menos una letra mayuscula
    def ContieneAlMenosUnaMayuscula(self,clave):
        return any(x.isupper() for x in clave)

    # Funcion que verifica que la clave tenga al menos un digito numerico
    def ContieneAlMenosUnDigito(self,clave):
        return any(x.isdigit() for x in clave)

    def IngresarUsuario(self, correo, clave):
        clave_dict = clave[::-1]
        element = self.my_dict.get(correo)
        return element == clave_dict

    
    
    


