import re
def enMayuscula(txt):
    mayuscula = ""
    txt = re.sub("\s{2,}", " ", txt)
    for i in txt.split(" "):
        mayuscula += i[0].upper() + i[1:] + " "
    return(mayuscula)
    
texto = input("Introduce un texto: ")
print(enMayuscula(texto))
