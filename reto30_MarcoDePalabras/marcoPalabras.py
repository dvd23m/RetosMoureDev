def nuevaLinea(palabra):
    difLongPalabras = len(palabraMasLarga) - len(palabra)
    print(f"* {palabra}{' '*difLongPalabras} *")

texto = input("Introduce un texto: ").split(" ")
palabraMasLarga = max(texto, key=len)

print('*'*(len(palabraMasLarga)+4))
for palabra in texto:
    nuevaLinea(palabra)
print('*'*(len(palabraMasLarga)+4))
