import tkinter as tk  
from tkinter import messagebox

def abrir_janela_secundaria():
    top = tk.Toplevel(janela)
    top.title("Janela de cadastro")
    top.geometry("400x300")
    top.configure(bg='#fbd0f6')

    tk.Label(top, text='Nome:', bg='#fbd0f6').grid(row=0, column=0, padx=10, pady=10)
    entrada_nome = tk.Entry(top)
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(top, text='Idade:', bg='#fbd0f6').grid(row=1, column=0, padx=10, pady=10)
    entrada_idade = tk.Entry(top)
    entrada_idade.grid(row=1, column=1, padx=10, pady=10)

    def enviar():
        nome = entrada_nome.get()
        idade = entrada_idade.get()
        if idade.isdigit():
            messagebox.showinfo("Sucesso", f"Cadastro realizado!!\nNome: {nome}\nIdade: {idade}")
            top.destroy()
        else:
            messagebox.showerror("Erro", "A idade deve conter apenas números!")

    tk.Button(top, text='Enviar', command=enviar).grid(row=2, column=0, columnspan=2, pady=10)

janela = tk.Tk()
janela.title("Cadastro") 
janela.geometry("400x300")
janela.configure(bg='#fbd0f6')

texto = tk.Label(
    janela, 
    text='Inicie seu cadastro aqui!!',
    fg='white', 
    bg='#fbd0f6',
    font=('Arial', 16, 'bold') 
)
texto.pack(pady=30)

botao = tk.Button(
    janela,
    text='Iniciar cadastro',
    command=abrir_janela_secundaria, 
    bg='#da90d1',
    fg='white',
    font=('Monospace', 12, 'bold')
)

botao.pack(pady=20)

janela.mainloop()
