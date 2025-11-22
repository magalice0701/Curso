import tkinter as tk
from tkinter import messagebox, simpledialog

usuarios = {}
saldo_global = 1000.00

def atualizar_saldo():
    saldo_label.config(text=f'Saldo: R$ {saldo_global:,.2f}')

def realizar_transacao(valor, descricao, tipo="transação"):
    global saldo_global
    
    if valor <= 0:
        messagebox.showerror("Erro", "O valor deve ser maior que zero!")
        return False
        
    if valor > saldo_global:
        messagebox.showerror("Erro", "Saldo insuficiente!")
        return False
        
    confirmar = messagebox.askyesno(
        f"Confirmar {tipo.title()}", 
        f"Você está prestes a realizar {descricao}.\nDeseja continuar?"
    )
    
    if confirmar:
        saldo_global -= valor
        atualizar_saldo()
        messagebox.showinfo(
            f"{tipo.title()} Realizada!", 
            f"{descricao} realizada com sucesso!\n"
            f"Novo saldo: R$ {saldo_global:,.2f}"
        )
        return True
    return False

def realizar_recarga(valor, operadora=None):
    if operadora:
        descricao = f"recarga de R$ {valor:,.2f} na {operadora}"
    else:
        descricao = f"recarga de R$ {valor:,.2f}"
    
    realizar_transacao(valor, descricao, "recarga")

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

        # Frame para operadoras
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
        # Nova janela para valores
        valores_window = tk.Toplevel(top)
        valores_window.title(f"Recarga - {operadora}")
        valores_window.geometry("300x400")
        valores_window.configure(bg='#BEFFBD')

        tk.Label(valores_window, text=f"Valores para {operadora}",
                 bg="#BEFFBD", fg="gray", font=("Verdana", 14, "bold")).pack(pady=20)

        # Botões com valores pré-definidos
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

        # Botão para valor personalizado
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
        
        if valor_str is None:  # Usuário cancelou
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

def abrir_pagamentos():
    top = tk.Toplevel()
    top.title("Pagamentos")
    top.geometry("375x812")
    top.configure(bg='#BEFFBD')

    tk.Label(top, text='Nome:', bg='#BEFFBD').pack(pady=10)
    entrada_nome = tk.Entry(top)
    entrada_nome.pack(pady=5)

    tk.Label(top, text='Senha:', bg='#BEFFBD').pack(pady=10)
    entrada_senha = tk.Entry(top, show="*")
    entrada_senha.pack(pady=5)

    def mostrar_tela_pagamentos(nome):
        for widget in top.winfo_children():
            widget.destroy()

        tk.Label(top, text=f"Pagamentos - {nome}",
                 bg="#BEFFBD", fg="gray", font=("Verdana", 16, "bold")).pack(pady=20)

        tk.Label(top, text="Contas para pagar:", 
                bg="#BEFFBD", font=("Verdana", 12, "bold")).pack(pady=10)

        # Contas pré-cadastradas
        contas = [
            {"nome": "Conta de Luz", "valor": 150.00, "vencimento": "10/12/2024"},
            {"nome": "Internet", "valor": 99.90, "vencimento": "15/12/2024"},
            {"nome": "Água", "valor": 80.50, "vencimento": "05/12/2024"},
            {"nome": "Cartão de Crédito", "valor": 350.00, "vencimento": "20/12/2024"},
            {"nome": "Aluguel", "valor": 1200.00, "vencimento": "01/12/2024"}
        ]

        for conta in contas:
            frame_conta = tk.Frame(top, bg="#BEFFBD")
            frame_conta.pack(pady=8, fill="x", padx=20)
            
            tk.Label(frame_conta, 
                    text=f"{conta['nome']}\nR$ {conta['valor']:,.2f} - Vence: {conta['vencimento']}",
                    bg="#BEFFBD",
                    font=('Monospace', 10),
                    justify="left").pack(side="left")
            
            tk.Button(frame_conta,
                    text="Pagar",
                    bg="#6DAD6D",
                    fg="white",
                    font=('Monospace', 9),
                    width=8,
                    command=lambda c=conta: pagar_conta(c)
            ).pack(side="right")

        # Botão para pagar conta personalizada
        tk.Button(top,
                text="Pagar Outra Conta",
                bg="#4A8C4A",
                fg="white",
                font=('Monospace', 12),
                width=20,
                command=pagar_conta_personalizada
        ).pack(pady=20)

        tk.Button(top, text="Voltar", command=top.destroy,
                  bg="#6DAD6D", fg="white", width=10).pack(pady=10)

    def pagar_conta(conta):
        descricao = f"pagamento de {conta['nome']} no valor de R$ {conta['valor']:,.2f}"
        realizar_transacao(conta['valor'], descricao, "pagamento")

    def pagar_conta_personalizada():
        # Solicitar dados da conta
        nome_conta = simpledialog.askstring("Nova Conta", "Digite o nome da conta:")
        if not nome_conta:
            return
            
        valor_str = simpledialog.askstring("Valor da Conta", f"Digite o valor para {nome_conta}:")
        if not valor_str:
            return
            
        try:
            valor = float(valor_str.replace(',', '.'))
            descricao = f"pagamento de {nome_conta} no valor de R$ {valor:,.2f}"
            realizar_transacao(valor, descricao, "pagamento")
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
        mostrar_tela_pagamentos(nome)

    tk.Button(top, text="Login", command=login, bg="#6DAD6D", fg="white", width=10).pack(pady=20)

def abrir_transferir():
    top = tk.Toplevel()
    top.title("Transferência")
    top.geometry("375x812")
    top.configure(bg='#BEFFBD')

    tk.Label(top, text='Nome:', bg='#BEFFBD').pack(pady=10)
    entrada_nome = tk.Entry(top)
    entrada_nome.pack(pady=5)

    tk.Label(top, text='Senha:', bg='#BEFFBD').pack(pady=10)
    entrada_senha = tk.Entry(top, show="*")
    entrada_senha.pack(pady=5)

    def mostrar_tela_transferir(nome):
        for widget in top.winfo_children():
            widget.destroy()

        tk.Label(top, text=f"Transferência - {nome}",
                 bg="#BEFFBD", fg="gray", font=("Verdana", 16, "bold")).pack(pady=20)

        tk.Label(top, text="Transferir para:", 
                bg="#BEFFBD", font=("Verdana", 12, "bold")).pack(pady=10)

        # Bancos disponíveis
        bancos = ["Banco do Brasil", "Itaú", "Bradesco", "Santander", "Caixa", "Nubank", "Inter", "Outro Banco"]

        frame_bancos = tk.Frame(top, bg="#BEFFBD")
        frame_bancos.pack(pady=10)

        # Primeira linha de bancos
        for i in range(4):
            banco = bancos[i]
            tk.Button(
                frame_bancos,
                text=banco,
                bg="#6DAD6D",
                fg="white",
                font=('Monospace', 9),
                width=15,
                height=2,
                command=lambda b=banco: transferir_para_banco(b)
            ).grid(row=0, column=i, padx=5, pady=5)

        # Segunda linha de bancos
        for i in range(4, 8):
            banco = bancos[i]
            tk.Button(
                frame_bancos,
                text=banco,
                bg="#6DAD6D",
                fg="white",
                font=('Monospace', 9),
                width=15,
                height=2,
                command=lambda b=banco: transferir_para_banco(b)
            ).grid(row=1, column=i-4, padx=5, pady=5)

        tk.Button(top, text="Voltar", command=top.destroy,
                  bg="#6DAD6D", fg="white", width=10).pack(pady=20)

    def transferir_para_banco(banco):
        # Solicitar dados da transferência
        valor_str = simpledialog.askstring("Valor da Transferência", f"Digite o valor para transferir para {banco}:")
        if not valor_str:
            return
            
        try:
            valor = float(valor_str.replace(',', '.'))
            
            # Solicitar conta destino
            conta_destino = simpledialog.askstring("Conta Destino", "Digite o número da conta destino:")
            if not conta_destino:
                return
                
            # Solicitar agência (se não for banco digital)
            if banco not in ["Nubank", "Inter"]:
                agencia = simpledialog.askstring("Agência", "Digite a agência destino:")
                if not agencia:
                    return
                descricao = f"transferência de R$ {valor:,.2f} para {banco} - Ag: {agencia} CC: {conta_destino}"
            else:
                descricao = f"transferência de R$ {valor:,.2f} para {banco} - CC: {conta_destino}"
            
            realizar_transacao(valor, descricao, "transferência")
            
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
        mostrar_tela_transferir(nome)

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
        valor_str = simpledialog.askstring("Valor do Pix", f"Digite o valor para {contato}:")
        
        if valor_str is None:
            return
            
        try:
            valor = float(valor_str.replace(',', '.'))
            descricao = f"Pix de R$ {valor:,.2f} para {contato}"
            realizar_transacao(valor, descricao, "pix")
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
    ("Pagamentos", abrir_pagamentos),
    ("Transferir", abrir_transferir),
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
