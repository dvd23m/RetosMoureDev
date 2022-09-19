# Import librerias
import pandas as pd
from tkinter import messagebox, ttk
import tkinter as tk
import math

# Cargar los datos
zelda = pd.read_html("https://en.m.wikipedia.org/wiki/List_of_The_Legend_of_Zelda_media")[0][["Title","Release"]]

# Separar texto por : y escoger primera fecha de lanzamiento
zelda["Release"] = zelda["Release"].apply(lambda x: x.split(":")[1])
# Eliminar letras tras el año de lanzamiento
zelda["Release"] = zelda["Release"].str.replace(r"[A-Z]{2,}", "", regex=True).str.strip()
# Convertir a fecha
zelda["Release"] = pd.to_datetime(zelda["Release"])
# Titulo como indice
zelda.set_index("Title", inplace=True)

# Crear interfaz
class AppZelda():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Juegos zelda')
        self.root.geometry('970x150')
        self.root.resizable(False, False)        
                  
        self.selectGame1 = tk.StringVar()
        self.selectGame2 = tk.StringVar()
        
        self.label1 = ttk.Label(self.root, text='Selecciona el primer juego').grid(pady=10, padx=25, row=1, column=0)
        self.label2 = ttk.Label(self.root, text='Selecciona el segundo juego').grid(pady=10, padx=25, row=1, column=1)

        self.comboJuego1 = ttk.Combobox(self.root, 
                                        width=60, 
                                        state="readonly", 
                                        values=list(zelda.index),
                                        textvariable=self.selectGame1).grid(pady=10, padx=25, row=3, column=0)
        
        self.comboJuego2 = ttk.Combobox(self.root, 
                                        width=60,
                                        state="readonly", 
                                        values=list(zelda.index),
                                        textvariable=self.selectGame2).grid(pady=10, padx= 25, row=3, column=1)

        self.btTiempoJuegos = tk.Button(self.root, 
                                        text="Calcular dias entre juegos",
                                        command = self.calcularDias).grid(pady=10, padx= 25, row=4, column=0)
        
        self.root.mainloop()

    def calcularDias(self):
       # Obtener seleccion de los combos
       self.tituloJuego1 = self.selectGame1.get()
       self.tituloJuego2 = self.selectGame2.get()
       # Calcular diferencia de dias
       self.diffDays = (abs(zelda.loc[self.tituloJuego1] - zelda.loc[self.tituloJuego2])["Release"].days) / 365
       # Separar parte decimal y entera
       self.days, self.years = math.modf(self.diffDays)
       # Resultado
       self.txt = f"La diferencia en días entre los juegos {self.tituloJuego1} y {self.tituloJuego2} es de {int(self.years)} años y {round(self.days * 365)} dias"
       messagebox.showinfo(message=self.txt, title="Diferencia de tiempo")
win1 = AppZelda()
