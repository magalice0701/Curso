import tkinter as tk

janela = tk.Tk()
janela.title('Exemplo grid')
janela.geometry("300x200")

tk.Label(janela, text= 'Nome: ').grid(row=0, column=0, padx= 10,)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text='Idade').grid(row=1, column=0, padx=10, pady=10)
entrada_idade=tk.Entry(janela)
entrada_idade.grid(row=1, column=1, padx=10, pady=10)

tk.Button(janela, text='Enviar').grid(row=2, column=0, columnspan=2, pady=10)

janela.mainloop()