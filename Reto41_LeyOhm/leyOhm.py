def calcularOhm(v, i, r):
    '''
        Funcion que calcula la ley de Ohm. Comprueba qué valores ha recibido y en función de estos ejecuta:
        V = R*I si recibe Corriente(I) y Resistencia(R)
        I = V/R si recibe Potencia(V) y Resistencia(R)
        R = V/I si recibe Potencia(V) y (Corriente)

        En caso de recibir I o R, se comprueba si, el contrario, es igual a 0. De ocurrir esto se finaliza el programa
        ya que el denominador de la fracción sería un 0, y no se puede dividir por cero.

        parametros: 2 son float, 1 sera cadena vacia ("")
    '''
    if v=="":
        print(f"\nEl valor de el potencial electrico es {round(r*i, 2)}")
    if r=="":
        # Se comprueba si division por cero
        try: 
            print(f"\nEl valor de la resistencia es {round(v/i, 2)}")
        except ZeroDivisionError:
            print("\nEl valor de la corriente no puede ser 0")
            return
    if i=="":
        try: 
            print(f"\nEl valor de la corriente es {round(v/r, 2)}")
        except ZeroDivisionError:
            print("\nEl valor de la resistencia no puede ser 0")
            return
    
def comprobarValor(valores):
    '''
        Funcion que comprueba si únicamente existe 1 valor como cadena vacia y, convierte los valores de la lista en float.
        También realiza la llamada a la función de cálculo de la ley de Ohm enviando los valores de la lista como argumento.

        parametros: lista con números y una cadena vacia
    '''
    # Únicamente debe faltar 1 dato
    if valores.count("")>1 or valores.count("")==0:
        print("Invalid values")
        return
    # Transformacion de tipos    
    for idx, val in enumerate(valores):
        if val=="":
            pass
        else:
            try:
                valores[idx] = float(val)
            except:
                print("Invalid values")
    calcularOhm(valores[0], valores[1], valores[2])
    
valores=[]
print("""
************************************************************************************************************
* La formula de Ohm es la siguiente V = R * I donde:                                                       *
*   ++ V es el potencial eléctrico en voltios                                                              *
*   ++ I es la corriente en amperios                                                                       *
*   ++ R es la resistencia.                                                                                *
* Para realizar los cálculos en esta app es necesario introducir únicamente 2 de los datos solicitados:    *
************************************************************************************************************
""")
valores.append(input("Introduce un valor numerico para el potencial. Si no lo conoces pulsa enter: "))
valores.append(input("Introduce un valor numerico para la corriente. Si no lo conoces pulsa enter: "))
valores.append(input("Introduce un valor numerico para la resistencia. Si no lo conoces pulsa enter: "))
comprobarValor(valores)
