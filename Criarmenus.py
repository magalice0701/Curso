import tkinter as tk
from tkinter import messagebox

def sobre():
    messagebox.showinfo('Sobre', 'Programa feito com Tkinter')

janela = tk.Tk()
janela.title('Menus do Tkinter')
janela.geometry('300x200')

menu_principal = tk.Menu(janela)
janela.config(menu=menu_principal)

menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_arquivo.add_command(label='Novo')
menu_arquivo.add_command(label='Abrir')
menu_arquivo.add_separator()
menu_arquivo.add_command(label='Sair', command=janela.quit)

menu_ajuda = tk.Menu(menu_principal, tearoff=0)
menu_ajuda.add_command(label='Sobre', command=sobre)

menu_principal.add_cascade(label='Arquivo', menu=menu_arquivo)
menu_principal.add_cascade(label='Ajuda', menu=menu_ajuda)

janela.mainloop()
