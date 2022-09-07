fibonacci = [0,1]

for i in range(1, 49):
    n = fibonacci[i] + fibonacci[i-1]
    fibonacci.append(n)

print(fibonacci)
