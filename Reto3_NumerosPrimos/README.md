 **¿ES UN NÚMERO PRIMO?**  
 Fecha publicación enunciado: 17/01/22  
 Dificultad: MEDIA  
 
Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.  
Hecho esto, imprime los números primos entre 1 y 100.  

## Explicación de mi solución

Este ejercicio ha sido resuelto mediante el metodo de la criba de Eratostenes. la criba, consta de los siguientes pasos:  

1- Listar los números naturales comprendidos entre 2 hasta *n*.
2- Se toma el primer número no rayado ni marcado, como número primo.  
3- Se tachan todos los múltiplos del número que se acaba de indicar como primo.  
4- Si el cuadrado del primer número que no ha sido rayado ni marcado es inferior a *n*, entonces se repite el segundo paso. Si no, el algoritmo termina, y todos los enteros no tachados son declarados primos.  
Como $3^2 = 9 < 100$, se vuelve al segundo paso:  

