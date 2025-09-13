import tkinter as tk

def tecla_pressionada(event):
    label['text'] = f'Você pressionou: {event.keysym}'

def clique_mouse(event):
    label['text'] = f'Clique nas cordenadas: ({event.x}, {event.y})'

janela = tk.Tk()
janela.title('Eventos de teclado e mouse')
janela.geometry('300x150')

label = tk.Label(janela, text='Pressione um tecla ou clique')
label.pack(pady=20)

janela.bind('<Key>', tecla_pressionada)
janela.bind('<Button-1>', clique_mouse) #Botão esquerdo do mouse

janela.mainloop()