import tkinter as tk 
from tkinter import messagebox

def abrir_pix():
    top = tk.Toplevel()
    top.title("Pix")
    top.geometry("400x300")
    top.configure(bg='#9932CC')

janela = tk.Tk()
janela.title("Banco")
janela.geometry("400x300")
janela.configure(bg="#9932CC")

texto = tk.Label(
    janela, 
    text='Bem-vindo(a) ao banco!!',
    fg='white', 
    bg="#9932CC",
    font=('Verdana', 16, 'bold') 
)
texto.grid(row=0, column=0, columnspan=4, pady=10)

pix = tk.Button(
    janela,
    text='Pix',
    command=abrir_pix, 
    bg="#DDA0DD",
    fg='white',
    font=('Monospace', 12, 'bold')
)
pix.grid(row=1, column=1, padx=20, pady=20)

pagamentos = tk.Button(
    janela,
    text='Pagamentos',
    command=abrir_pix, 
    bg="#DDA0DD",
    fg='white',
    font=('Monospace', 12, 'bold')
)
pagamentos.grid(row=1, column=2, padx=20, pady=20)

transferir = tk.Button(
    janela,
    text='Transferir',
    command=abrir_pix, 
    bg="#DDA0DD",
    fg='white',
    font=('Monospace', 12, 'bold')
)
transferir.grid(row=1, column=3, padx=20, pady=20)

recarga = tk.Button(
    janela,
    text='Recarga de celular',
    command=abrir_pix, 
    bg="#DDA0DD",
    fg='white',
    font=('Monospace', 12, 'bold')
)
recarga.grid(row=1, column=4, padx=20, pady=20)

janela.mainloop()

#pix, pagamentos, transferir, recarga de celular 
