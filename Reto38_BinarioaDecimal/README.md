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

> En primer lugar, se solicitará al usuario que introduzca un número en binario, por lo únicamente se podrán introducir ceros y unos. 
> Si los valores introducidos son correctos, se inicia una función recursiva que realizará los cálculos, tal y como se ha mostrado en el ejemplo anterior,
> para retornar el valor en forma decimal.
