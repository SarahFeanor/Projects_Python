''' 
Autor: SarahFR
Data: 09/08/2022
Versão:0.1

'''

# Biblioteca tkinter/ datetime/ pyglet
from tkinter import*
import tkinter 

from datetime import datetime 

import pyglet   
pyglet.font.add_file('digital-7.ttf')

# Colors
color1= '#070808' #preto
color2= '#ff00a2' #rosa
color3= '#02de3d' #verde
color4= '#fcfcfc' #branca
color5= '#bdbdbd' #cinza
color6= '#27069c' #azul
color7= '#e0e004' #amarela

# Fundo do aplicativo/ cor da letra
fundo = color1
letra = color2
letra2 = color4

# Janelas
janela= Tk()
janela.title('')
janela.geometry('440x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=color1)

# Função 
def relogio():
    tempo =  datetime.now()
    
    # Hora, data, dia da semana, ano e mês.
    hora=tempo.strftime('%H:%M:%S')
    dia_semana=tempo.strftime('%A')
    dia= tempo.day
    mes= tempo.strftime("%B")
    ano= tempo.strftime('%Y')
    
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana +' - '+ str(dia)+'/'+ str(mes)+ "/"+ str(ano))

# Hora
l1=Label(janela, text='', font=('digital-7 100'), bg=fundo, fg=letra)
l1.grid(row=0, column=0, sticky=NW,padx=5)

# Dia da semana
l2=Label(janela, text='', font=('digital-7 17'), bg=fundo, fg=letra2)
l2.grid(row=1, column=0, sticky=NW,padx=5)


relogio()
janela.mainloop()

