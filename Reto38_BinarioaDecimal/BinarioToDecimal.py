import re

def calcularBinario(exp, n):
    '''
        Función recursiva. Recibe un número (1 o 0) y su índice en la cadena introducida
        por el usuario. Con estos 2 valores se calculará la operación correspondiente a:
        número (n) * 2 elevado al indice (exp)

        Params: 111001
            n (int) = valdrá 0 o 1
            exp (int) = tiene el valor del índice que ocupa n en la cadena introducida por el usuario
        
        Return:
            (int) = valor correspondiente a n*2**exp
    '''
    print(f"({n}*2^{exp})", end=" + ")
    return n*2**exp

# Se comprueba que el input del usuario sólo contenga unos y ceros
patron = re.compile("[^01]+")
nBinario = input("Introduce un número binario (0's y 1's): ")
while patron.search(nBinario):
    nBinario = input("Solo se pueden introducir unos y ceros: ")

# Se voltea el input
nBinario = nBinario[::-1]
decimal = 0
# Para cada elemento del input se llama a la función y se calcula el valor
print("\nFórmula para el cálculo\n------------------------")
for i in range(0, len(nBinario)):
    decimal += calcularBinario(i, int(nBinario[i]))

print(f"\n\nEl número {nBinario[::-1]} es {decimal} en decimal")

