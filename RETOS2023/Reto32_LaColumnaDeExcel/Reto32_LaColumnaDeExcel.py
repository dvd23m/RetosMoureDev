abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cadena = 'XFC'
celda = 0
for exp, l in enumerate(reversed(cadena)):
    celda += 26**exp * (abc.index(l) + 1)
print(celda)
    





