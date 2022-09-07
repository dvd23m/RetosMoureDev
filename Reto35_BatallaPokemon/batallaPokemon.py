def buscarEfectividad(tipo1, tipo2):
    '''
        Funcion que recorre un array en funcion del tipo de pokemon atacante y defensor,
        que son los que marcan los indices i, j.
        
        Siendo el orden de los tipos de pokemon: Agua, Fuego, Planta, Electrico
                        
        Params:
            tipo1 (int): tipo de pokemon atacante 
            tipo2 (int): tipo de pokemon defensor
        
        Retorna:
            (int): El valor de la efectividad
    '''
    # valores pokeTipos: Agua, Fuego, Planta, Electrico 
    pokeTipos = [[0.5, 2, 0.5, 1],
            [0.5, 0.5, 2, 1],
            [2, 0.5, 0.5, 1],
            [0.5, 1, 0.5, 0.5]]
    return pokeTipos[tipo1][tipo2]


def batalla(ataque, defensa, efectividad):
    '''
        Calcula el daño ocasionado en la batalla
        
        Params:
            ataque (int): indica el valor del ataque introducido por el usuario
            defensa (int): indica el valor de la defensa introducido por el usuario
            efectividad (int): multiplicador del ataque
        
        Retorna:
            (int): El valor del daño ocasionado en funcion de la formula
            50 * (ataque / defensa) * efectividad
    '''
    return  50 * (ataque / defensa) * efectividad

def escoger_tipo():
    '''
    Comprueba que el valor del tipo de pokemon se encuentre entre 0 y 3
    
    siendo [0-Agua, 1-Fuego, 2-Planta, 3-Electrico ]
    
    Params: None
    
    Retorna:
        (int) : Valor del tipo de pokemon entre 0 y 3
    '''
    while True:
        try:
            valor = int(input("Introduce un numero entre el 0 y el 3 [0-Agua, 1-Fuego, 2-Planta, 3-Electrico ]: "))
            if valor == 0 or valor < 4:
                return valor                
        except ValueError:
            print("Debes introducir un numero entre el 0 y el 3 [0-Agua, 1-Fuego, 2-Planta, 3-Electrico ]:")   
            
def ataqueDefensa():
    '''
    Comprueba que el valor de ataque o defensa se encuentre entre 1 y 100
    
    Params: None
    
    Retorna:
        (int) : Valor del tipo de pokemon entre 1 y 100
    '''
    while True:
        try:
            valor = int(input("Introduce un numero entre el 1 y el 100: "))
            if (valor >= 1) and (valor <= 100):
                return valor                
        except ValueError:
            print("Debes introducir un numero entre el 1 y el 100:")  


# Tipos de pokemon
tipos = ["Agua", "Fuego", "Planta", "Electrico"]

# Iniciar la solicitud de datos al usuario
tipo1 = escoger_tipo()
ataque = ataqueDefensa()
tipo2 = escoger_tipo()
defensa = ataqueDefensa()
efectividad = buscarEfectividad(tipo1, tipo2)
damage = batalla(ataque, defensa, efectividad)

print(f'''El daño ocasionado por un pokemon de tipo {tipos[tipo1]} con un ataque de {ataque} a otro de tipo {tipos[tipo2]}
con defensa de {defensa}, es de {round(damage)}''')
