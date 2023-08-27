abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def calcularCelda(cadena):
    '''
        Calcula el número de la columna de Excel en función del nombre de la misma
        Ejemplos:
        Si el nombre es A la columna será 1 
        Si el nombre es AA columna = 27
        Si el nombre es BAA columna = 1379

        Si el programa recibe la palabra 'salir' se detendrá

        Params
        cadena: String con el nombre de la columna
        
        Return:
        No se retorna ningún valor. Se imprime directamente el resultado
    '''
    columna = 0
    for exp, l in enumerate(reversed(cadena)):
        columna += 26**exp * (abc.index(l) + 1)
    print(f'La celda correspondiente a {cadena} es {columna}')

while (cadena := input("Introduce una celda formato AAA: ")).isalpha() == False:
    print("Solo se pueden introducir letras")
if cadena != 'salir':
    calcularCelda(cadena.upper())




