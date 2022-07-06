from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from datetime import datetime
from pyglet import *
import pyglet


font.add_file('DigitalClock/fonts/digital-7.ttf')


# Color
col1 = "#3d3d3d" #Black
col2 = "#fafcff" #White
col3 = "#21c25c" #green
col4 = "#eb463b" #red
col5 = "#dedcdc" #gray
col6 = "#3080f0" #blue

fundo = col1
color = col2

janela=Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=col1)

#Função
def relogio():
    # Data
    tempo =  datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b") #B exibe nome completo
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio) #Deposi de 200 ms ira executar a função relógio de novo
    l2.config(text=dia_semana + " " + str(dia) + "/" + str(mes) + "/" + str(ano))


l1 = Label(janela, text="", font=("digital-7 60"), bg=fundo, fg=color)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font=("digital-7 15"), bg=fundo, fg=color)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()




