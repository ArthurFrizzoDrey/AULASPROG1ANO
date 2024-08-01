#criando a primeira janela
from tkinter import *
#definindo variáveis de cores
janela= Tk() #T maiusculo
janela.title('Olá mundo')#criando o titulo da janela
janela.geometry('600x250') #Definindo o tamanho da janela 1- largura por x 2-Altura
janela.config(bg='#4d0000')#alterar cor de fundo da janela, rece um background, existe um site onde você poder ver as cores
#janela.iconphoto(False, PhotoImage(file='logo.png')), este código altera o icone da janela.
janela.resizable(width=True, height=True) #Tornando a janela não redimencional
janela.mainloop() #SEMPRE NO FIM DO CODIGO - PERMITE QUE RODE CONSTANTEMENTE


