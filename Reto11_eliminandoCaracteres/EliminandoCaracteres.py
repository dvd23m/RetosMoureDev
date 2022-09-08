def diffCadenas(str1, str2):
	out1 = "".join(set(str1) - set(str2))
	out2 = "".join(set(str2) - set(str1))
	print(out1)
	print(out2)

str1= "Esto de los retos es muy divertido"
str2="seguro que mejoraremos nuestra lógica"
diffCadenas(str1, str2)

