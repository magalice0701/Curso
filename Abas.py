import tkinter as tk
from tkinter import ttk

class Sistema(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema com Abas")
        self.geometry("400x300")

        abas = ttk.Notebook(self)
        abas.pack(expand=True, fill="both")

        # Aba Cadastro
        aba_cadastro = tk.Frame(abas)
        tk.Label(aba_cadastro, text="Usuário:").pack(pady=5)
        self.usuario = tk.Entry(aba_cadastro)
        self.usuario.pack(pady=5)

        tk.Label(aba_cadastro, text="Senha:").pack(pady=5)
        self.senha = tk.Entry(aba_cadastro, show="*")
        self.senha.pack(pady=5)

        tk.Button(aba_cadastro, text="Cadastrar", command=self.cadastrar).pack(pady=10)

        # Aba Sobre
        aba_sobre = tk.Frame(abas)
        tk.Label(aba_sobre, text="Sistema desenvolvido em Tkinter", font=("Arial", 12)).pack(pady=20)

        abas.add(aba_cadastro, text="Cadastro")
        abas.add(aba_sobre, text="Sobre")

    def cadastrar(self):
        user = self.usuario.get()
        senha = self.senha.get()
        print(f"Usuário: {user}, Senha: {senha}")

def main():
    app = Sistema()
    app.mainloop()

if __name__ == "__main__":
    main()