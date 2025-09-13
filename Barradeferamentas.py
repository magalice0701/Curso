import tkinter as tk
from tkinter import messagebox

def salvar():
    messagebox.showinfo('Ação', 'Arquivo salvo!')

janela = tk.Tk()
janela.title('Barra de Feramentas')
janela.geometry('300x400')

tollbar = tk.Frame(janela, bg='#95A5A6')
tollbar.pack(side='top', fill='x')

tk.Button(tollbar, text='Salvar', command=salvar).pack(side='left', padx=2, pady=2)
tk.Button(tollbar, text='Sair', command=janela.quit).pack(side='left', padx=2, pady=2)

janela.mainloop()