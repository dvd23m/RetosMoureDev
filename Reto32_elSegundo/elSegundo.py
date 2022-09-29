from random import randrange

# Generar lista de aleatorios
nums=[randrange(0, 100) for x in range(20)]

print(f"La lista inicial es: {nums}")
print(f"El segundo mas grande es:  {sorted(nums, reverse=True)[1]}")
