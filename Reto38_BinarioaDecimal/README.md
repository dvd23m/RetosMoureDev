**Reto #38**
BINARIO A DECIMAL  
Fecha publicación enunciado: 19/09/22  
Dificultad: MEDIA  

Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar  
funciones propias del lenguaje que lo hagan directamente.

## ¿ Qué proceso se sigue para pasar de binario a decimal?

Para obtener el decimal a partir de un binario se sigue la siguiente fórmula:

$decimal= d_0 · 2^0 + d_1 · 2^1 + d_3 · 2^3 + + d_n · 2^n$ 

## Ejemplo 

Se pretende encontrar el decimal correspondiente al número 111001:  
|binario|1|1|1|0|0|1|
|----|--|--|--|--|--|--|
|potencia de 2|2⁵|2⁴|2³|2²|2¹|2⁰|

por lo tanto:
111001 = 1 x 2⁵ + 1 x 2⁴ + 1 x 2³ + 0 x 2² + 0 x 2¹ + 1 x 2⁰ = 57 

## Funcionamiento del programa

> En primer lugar, se solicitará al usuario que introduzca un número en binario, por lo únicamente se podrán introducir ceros y unos. Esta comprobación
se realizará mediante la expresión regular "[^01]+"  
Si el input es correcto éste se volteará de forma que se obtenga más fácilmente el índice (exponente) y el valor correspondientes. 
En este punto se ejecutará una función recursiva que realizará los cálculos, tal y como se ha mostrado en el ejemplo anterior.

Función:  
```
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
```
Loop:  
```
for i in range(0, len(nBinario)):
    decimal += calcularBinario(i, int(nBinario[i]))
```

