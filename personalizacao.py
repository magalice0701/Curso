import tkinter as tk

janela = tk.Tk()
janela.title('Personalização')
janela.geometry('400x300')
janela.configure(bg='#2C3E50') #Fundo da janela 

texto = tk.Label(
    janela, 
    text='Hello word',
    fg='white', #cor do texto
    bg= '#2C3E50',
    font=('Arial', 16, 'bold') #fonte, tamanho e estilo
)
texto.pack(pady=30)

botao=tk.Button(
    janela,
    text='Clique Aqui',
    bg='#E74C3C',
    fg='white',
    font=('Verdana', 12, 'bold')
)
botao.pack(pady=10)

janela.mainloop()