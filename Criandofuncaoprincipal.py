# import tkinter as tk

# def main():
#     janela = tk.Tk()
#     janela.title('Exemplo de main')
#     janela.geometry('300x200')

#     tk.Label(janela, text='Olá mundo!!').pack(pady=20)
#     tk.Button(janela, text='Sair', command= janela.quit).pack(pady=10)

#     janela.mainloop()

# if __name__ == '__main__':
#     main()

import tkinter as tk

class MinhaJanela(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter com Classe')
        self.geometry('300x200')

        self.texto = tk.Label(self, text= 'Bem-Vindo')
        self.texto.pack(pady=20)

        botao = tk.Button(self, text='Clique', command=self.mudar_texto)
        botao.pack(pady=10)

    def mudar_texto(self):
        self.texto.config(text='Você clicou no botão')

def main():
    app = MinhaJanela()
    app.mainloop()

if __name__ == '__main__':
    main()