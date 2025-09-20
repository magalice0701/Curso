import tkinter as tk

def main(): 
    janela = tk.Tk()
    janela.title('Exemplo com main')
    janela.geometry('300x200')

    tk.Label(janela, text = 'Olá, Tkinter com main!').pack(pady=20)
    tk.Button(janela, text='Sair', command=janela.quit).pack(pady=10)

    janela.mainloop()

if __name__ == '__main__':
    main()