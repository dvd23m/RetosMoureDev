def calcularArea(poligono):
    poli, b, h= poligono[0], poligono[1], poligono[2]
    if poli == "t":
        return (b*h)/2
    elif poli == "r":
        return b*h 
    elif poli == "c":
        return b**2

# Inicializacion de variables
base = 0
altura = 0
poli = ''

# Comprobar si introduccion de los datos del usuario
while poli != 't' and poli != 'r' and poli != 'c':
    poli = input("introduce poligono: [triangulo:t, rectangulo:r, cuadrado:c]: ")

while base <= 0:
    try:
        base = int(input("Introduce la base (>0): "))
    except ValueError:
        print("Debes introducir un numero mayor que 0")

# Si el poligono es cuadrado 'c' no se pide la altura
if poli != "c":
    while altura <= 0:
        try:
            altura = int(input("Introduce la altura (>0): "))
        except ValueError:
            print("Debes introducir un numero mayor que 0")

poligono = [poli, base, altura]
area = calcularArea(poligono)
print(f"El area del poligono seleccionado es: {area}")

