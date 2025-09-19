import tkinter as tk
from tkinter import messagebox, filedialog

def novo_arquivo():
    texto.delete("1.0", tk.END)
    messagebox.askyesno("Confirmar", "Você tem certeza que não quer salvar?")
    if "no": 
        command = salvar_arquivo

def abrir_arquivo():
    caminho = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if caminho:
        with open(caminho, "r") as file:
            conteudo = file.read()
        texto.delete("1.0", tk.END)
        texto.insert(tk.END, conteudo)

def salvar_arquivo():
    caminho = filedialog.asksaveasfilename(defaultextension=".txt")
    if caminho:
        with open(caminho, "w") as file:
            file.write(texto.get("1.0", tk.END))
        messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")

janela = tk.Tk()
janela.title("Editor Simples")
janela.geometry("400x300")

# Menu
menu_principal = tk.Menu(janela)
janela.config(menu=menu_principal)
menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_arquivo.add_command(label="Novo", command=novo_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)
menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)

# Barra de ferramentas
toolbar = tk.Frame(janela, bg="#BDC3C7")
toolbar.pack(side="top", fill="x")
tk.Button(toolbar, text="Novo", command=novo_arquivo).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Abrir", command=abrir_arquivo).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Salvar", command=salvar_arquivo).pack(side="left", padx=2, pady=2)

# Área de texto
texto = tk.Text(janela)
texto.pack(expand=True, fill="both")

janela.mainloop()
