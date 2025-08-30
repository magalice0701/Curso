import tkinter as tk

def mostrarNome():
    nome_digitado = entrada.get()
    texto['text'] = f'Olá, {nome_digitado}'

janela = tk.Tk()
janela.title('Entrada de texto')
janela.geometry('1080x1080')

texto = tk.Label(janela, text= 'Digite o seu nome')
texto.pack(pady=10)

entrada = tk.Entry(janela)
entrada.pack(pady= 5)

botao = tk.Button(janela, text= 'Enviar', command=mostrarNome)
botao.pack(pady=10)

janela.mainloop()