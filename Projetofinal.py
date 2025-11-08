import tkinter as tk
from tkinter import messagebox

usuarios = {}
saldo_global = 1000.00

def abrir_pix():
    top = tk.Toplevel()
    top.title("Pix")
    top.geometry("375x812")
    top.configure(bg='#BEFFBD')

    tk.Label(top, text='Nome:', bg='#BEFFBD').pack(pady=10)
    entrada_nome = tk.Entry(top)
    entrada_nome.pack(pady=5)

    tk.Label(top, text='Senha:', bg='#BEFFBD').pack(pady=10)
    entrada_senha = tk.Entry(top, show="*")
    entrada_senha.pack(pady=5)

    def mostrar_tela_pix(nome):
        for widget in top.winfo_children():
            widget.destroy()

        tk.Label(top, text=f"Bem-vindo(a) ao Pix, {nome}!",
                 bg="#BEFFBD", fg="gray", font=("Verdana", 16, "bold")).pack(pady=30)

        tk.Label(top, text="Contatos frequentes:", bg="#BEFFBD", font=("Verdana", 12, "bold")).pack(pady=5)

        contatos = ["Loja", "Mãe", "Pai", "Dentista"]
        for contato in contatos:
            tk.Button(
                top,
                text=contato,
                bg="#6DAD6D",
                fg="white",
                font=('Monospace', 12),
                width=15,
                command=lambda c=contato: messagebox.showinfo("Pix", f"Você selecionou {c}")
            ).pack(pady=10)

        tk.Button(top, text="Voltar", command=top.destroy,
                  bg="#6DAD6D", fg="white", width=10).pack(pady=30)

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
        mostrar_tela_pix(nome)

    tk.Button(top, text="Login", command=login, bg="#6DAD6D", fg="white", width=10).pack(pady=20)


def abrir_login_generico(titulo):
    top = tk.Toplevel()
    top.title(titulo)
    top.geometry("375x812")
    top.configure(bg='#BEFFBD')

    tk.Label(top, text=f'{titulo}', bg='#BEFFBD', font=('Verdana', 16, 'bold')).pack(pady=15)

    tk.Label(top, text='Nome:', bg='#BEFFBD').pack(pady=10)
    entrada_nome = tk.Entry(top)
    entrada_nome.pack(pady=5)

    tk.Label(top, text='Senha:', bg='#BEFFBD').pack(pady=10)
    entrada_senha = tk.Entry(top, show="*")
    entrada_senha.pack(pady=5)

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

    tk.Button(top, text="Login", command=login, bg="#6DAD6D", fg="white", width=10).pack(pady=20)


def abrir_conta():
    conta = tk.Toplevel()
    conta.title("Sua conta")
    conta.geometry("375x812")
    conta.configure(bg='#BEFFBD')

    tk.Label(conta, text='Cadastro / Login', bg='#BEFFBD', font=('Verdana', 16, 'bold')).pack(pady=15)

    tk.Label(conta, text='Nome:', bg='#BEFFBD').pack(pady=10)
    entrada_nome = tk.Entry(conta)
    entrada_nome.pack(pady=5)

    tk.Label(conta, text='Senha:', bg='#BEFFBD').pack(pady=10)
    entrada_senha = tk.Entry(conta, show="*")
    entrada_senha.pack(pady=5)

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

    frame_botoes = tk.Frame(conta, bg="#BEFFBD")
    frame_botoes.pack(pady=20)

    tk.Button(frame_botoes, text="Registrar", command=registrar, bg="#6DAD6D", fg="white", width=10).pack(side="left", padx=10)
    tk.Button(frame_botoes, text="Login", command=login, bg="#6DAD6D", fg="white", width=10).pack(side="left", padx=10)

janela = tk.Tk()
janela.title("Banco")
janela.geometry("375x812")
janela.configure(bg="#BEFFBD")

tk.Label(
    janela,
    text='Bem-vindo(a) ao banco!',
    fg='gray',
    bg="#BEFFBD",
    font=('Verdana', 16, 'bold')
).pack(pady=15)

saldo_label = tk.Label(
    janela,
    text=f'Saldo: R$ {saldo_global:,.2f}',
    fg='green',
    bg="#BEFFBD",
    font=('Verdana', 14, 'bold')
)
saldo_label.pack(pady=10)

botoes = [
    ("Pix", abrir_pix),
    ("Pagamentos", lambda: abrir_login_generico("Pagamentos")),
    ("Transferir", lambda: abrir_login_generico("Transferir")),
    ("Recarga", lambda: abrir_login_generico("Recarga")),
    ("Conta", abrir_conta),
    ("Sair", janela.quit)
]

for texto, comando in botoes:
    tk.Button(
        janela,
        text=texto,
        command=comando,
        bg="#6DAD6D",
        fg='white',
        font=('Monospace', 12, 'bold'),
        width=20
    ).pack(pady=10)

tk.Label(
    janela,
    text='Ainda estamos desenvolvendo o app!',
    fg='gray',
    bg="#BEFFBD",
    font=('Verdana', 12, 'bold')
).pack(side="bottom", pady=30)

janela.mainloop()
