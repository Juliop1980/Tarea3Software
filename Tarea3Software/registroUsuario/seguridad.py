import re

def VerificarRegistro(correo, clave1, clave2):
    return VerificarClavesCoinciden(clave1, clave2) and ValidarCorreo(correo) and ValidarClave(clave1)

def ValidarClave(clave):
    return ValidarLongitudClave(clave) and ValidarNoCaracteresEspeciales(clave) and ContieneAlMenosTresLetras(clave) and ContieneAlMenosUnaMayuscula(clave)  and ContieneAlMenosUnaMinuscula(clave) and ContieneAlMenosUnDigito(clave)
      
def VerificarClavesCoinciden(clave1, clave2):
    return clave1==clave2

def ValidarCorreo(correo):
    patron = "[^@]+@[^@]+\.[^@]+"
    Correo_REGEX = re.compile(patron)
    result = bool(Correo_REGEX.match(correo))
    return result
    
def ValidarLongitudClave(clave):
    longitudMinimaClave = 8
    longitudMaximaClave = 16
    longitudCorreo = len(clave)
    return longitudCorreo >= longitudMinimaClave and longitudCorreo <= longitudMaximaClave

def ValidarNoCaracteresEspeciales(clave):
    return bool(re.match("^[a-zA-Z0-9_]*$", clave))

def ContieneAlMenosTresLetras(clave):
    return bool(re.match("(.*[a-z]){3}", clave))

def ContieneAlMenosUnaMinuscula(clave):
    return any(x.islower() for x in clave)

def ContieneAlMenosUnaMayuscula(clave):
    return any(x.isupper() for x in clave)

def ContieneAlMenosUnDigito(clave):
    return any(x.isdigit() for x in clave)
    


