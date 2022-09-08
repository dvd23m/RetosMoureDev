**DECIMAL A BINARIO**  
Fecha publicación enunciado: 18/02/22  
Dificultad: FÁCIL  
Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

## Cómo pasar de decimal a binario?  
> Para poder obtener el número binario, es necesario ir dividiendo el número en base decimal entre dos e ir anotando el resto (0 si el resultado es par  o 1 si es impar). Ua vez obtenidos todos los restos, deberán colocarse de derecha a izquierda si se han anotado en forma de lista o de abajo hacia arriba en caso de haber realizado la división de forma manual tal y como lo hacíamos en el colegio. Con unos ejemplos se verá mucho más claro. 

Ejemplo 1: Encontrar el binario del número 79

$\frac{79}{2} = 39,5$(impar) -> 1  
$\frac{39}{2} = 19$(impar) -> 1  
$\frac{19}{2} = 9,5$(impar) -> 1  
$\frac{9}{2} = 4,5$(impar) -> 1  
$\frac{4}{2} = 2$(par) -> 0  
$\frac{2}{2} = 1$(par) -> 0  
$\frac{1}{2} = 0,5$(impar) -> 1  

Si se unen los resultados se obtiene 1111001 pero para obtener el binario deben cogerse de derecha a izquierda (o de abajo a arriba si se mira paso a paso). Por lo tanto 79 en binario es 1001111

  
