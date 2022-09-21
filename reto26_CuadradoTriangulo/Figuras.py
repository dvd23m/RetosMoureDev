def imprimirFigura(fig, size):
    if fig == 1: # Cuadrado
        print(size*(size*' *'+"\n"))
    if fig == 2: # Triangulo
        for i in range(1, size+1):
            print(' *'+"\n")
    if fig == 3: # Piramide
        for i in range(size):
            print('+'*(size - i) + '*'*(2 * i + 1))
    if fig == 4: # Rombo
        for i in range(size):
            print(' '*(size - i) + '*'*(2 * i + 1))
        for i in range(1, size):
            print(' '*(i + 1) + '*'*(2 * size -2*i -1))


n = int(input("Introduce el tamaño de la figura (mayor que 0): "))
while n < 1:
    n = int(input("Introduce el tamaño de la figura (mayor que 0): "))

figura = int(input("Introduce la figura [1-Cuadrado, 2-Triangulo, 3-Piramide, 4-Rombo]: "))
while figura not in [1,2,3,4]:
    figura = int(input("Introduce la figura [1-Cuadrado, 2-Triangulo, 3-Piramide, 4-Rombo]: "))

imprimirFigura(figura, n)
