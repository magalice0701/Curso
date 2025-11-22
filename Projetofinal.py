import tkinter as tk
from tkinter import messagebox, simpledialog

usuarios = {}
saldo_global = 1000.00

def atualizar_saldo():
    saldo_label.config(text=f'Saldo: R$ {saldo_global:,.2f}')

def realizar_recarga(valor, operadora=None):
    global saldo_global
    
    if valor <= 0:
        messagebox.showerror("Erro", "O valor deve ser maior que zero!")
        return
        
    if valor > saldo_global:
        messagebox.showerror("Erro", "Saldo insuficiente!")
        return

    if operadora:
        confirmar = messagebox.askyesno(
            "Confirmar Recarga", 
            f"Você está prestes a recarregar R$ {valor:,.2f} na {operadora}.\nDeseja continuar?"
        )
    else:
        confirmar = messagebox.askyesno(
            "Confirmar Recarga", 
            f"Você está prestes a recarregar R$ {valor:,.2f}.\nDeseja continuar?"
        )
    
    if confirmar:
        saldo_global -= valor
        atualizar_saldo()
        if operadora:
            messagebox.showinfo(
                "Recarga Realizada!", 
                f"Recarga de R$ {valor:,.2f} na {operadora} realizada com sucesso!\n"
                f"Novo saldo: R$ {saldo_global:,.2f}"
            )
        else:
            messagebox.showinfo(
                "Recarga Realizada!", 
                f"Recarga de R$ {valor:,.2f} realizada com sucesso!\n"
                f"Novo saldo: R$ {saldo_global:,.2f}"
            )

def abrir_recarga():
    top = tk.Toplevel()
    top.title("Recarga de Celular")
    top.geometry("375x812")
    top.configure(bg='#BEFFBD')

    tk.Label(top, text='Nome:', bg='#BEFFBD').pack(pady=10)
    entrada_nome = tk.Entry(top)
    entrada_nome.pack(pady=5)

    tk.Label(top, text='Senha:', bg='#BEFFBD').pack(pady=10)
    entrada_senha = tk.Entry(top, show="*")
    entrada_senha.pack(pady=5)

    def mostrar_tela_recarga(nome):
        for widget in top.winfo_children():
            widget.destroy()

        tk.Label(top, text=f"Recarga de Celular - {nome}",
                 bg="#BEFFBD", fg="gray", font=("Verdana", 16, "bold")).pack(pady=20)

        frame_operadoras = tk.Frame(top, bg="#BEFFBD")
        frame_operadoras.pack(pady=10)

        tk.Label(frame_operadoras, text="Selecione a operadora:", 
                bg="#BEFFBD", font=("Verdana", 12, "bold")).pack(pady=5)

        operadoras = ["Vivo", "Claro", "Tim", "Oi", "Outras"]
        for operadora in operadoras:
            tk.Button(
                frame_operadoras,
                text=operadora,
                bg="#6DAD6D",
                fg="white",
                font=('Monospace', 10),
                width=12,
                command=lambda op=operadora: mostrar_valores_recarga(op)
            ).pack(side="left", padx=5, pady=5)

        tk.Button(top, text="Voltar", command=top.destroy,
                  bg="#6DAD6D", fg="white", width=10).pack(pady=20)

    def mostrar_valores_recarga(operadora):
        valores_window = tk.Toplevel(top)
        valores_window.title(f"Recarga - {operadora}")
        valores_window.geometry("300x400")
        valores_window.configure(bg='#BEFFBD')

        tk.Label(valores_window, text=f"Valores para {operadora}",
                 bg="#BEFFBD", fg="gray", font=("Verdana", 14, "bold")).pack(pady=20)
        valores = [20.00, 30.00, 40.00, 50.00]
        
        for valor in valores:
            tk.Button(
                valores_window,
                text=f"R$ {valor:,.2f}",
                bg="#6DAD6D",
                fg="white",
                font=('Monospace', 12, 'bold'),
                width=15,
                height=2,
                command=lambda v=valor, op=operadora: realizar_recarga(v, op)
            ).pack(pady=10)

        tk.Button(
            valores_window,
                text="Outro Valor",
                bg="#4A8C4A",
                fg="white",
                font=('Monospace', 12),
                width=15,
                command=lambda: abrir_valor_personalizado(operadora)
        ).pack(pady=10)

        tk.Button(valores_window, text="Voltar", command=valores_window.destroy,
                  bg="#6DAD6D", fg="white", width=10).pack(pady=10)

    def abrir_valor_personalizado(operadora):
        valor_str = simpledialog.askstring("Valor Personalizado", f"Digite o valor para {operadora}:")
        
        if valor_str is None: 
            return
            
        try:
            valor = float(valor_str.replace(',', '.'))
            realizar_recarga(valor, operadora)
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido!")

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
        mostrar_tela_recarga(nome)

    tk.Button(top, text="Login", command=login, bg="#6DAD6D", fg="white", width=10).pack(pady=20)

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

    def realizar_pix(contato):
        global saldo_global
        
        valor_str = simpledialog.askstring("Valor do Pix", f"Digite o valor para {contato}:")
        
        if valor_str is None: 
            return
            
        try:
            valor = float(valor_str.replace(',', '.'))
            
            if valor <= 0:
                messagebox.showerror("Erro", "O valor deve ser maior que zero!")
                return
                
            if valor > saldo_global:
                messagebox.showerror("Erro", "Saldo insuficiente!")
                return
                

            confirmar = messagebox.askyesno(
                "Confirmar Pix", 
                f"Você está prestes a transferir R$ {valor:,.2f} para {contato}.\nDeseja continuar?"
            )
            
            if confirmar:
                saldo_global -= valor
                atualizar_saldo()
                messagebox.showinfo(
                    "Pix Realizado!", 
                    f"Pix de R$ {valor:,.2f} para {contato} realizado com sucesso!\n"
                    f"Novo saldo: R$ {saldo_global:,.2f}"
                )
                
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido!")

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
                command=lambda c=contato: realizar_pix(c)
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
    ("Recarga", abrir_recarga),
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
