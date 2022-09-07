n = 100
# Crear lista del 2 a n
primos = list(range(2, n+1))

i = 0

while primos[i] ** 2 <= n:
    for num in primos:
        # Omitir los primos seleccionados
        if num <= primos[i]:
            continue
        elif num % primos[i] == 0:
            primos.remove(num)
    i += 1

print(f"Los primos del 1 al 100 en función de la criba de Eratóstenes son {primos}")    
