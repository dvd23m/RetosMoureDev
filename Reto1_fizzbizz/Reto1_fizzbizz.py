for i in range(1, 101):
    if (i % 3 == 0) & (i % 5 == 0):
        print("fizzbizz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("bizz")
    else:
        print(i)
