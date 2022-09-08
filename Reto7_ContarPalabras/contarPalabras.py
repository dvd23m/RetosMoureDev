import re
from collections import defaultdict
import json

totalByWords = defaultdict(int)

def ContadorPalabras(txt):
    '''
        Función que elimina caracteres que no sean numeros o letras, separa todas las palabras y las 
        pone en minusculas. Una vez tiene esto, recorre la lista de palabras y las introduce en un defaultDict
        incrementando en 1 el valor de cada key

        Params: 
            txt(string): El texto para realizar el conteo

        Return:
            totalByWords(dict): El diccionario con las palabras y el total de veces que aparecen
    '''

    txt = re.sub('[^A-Za-z0-9]', " ", txt)
    txt = txt.lower().split()
    for word in txt:
        totalByWords[word] += 1

    return totalByWords

texto = '''
 Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales
 * a Sauron contra otras bondadosas que no quieren que el mal reine
 * sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
 *   Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
 *   Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre
 * los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate.
 *   Dependiendo de la suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable
 *   de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco
 *     2 Pelosos empatan contra 1 Orco
 *     3 Pelosos ganan a 1 Orco
'''
# Se utiliza json.dumps para dar formato más legible a la visualización del dict
print(json.dumps(ContadorPalabras(texto), sort_keys=False, indent=4))
