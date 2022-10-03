# importando tkinter 
from tkinter.ttk import *
from tkinter import*

# importando pillow
from PIL import Image, ImageTk
from matplotlib import image
from matplotlib.pyplot import text

from pygame import mixer
import time
from datetime import datetime

from time import sleep
from threading import Thread

# cores

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#d6872d"  # ouro / gold
co3 = "#fc766d"  # vermelha / red
co4 = "#403d3d"   # preta / black
co5 = "#4a88e8"  # Azul / Bblue


# criando janela

janela = Tk()
janela.title("")
janela.geometry('350x150')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# dividindo a janela em 2 frames
frame_logo = Frame(janela, width=400, height=10, bg=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0)

frame_corpo = Frame(janela, width=400, height=290, bg=co1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0)

# configurando o frame logo
l_linha = Label(frame_logo, width=400, height=1, bg=co2, anchor=NW, font=('Ivy 1'))
l_linha.place(x=0, y=0)


# configurando o frame corpo

imagem = Image.open('icon1.png')
imagem = imagem.resize((100,100))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frame_corpo, height=100,image=imagem, compound=LEFT, padx=10, anchor=NW, font=('Ivy 16 bold'), bg=co1, fg=co3)
l_imagem.place(x=10, y=10)

l_nome = Label(frame_corpo,text='Alarme', height=1, anchor=NE, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=105, y=10)


# criando combo boxes

l_hora = Label(frame_corpo,text='Horas', height=1, anchor=NW, font=('arial 7'), bg=co1, fg=co4)
l_hora.place(x=127, y=40)
c_hora = Combobox(frame_corpo, width=2,font=('Ivy 15'))
c_hora['value'] = ("00", "01", "02", "03", "04", "05","06", "07", "08", "09", "10", "11", "12")
c_hora.current(0)
c_hora.place(x=130, y=58)

l_minuto = Label(frame_corpo,text='Minutos', height=1, anchor=NW, font=('arial 7'), bg=co1, fg=co4)
l_minuto.place(x=177, y=40)
c_minuto = Combobox(frame_corpo, width=2,font=('Ivy 15'))
c_minuto['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28",
                   "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_minuto.current(0)
c_minuto.place(x=180, y=58)

l_segundos = Label(frame_corpo,text='Segundos', height=1, anchor=NW, font=('arial 7'), bg=co1, fg=co4)
l_segundos.place(x=227, y=40)
c_segundos = Combobox(frame_corpo, width=2,font=('Ivy 15'))
c_segundos['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28",
                   "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_segundos.current(0)
c_segundos.place(x=230, y=58)

l_periodo = Label(frame_corpo,text='Periodo', height=1, anchor=NW, font=('arial 7'), bg=co1, fg=co4)
l_periodo.place(x=277, y=40)
c_periodo = Combobox(frame_corpo, width=3,font=('Ivy 15'))
c_periodo['value'] = ("AM", "PM")
c_periodo.current(0)
c_periodo.place(x=280, y=58)


def ativar_alarme():
    if selecionado.get() ==1:
        print('Ativar: ', selecionado.get())
    else:
        # criar thread
        t1 = Thread(target=alarme)   
        # iniciar o thread
        t1.start()
        

def desativar_alarme():
    print('Alarme desativado: ', selecionado.get())
    mixer.music.stop()
    

selecionado = IntVar()

radio = Radiobutton(frame_corpo,command=ativar_alarme, text='Ativar', value=1, variable=selecionado, font=('Arial 8'),bg=co1, fg=co4)
radio.place(x=125, y=95)



def tocar_alarme():
    mixer.music.load('2.mp3')
    mixer.music.play()
    selecionado.set(0)
    
    radio = Radiobutton(frame_corpo,command=desativar_alarme, text='Desativar', value=1, variable=selecionado, font=('Arial 8'),bg=co1, fg=co4)
    radio.place(x=187, y=95)

    
def alarme():
    while True:
        control = selecionado.get()
        h_alarme = c_hora.get()
        m_alarme = c_minuto.get()
        s_alarme = c_segundos.get()
        p_alarme = c_periodo.get().upper()
        
        # obtendo a hora atual
        hora_atual = datetime.now()

        hora = hora_atual.strftime("%I")
        minuto = hora_atual.strftime("%M")
        segundo = hora_atual.strftime("%S")
        periodo = hora_atual.strftime("%p")
        
        if control==1:
            if p_alarme == periodo:
                if h_alarme == hora:
                    if m_alarme == minuto:
                        if s_alarme == segundo:
                            print("Hora de fazer uma pausa")
                            tocar_alarme()
                            ativar_alarme()
                            
                            
        sleep(1)
        
        

t1 = Thread(target=alarme)   

# iniciar o thread
t1.start()
mixer.init()



janela.mainloop()