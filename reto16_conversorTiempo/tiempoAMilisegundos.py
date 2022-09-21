def milisegundos(days, hours, mins, secs):
    d = days * 24 * 60**2 
    h = hours * 60**2
    m = mins * 60
    print(f"{days} dias, {hours} horas, {mins} minutos y {secs} segundos son {(d+h+m+secs)*1000} milisegundos")

def comprobarPositivos(n, mensaje):
    while n < 0:
        n = int(input(mensaje))
    return n

days = comprobarPositivos(int(input("Introduce los dias: ")), "Introduce los dias: ")
hours = comprobarPositivos(int(input("Introduce las horas: ")), "Introduce las horas: ")
mins = comprobarPositivos(int(input("Introduce los minutos: ")), "Introduce los minutos: ")
secs = comprobarPositivos(int(input("Introduce los segundos: ")), "Introduce los segundos: ")

milisegundos(days, hours, mins, secs)
