import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

janela = tk.Tk
janela.title('Banco')
janela.geometry('300x200')

tk.Label(janela, text= 'Olá, bem-vindo ao banco!').pack(pady=20)
tk.Button(janela, text='Pix')

janela.mainloop()
#pix, pagamentos, transferir, recarga de celular 