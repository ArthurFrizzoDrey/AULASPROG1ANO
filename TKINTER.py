#criando a primeira janela
from tkinter import *
#definindo variáveis de cores
#cor1= '#47d147' Verde Clara
#cor2= '#3385ff' Azul Clara
#cor3= '#4d0000' vermelha escura
janela= Tk() #T maiusculo
janela.title('Olá mundo')#criando o titulo da janela
janela.geometry('600x250') #Definindo o tamanho da janela 1- largura por x 2-Altura
janela.config(bg='#3385ff')#alterar cor de fundo da janela, rece um background, existe um site onde você poder ver as cores
janela.iconphoto(False, PhotoImage(file='transferir.png')) #este código altera o icone da janela.
janela.resizable(width=True, height=True) #Tornando a janela não redimencional
janela.mainloop() #SEMPRE NO FIM DO CODIGO - PERMITE QUE RODE CONSTANTEMENTE



