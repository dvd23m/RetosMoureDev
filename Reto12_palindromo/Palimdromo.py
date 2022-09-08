import re
from unidecode import unidecode

# Limpiar caracteres especiales, acentiqcion, espacios
regexp = re.compile(r'[^A-Za-z0-1]')
cadena= "Ana lleva al oso la avellana."
cad = unidecode(cadena).lower()
cad = re.sub(regexp, "", cad)

if cad == cad[::-1]:
	print(f"{cadena} Es un palindromo")
else:
	print(f"{cadena} No es un palindromo")
