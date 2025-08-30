import tkinter as tk

def mensagem():
    texto['text'] = 'Você clicou no botão!!'

janela = tk.Tk()
janela.title('Exemplo de evento')
janela.geometry('400x200')

texto = tk.Label(janela, text = 'Clique no botão abaixo')
texto.pack(pady=20)

botao = tk.Button(janela, text = 'Clique aqui', command=mensagem)
botao.pack(pady=10)
# botao.pack(pady =10, padx= 50, side = 'top')

janela.mainloop()