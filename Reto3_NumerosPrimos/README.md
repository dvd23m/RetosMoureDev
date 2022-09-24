 **¿ES UN NÚMERO PRIMO?**  
 Fecha publicación enunciado: 17/01/22  
 Dificultad: MEDIA  
 
Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.  
Hecho esto, imprime los números primos entre 1 y 100.  

## Explicación de mi solución

Este ejercicio ha sido resuelto mediante el metodo de la [Criba de Eratostenes](https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes). la criba, consta de los siguientes pasos: 

Para una n = 20

1- Listar los números naturales comprendidos entre 2 hasta *n*.  
![](https://github.com/dvd23m/RetosMoureDev/blob/main/Reto3_NumerosPrimos/Captura%20desde%202022-09-07%2018-22-31.png)  

2- Se toma el primer número no rayado ni marcado, como número primo.  
![](https://github.com/dvd23m/RetosMoureDev/blob/main/Reto3_NumerosPrimos/Captura%20desde%202022-09-07%2018-23-04.png)  

3- Se tachan todos los múltiplos del número que se acaba de indicar como primo.  
![](https://github.com/dvd23m/RetosMoureDev/blob/main/Reto3_NumerosPrimos/Captura%20desde%202022-09-07%2018-23-09.png)  

4- Si el cuadrado del primer número que no ha sido rayado ni marcado es inferior a *n*, entonces se repite el segundo paso. Si no, el algoritmo termina, y todos los enteros no tachados son declarados primos.  
Como $3^2 = 9 < 20$, se vuelve al segundo paso:  
![](https://github.com/dvd23m/RetosMoureDev/blob/main/Reto3_NumerosPrimos/Captura%20desde%202022-09-07%2018-23-14.png)  

En el cuarto paso, el primer número que no ha sido tachado ni marcado es 5. Como su cuadrado es mayor que *n*, el algoritmo termina y se consideran primos todos los números que no han sido tachados.

<p align="center">
<img src="https://user-images.githubusercontent.com/68005809/188928576-acc2eaed-a42a-40f2-a967-0fe5eed8e1f5.gif" alt="animated" />
</p>

Como resultado se obtienen los números primos comprendidos entre 2 y 20, y estos son: 2, 3, 5, 7, 11, 13, 17, 19.
