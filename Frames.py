import tkinter as tk 

janela = tk.Tk()
janela.title('Exemplo com Frames')
janela.geometry('400x200')

frame1 = tk.Frame(janela, bg='lightblue')
frame1.pack(fill='x')

frame2 = tk.Frame(janela, bg='lightgreen')
frame2.pack(expand=True, fill='both')

tk.Label(frame1, text='Topo').pack(pady=10)
tk.Label(frame2, text='Conteúdo principal').pack(pady=20)

janela.mainloop()