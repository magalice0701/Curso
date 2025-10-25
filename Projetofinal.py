import tkinter as tk 
from tkinter import messagebox

def abrir_pix():
    top = tk.Toplevel()
    top.title("Pix")
    top.geometry("375x812")
    top.configure(bg='#BEFFBD')

    tk.Label(pix, text='Nome:', bg='#BEFFBD').grid(row=0, column=0, padx=10, pady=10)
    entrada_nome = tk.Entry(pix)
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(pix, text='Senha:', bg='#BEFFBD').grid(row=1, column=0, padx=10, pady=10)
    entrada_senha = tk.Entry(pix, show="*")
    entrada_senha.grid(row=1, column=1, padx=10, pady=10)

    def login():
        nome = entrada_nome.get().strip()
        senha = entrada_senha.get().strip()

        if not nome or not senha:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        if nome not in usuarios:
            messagebox.showerror("Erro", "Usuário não encontrado. Registre-se primeiro!")
            return

        if usuarios[nome] != senha:
            messagebox.showerror("Erro", "Senha incorreta!")
            return

        messagebox.showinfo("Bem-vindo!", f"Login bem-sucedido! Olá, {nome}!")

    tk.Button(pix, text="Login", command=login, bg="#6DAD6D", fg="white").grid(row=2, column=1, padx=10, pady=15)

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

usuarios = {}

def abrir_conta():
    """Janela de login e registro"""
    conta = tk.Toplevel()
    conta.title("Sua conta")
    conta.geometry("373x812")
    conta.configure(bg='#BEFFBD')

    tk.Label(conta, text='Nome:', bg='#BEFFBD').grid(row=0, column=0, padx=10, pady=10)
    entrada_nome = tk.Entry(conta)
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(conta, text='Senha:', bg='#BEFFBD').grid(row=1, column=0, padx=10, pady=10)
    entrada_senha = tk.Entry(conta, show="*")
    entrada_senha.grid(row=1, column=1, padx=10, pady=10)

    def registrar():
        nome = entrada_nome.get().strip()
        senha = entrada_senha.get().strip()

        if not nome or not senha:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        if nome in usuarios:
            messagebox.showerror("Erro", "Usuário já registrado! Faça login.")
            return

        usuarios[nome] = senha
        messagebox.showinfo("Sucesso", f"Conta registrada para {nome}!")
        entrada_nome.delete(0, tk.END)
        entrada_senha.delete(0, tk.END)

    def login():
        nome = entrada_nome.get().strip()
        senha = entrada_senha.get().strip()

        if not nome or not senha:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        if nome not in usuarios:
            messagebox.showerror("Erro", "Usuário não encontrado. Registre-se primeiro!")
            return

        if usuarios[nome] != senha:
            messagebox.showerror("Erro", "Senha incorreta!")
            return

        messagebox.showinfo("Bem-vindo!", f"Login bem-sucedido! Olá, {nome}!")

    tk.Button(conta, text="Registrar", command=registrar, bg="#6DAD6D", fg="white").grid(row=2, column=0, padx=10, pady=15)
    tk.Button(conta, text="Login", command=login, bg="#6DAD6D", fg="white").grid(row=2, column=1, padx=10, pady=15)
    
janela = tk.Tk()
janela.title("Banco")
janela.geometry("375x812")
janela.configure(bg="#BEFFBD")

texto = tk.Label(
    janela, 
    text='Bem-vindo(a) ao banco!!',
    fg='gray', 
    bg="#BEFFBD",
    font=('Verdana', 16, 'bold') 
)
texto.place(x=50, y=10)

texto = tk.Label(
    janela,
    text='Ainda estamos desenvolvendo o app!!',
    fg='gray',
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

#Caso a pessoa não tenha uma conta registrada não conseguir fazer nada 
#Ter uma parte para registrar uma conta com nome e senha
#Caso a pessoa não tenha uma conta registrada não conseguir fazer nada 


