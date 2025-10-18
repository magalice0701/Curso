import tkinter as tk 
from tkinter import messagebox

def abrir_pix():
    top = tk.Toplevel()
    top.title("Pix")
    top.geometry("375x812")
    top.configure(bg='#BEFFBD')

def abrir_pagamentos():
    top = tk.Toplevel()
    top.title("Pagamentos")
    top.geometry("375x812")
    top.configure(bg='#BEFFBD')

def abrir_transferir():
    top = tk.Toplevel()
    top.title("Transferir")
    top.geometry("375x812")
    top.configure(bg='#BEFFBD')

def abrir_recarga():
    top = tk.Toplevel()
    top.title("Recarga")
    top.geometry("375x812")
    top.configure(bg='#BEFFBD')

def abrir_conta():
    top = tk.Toplevel()
    top.title("Sua conta")
    top.geometry("373x812")
    top.configure(bg='#BEFFBD')

    tk.Label(top, text='Nome:', bg='#BEFFBD').grid(row=0, column=0, padx=10, pady=10)
    entrada_nome = tk.Entry(top)
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(top, text='Senha:', bg='#BEFFBD').grid(row=1, column=0, padx=10, pady=10)
    entrada_idade = tk.Entry(top)
    entrada_idade.grid(row=1, column=1, padx=10, pady=10)

    def enviar():
        nome = entrada_nome.get()
        senha = entrada_idade.get()

        if not nome or not senha:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos!!')
        elif senha.isdigit():
            messagebox.showinfo("Sucesso", f"Cadastro realizado!!\nNome: {nome}\nSenha: {senha}")
            top.destroy()
        else:
            messagebox.showerror("Erro", "A idade deve conter apenas números!")

    tk.Button(top, text='Enviar', command=enviar).grid(row=2, column=0, columnspan=2, pady=10)

janela = tk.Tk()
janela.title("Banco")
janela.geometry("375x812")
janela.configure(bg="#BEFFBD")

texto = tk.Label(
    janela, 
    text='Bem-vindo(a) ao banco!!',
    fg='white', 
    bg="#BEFFBD",
    font=('Verdana', 16, 'bold') 
)
texto.place(x=50, y=10)

texto = tk.Label(
    janela,
    text='Ainda estamos desenvolvendo o app!!',
    fg='black',
    bg="#BEFFBD",
    font=('Verdana', 12, 'bold') 
)
texto.place(x=20, y=700)

pix = tk.Button(
    janela,
    text='Pix',
    command=abrir_pix, 
    bg="#6DAD6D",
    fg='white',
    font=('Monospace', 12, 'bold')
)
pix.place(x=10, y=84)

pagamentos = tk.Button(
    janela,
    text='Pagamentos',
    command=abrir_pagamentos, 
    bg="#6DAD6D",
    fg='white',
    font=('Monospace', 12, 'bold')
)
pagamentos.place(x=70, y=84)

transferir = tk.Button(
    janela,
    text='Transferir',
    command=abrir_transferir, 
    bg="#6DAD6D",
    fg='white',
    font=('Monospace', 12, 'bold')
)
transferir.place(x=280 ,y=84)

recarga = tk.Button(
    janela,
    text='Recarga',
    command=abrir_recarga, 
    bg="#6DAD6D",
    fg='white',
    font=('Monospace', 12, 'bold')
)
recarga.place(x=190 ,y=84)

conta = tk.Button(
    janela,
    text='Conta',
    command=abrir_conta,
    bg="#6DAD6D",
    fg='white',
    font=('Monospace', 12, 'bold')
)
conta.place(x=155, y=130)

sair = tk.Button(
    janela,
    text='Sair',
    command=janela.quit, 
    bg="#6DAD6D",
    fg='white',
    font=('Monospace', 12, 'bold')
)
sair.place(x=165, y=300)

janela.mainloop()

#Ter uma parte para registrar uma conta com nome e senha
#Caso a pessoa não tenha uma conta registrada não conseguir fazer nada 

