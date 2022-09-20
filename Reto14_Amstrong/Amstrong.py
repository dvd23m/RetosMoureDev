def EsAmstrong(n):
    long = len(str(n))
    suma = 0
    for cifra in str(n):
        suma += int(cifra)**long  
    if suma == n:
        return "sí"
    return "no"

# Comprobacion input sea positivo
numero = int(input("Introduce un numero: "))
while numero <= 0:
    numero = int(input("Introduce un numero positivo mayor que 0: "))

print(f"El numero {numero} {EsAmstrong(numero)} es un número amstrong")
