from math import factorial

def combinacion(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))

num = int(input("Introduce un número: "))

for n in range(num):
    row = []    
    for r in range(n+1):
        row.append(combinacion(n, r))
    print(' '*(num-n) + " ".join(str(e) for e in row))
