#importanto tkinter

from tkinter import *
from tkinter import ttk

cor1 = "#3b3b3b" #cor preta
cor2 = "#feffff" #branca
cor3 = "#38576b" #azul
cor4 = "#eCeff1" #cizenta
cor5 = '#FFAB40' #orange


janela = Tk()
janela.title("Calculadora")
janela.geometry("320x425")
janela.config(bg=cor1)

# Criando frames

Frame_tela = Frame(janela, width=321, height=70, bg=cor3)
Frame_tela.grid(row=0, column=0)

Frame_corpo = Frame(janela, width=321, height=363)
Frame_corpo.grid(row=1, column=0)

#criando função

#variavel todos os valores

todos_valores = ''

# criando label
valor_texto = StringVar()

def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)


    #passando valor para a tela
    valor_texto.set(todos_valores)

#função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
#função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set("")





app_label = Label(Frame_tela, textvariable=valor_texto, width=19, height=3, padx=7, relief=FLAT, anchor="e", justify="right",font=('Ivy 20'), bg=cor3, fg=cor2 )
app_label.place(x=0, y=0)

#Criando botões

b_1 = Button(Frame_corpo,command= limpar_tela, text="C", width=15, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE) 
b_1.place(x=0, y=0)

b_2 = Button(Frame_corpo,command= lambda: entrar_valores('%'), text="%", width=7, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_2.place(x=160, y=0)

b_3 = Button(Frame_corpo,command= lambda: entrar_valores('/'), text="/", width=7, height=3, bg=cor5 , fg=cor2, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_3.place(x=240, y=0)

#linha1

b_4 = Button(Frame_corpo,command= lambda: entrar_valores('7'), text="7", width=7, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=71)

b_4 = Button(Frame_corpo,command= lambda: entrar_valores('8'), text="8", width=7, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_4.place(x=80, y=71)

b_5 = Button(Frame_corpo,command= lambda: entrar_valores('9'), text="9", width=7, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_5.place(x=160, y=71)


b_4 = Button(Frame_corpo,command= lambda: entrar_valores('*'), text="*", width=7, height=3, bg=cor5 , fg=cor2, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_4.place(x=240, y=71)

#linha 2

b_6 = Button(Frame_corpo,command= lambda: entrar_valores('4'), text="4", width=7, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_6.place(x=0, y=142)

b_7 = Button(Frame_corpo,command= lambda: entrar_valores('5'), text="5", width=7, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_7.place(x=80, y=142)

b_8 = Button(Frame_corpo,command= lambda: entrar_valores('6'), text="6", width=7, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_8.place(x=160, y=142)


b_9 = Button(Frame_corpo,command= lambda: entrar_valores('-'), text="-", width=7, height=3, bg=cor5 , fg=cor2, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_9.place(x=240, y=142)

#linha 3

b_10 = Button(Frame_corpo,command= lambda: entrar_valores('1'), text="1", width=7, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_10.place(x=0, y=213)

b_11 = Button(Frame_corpo,command= lambda: entrar_valores('2'), text="2", width=7, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_11.place(x=80, y=213)

b_12 = Button(Frame_corpo,command= lambda: entrar_valores('3'), text="3", width=7, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_12.place(x=160, y=213)


b_13 = Button(Frame_corpo,command= lambda: entrar_valores('+'), text="+", width=7, height=3, bg=cor5 , fg=cor2, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_13.place(x=240, y=213)


#utima linha 4
b_14 = Button(Frame_corpo,command= lambda: entrar_valores('0'), text="0", width=15, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE) 
b_14.place(x=0, y=284)

b_15 = Button(Frame_corpo,command= lambda: entrar_valores('.'), text=".", width=7, height=3, bg=cor4, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_15.place(x=160, y=284)

b_16 = Button(Frame_corpo,command = calcular , text="=", width=7, height=3, bg=cor5 , fg=cor2, font=('Ivy 13 bold '), relief=RAISED, overrelief=RIDGE)
b_16.place(x=240, y=284)




janela.mainloop()
