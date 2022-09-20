def factorialRecursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorialRecursivo(n-1)

print(factorialRecursivo(5))
