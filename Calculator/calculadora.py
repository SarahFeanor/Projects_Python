
''' 

    Autor: SarahFR 
    Data: 21/07/2022
    Versão: 1.0

'''
# Projeto de aprendizado - Criando Calculadora em Python

# Etapa 1 - Importando as bibliotecas necessarias para dentro do script, usando o tkinter

from tkinter import *
from tkinter import ttk

# Cores

color1 = '#010f0f' # black
color2 = '#fafafa' # branco
color3 = '#235959' # verde
color4 = '#c8dbdb' # cinza
color5 = '#54ded2' # azul piscina
color6 = '#38a69b' # azul piscina escuro
color7 = '#0a3b8a' # azul
color8 = '#072c66' # azul escuro


# Etapa 2 - Criando e configurando a janela 

janela = Tk()
janela.title('Calculadora')
janela.geometry('320x340')
janela.config(bg=color1)

# Etapa 3 - Dividindo a janela em dois frames 

frame_tela = Frame(janela, width=320, height=80, bg=color6 )
frame_tela.grid(row=0, column=0)

frame_quadro = Frame(janela, width=320, height=358)
frame_quadro.grid(row=1, column=0)

# Etapa: Criando a lógica para está calculadora

# Variavel
todos_valores = ''

# Criando label
valor_texto = StringVar()

# Criando função

def entrada_valores(event):

    global todos_valores 
    
    todos_valores = todos_valores + str(event)
    
    
    # Imprimimdo o valor para tela
    valor_texto.set(todos_valores)

 # Função para calcular   

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

# Função limpar tela

def limpar_tela ():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

# Label 
app_label = Label(frame_tela, textvariable = valor_texto, width=16, height=2, padx=2, relief=FLAT, anchor= "e", justify=RIGHT, font=('Ivy 25'), bg=color6, fg=color2)
app_label.place(x=0,y=0)

# Etapa 4 e 5 - Criando botoes e definido texto, dimenções, cores, fonte e estilos dos botões 


# 1ª fileira - BOTÕES (C % /)

bt1 = Button(frame_quadro, command= limpar_tela, text='C' , width=15, heigh=2, bg=color4, fg=color8, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt1.place(x=0,y=0)

bt2 = Button(frame_quadro, command= lambda: entrada_valores('%'), text='%', width=7, heigh=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt2.place(x=160,y=0)

bt3 = Button(frame_quadro, command= lambda: entrada_valores('/'), text='/' , width=7, heigh=2, bg=color7, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt3.place(x=240,y=0)


# 2ª fileira - BOTÕES (7, 8 , 9, *)

bt4 = Button(frame_quadro, command= lambda: entrada_valores('7'), text='7' ,width=7, heigh=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt4.place(x=0,y=52)

bt5 = Button(frame_quadro, command= lambda: entrada_valores('8'), text='8' ,width=7, heigh=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt5.place(x=80,y=52)

bt6 = Button(frame_quadro, command= lambda: entrada_valores('9'), text='9' , width=7, heigh=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt6.place(x=160,y=52)

bt7 = Button(frame_quadro, command= lambda: entrada_valores('*'), text='*' ,width=7, heigh=2, bg=color7, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt7.place(x=240,y=52)


# 3ª fileira - BOTÕES (4,5,6, -)

bt4 = Button(frame_quadro, command= lambda: entrada_valores('4'), text='4' ,width=7, heigh=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt4.place(x=0,y=104)

bt5 = Button(frame_quadro, command= lambda: entrada_valores('5'), text='5' ,width=7, heigh=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt5.place(x=80,y=104)

bt6 = Button(frame_quadro, command= lambda: entrada_valores('6'), text='6' , width=7, heigh=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt6.place(x=160,y=104)

bt7 = Button(frame_quadro, command= lambda: entrada_valores('-'), text='-' ,width=7, heigh=2, bg=color7, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt7.place(x=240,y=104)

# 4ª fileira - BOTÕES ( 1, 2, 3 +)

bt4 = Button(frame_quadro, command= lambda: entrada_valores('1'), text='1' , width=7, heigh=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt4.place(x=0,y=156)

bt5 = Button(frame_quadro, command= lambda: entrada_valores('2'), text='2' , width=7, heigh=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt5.place(x=80,y=156)

bt6 = Button(frame_quadro, command= lambda: entrada_valores('3'), text='3' , width=7, heigh=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt6.place(x=160,y=156)

bt7 = Button(frame_quadro, command= lambda: entrada_valores('+'), text='+' ,width=7, heigh=2, bg=color7, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt7.place(x=240,y=156)

# 5ª fileira - BOTÕES (0 . =)

bt1 = Button(frame_quadro, command= lambda: entrada_valores('0'), text='0' , width=15, heigh=2, bg=color4, fg= color8, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt1.place(x=0,y=208)

bt2 = Button(frame_quadro, command= lambda: entrada_valores('.'), text='.' ,width=7, heigh=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt2.place(x=160,y=208)

bt3 = Button(frame_quadro, command = calcular, text='=' , width=7, heigh=2, bg=color8, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt3.place(x=240,y=208)




janela.mainloop()




