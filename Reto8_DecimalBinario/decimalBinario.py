binario = []
n = 0
def decimalToBinary(n):
    while n > 0:
        resto = n % 2
        n //= 2
        binario.append(str(resto))
    return binario

while n <= 0:
    try:
        n = int(input("Introduce un numero positivo para convertir a binario: "))
        bin = decimalToBinary(n)
    except ValueError:
        print("Recuerda que debes introducir un valor numerico")

print(f"El numero {n} es {''.join(bin)} en binario")
