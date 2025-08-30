import tkinter as tk

def somar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado['text'] = f'Resultado: {num1 + num2}'

def subtrair():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado['text'] = f'Resultado: {num1 - num2}'

def multiplicar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado['text'] = f'Resultado: {num1 * num2}'

def dividir():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado['text'] = f'Resultado: {num1 / num2}'


janela = tk.Tk()
janela.title('Mini Calculadora')
janela.geometry('300x250')

#Número 1 
tk.Label(janela, text='Número 1:').pack(pady=5)
entrada1 = tk.Entry(janela)
entrada1.pack(pady=5)

#Número 2
tk.Label(janela, text='Número 2:').pack(pady=5)
entrada2 = tk.Entry(janela)
entrada2.pack(pady=5)

#Botão somar
tk.Button(janela, text= 'Somar', command=somar).pack(pady=10)

#Botão subtrair
tk.Button(janela, text= 'Subtrair', command=subtrair).pack(pady=10)

#Botão dividir
tk.Button(janela, text= 'Dividir', command=dividir).pack(pady=10)

#Botão multiplicar
tk.Button(janela, text= 'Multiplicar', command=multiplicar).pack(pady=10)


#Resultado
resultado = tk.Label(janela, text='Resultado: ')
resultado.pack(pady=10)

janela.mainloop()