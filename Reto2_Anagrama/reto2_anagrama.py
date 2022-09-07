def EsAnagrama(word1, word2):
    if sorted(word1.lower()) == sorted(word2.lower()):
        return "sí"
    return "no"

word1 = "Japones"
word2 = "Esponja"

res_anagrama = EsAnagrama(word1, word2)

print(f'Las palabras {word1} y {word2} {res_anagrama} son anagramas')
