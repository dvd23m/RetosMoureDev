def factorialRecursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorialRecursivo(n-1)

n = int(input("Introduce un numero para calcular su factorial: "))
while n < 0:
    n = int(input("El número debe ser positivo: "))
print(factorialRecursivo(n))
