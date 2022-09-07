 **¿ES UN NÚMERO PRIMO?**  
 Fecha publicación enunciado: 17/01/22  
 Dificultad: MEDIA  
 
Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.  
Hecho esto, imprime los números primos entre 1 y 100.  

## Explicación de mi solución

Este ejercicio ha sido resuelto mediante el metodo de la [Criba de Eratostenes](https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes). la criba, consta de los siguientes pasos: 

Para una n = 20

1- Listar los números naturales comprendidos entre 2 hasta *n*.  

2- Se toma el primer número no rayado ni marcado, como número primo.  
3- Se tachan todos los múltiplos del número que se acaba de indicar como primo.  
4- Si el cuadrado del primer número que no ha sido rayado ni marcado es inferior a *n*, entonces se repite el segundo paso. Si no, el algoritmo termina, y todos los enteros no tachados son declarados primos.  
Como $3^2 = 9 < 100$, se vuelve al segundo paso:  

En el cuarto paso, el primer número que no ha sido tachado ni marcado es 5. Como su cuadrado es mayor que *n*, el algoritmo termina y se consideran primos todos los números que no han sido tachados.

<center>
![Sieve_of_Eratosthenes_animation](https://user-images.githubusercontent.com/68005809/188928576-acc2eaed-a42a-40f2-a967-0fe5eed8e1f5.gif)
</center>
Como resultado se obtienen los números primos comprendidos entre 2 y 20, y estos son: 2, 3, 5, 7, 11, 13, 17, 19.




