import tkinter as tk

janela = tk.Tk()
janela.title('Imagem no Tkinter')

#Imagem PNG
img = tk.PhotoImage(file= 'Habbo Pixel.png')

label_imagem = tk.Label(janela, image=img)
label_imagem.pack(pady=20)


janela.mainloop()