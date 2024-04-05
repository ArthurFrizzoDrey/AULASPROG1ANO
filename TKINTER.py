#IMPORTAR TKINTER E DAR NOME A JANELA
from tkinter import*
janela= Tk()
janela.title('Aprendendo Python')
janela.geometry("300x300")

#JOGUE SEU CÓDIGO PARA DENTRO DE UMA FUNÇÃO
def texto_clicado():
   texto= f'''
   TEM NADA AQUI NÃO KKKKK'''
   texto_pegadinha["text"]=texto

#CRIANDO A JANELA USANDO TKINTER

#texto da janela
texto_orientação=Label(janela,text='Clique no botão para exibir a mensagem')
texto_orientação.grid(column=0,row=0,padx=10,pady=10)

#botão
botão= Button(janela,text='MENSAGEM AQUI',command=texto_clicado)
botão.grid(column=0, row=2,padx=10,pady=10)

#deixando a informação na janela
texto_pegadinha=Label(janela,text='')
texto_pegadinha.grid(column=0,row=2,padx=10,pady=10)

#code responsavel por deixar a janela rodar
janela.mainloop()
#este código sempre será o último de sua janela