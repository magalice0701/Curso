import tkinter as tk 

#1 - Criar a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela") # título da janela
janela.geometry("400x300") # definir o tamanho da janela

#2 Criar Widgets
texto = tk.Label(janela, text= 'Olá Mundo') # cria um texto
texto.pack(pady=20) # adiciona na janela com espaçamento

#3 Botão clicavel
botao = tk.Button(janela, text= 'Clique aqui') #cria um botão
botao.pack(pady=10) #adiciona na janela com espaçamento

#4 Executar janela
janela.mainloop() #mantém a janela aberta