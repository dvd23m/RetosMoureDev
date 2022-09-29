**Reto #39**  
TOP ALGORITMOS: QUICK SORT  
Fecha publicación enunciado: 27/09/22  
Dificultad: MEDIA  

Enunciado: Implementa uno de los algoritmos de ordenación más famosos: el "Quick Sort",  creado por C.A.R. Hoare.  
Entender el funcionamiento de los algoritmos más utilizados de la historia nos ayuda a  mejorar nuestro conocimiento sobre ingeniería de software.  

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif" alt="animated" />
</p>

## ¿Cómo funciona quick sort?
En el siguiente ejemplo se marcan el pivote y los índices i y j con las letras p, i y j respectivamente.  

Comenzamos con la lista completa. El elemento pivote será el 4:  
```
 5 - 3 - 7 - 6 - 2 - 1 - 4  
                         p
``` 
Comparamos con el 5 por la izquierda y el 1 por la derecha.    
 ```
 5 - 3 - 7 - 6 - 2 - 1 - 4   
 i                   j   p  
 ```
5 es mayor que 4 y 1 es menor. Intercambiamos:  
```
 1 - 3 - 7 - 6 - 2 - 5 - 4  
 i                   j   p   
 ```
Avanzamos por la izquierda y la derecha:  
 ```
 1 - 3 - 7 - 6 - 2 - 5 - 4  
     i           j       p   
```
3 es menor que 4: avanzamos por la izquierda. 2 es menor que 4: nos mantenemos ahí.  
```
1 - 3 - 7 - 6 - 2 - 5 - 4  
         i       j       p   
```
7 es mayor que 4 y 2 es menor: intercambiamos.  
```
1 - 3 - 2 - 6 - 7 - 5 - 4  
         i       j       p   
```
Avanzamos por ambos lados:
```
1 - 3 - 2 - 6 - 7 - 5 - 4
            iyj          p 
```
En este momento termina el ciclo principal, porque los índices se cruzaron. Ahora intercambiamos lista[i] con lista[p] (pasos 16-18):
```
1 - 3 - 2 - 4 - 7 - 5 - 6
             p 
```
Aplicamos recursivamente a la sublista de la izquierda (índices 0 - 2). Tenemos lo siguiente:
```
1 - 3 - 2 
```
1 es menor que 2: avanzamos por la izquierda. 3 es mayor: avanzamos por la derecha. Como se intercambiaron los índices termina el ciclo. Se intercambia lista[i] con lista[p]:
```
1 - 2 - 3 
```
El mismo procedimiento se aplicará a la otra sublista. Al finalizar y unir todas las sublistas queda la lista inicial ordenada en forma ascendente.
```
1 - 2 - 3 - 4 - 5 - 6 - 7
```

## Implementacion  

Este ejercicio se ha realizado mediante la división recursiva de una lista de números en 2 listas diferentes  
- left: Aquellos números menores al pivote  
- right: Aquellos números mayores al pivote
- Donde el pivote será el primer elemento de la lista  

```
    left = []
    right = []
    pivot = nums[0]
    
    for i in range(1, len(nums)):
        # Si valor de nums es < que pivot se va a la izquierda sino a la derecha
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
```
Para poder aplicar esta separación *left-right* entre las distintas divisiones, se ejecuta la función de forma recursiva para cada una de las divisiones.  
Por lo tanto, el retorno de la función es el siguiente:

```
return quickSort(left) + [pivot] + quickSort(right)
```
La forma en que la recursión finalice, es incluyendo al inicio de la función un condicional que compruebe si la lista esta vacía. En caso de que   
esto sea cierto, retornar dicha lista vacía. Finalmente, la función quedará de la siguiente manera:

```
def quickSort(nums):
    # Si la lista esta vacía se retorna
    if len(nums) == 0:
        return nums

    left = []
    right = []
    pivot = nums[0]
    
    for i in range(1, len(nums)):
        # Si valor de nums es < que pivot se va a la izquierda sino a la derecha
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
    # Se realiza la recursion
    return quickSort(left) + [pivot] + quickSort(right)
```





