from random import randrange

# Generar 20 numeros aleatorios entre 1 y 99
nums = [randrange(1, 100, 1) for x in range(20)]

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

print(f"Lista de numeros inicial: {nums}")
print(f"Lista de numeros ordenada: {quickSort(nums)}")
