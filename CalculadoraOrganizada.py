import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Simples")
        self.geometry("300x200")

        tk.Label(self, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)

        self.num1 = tk.Entry(self)
        self.num2 = tk.Entry(self)
        self.num1.grid(row=0, column=1)
        self.num2.grid(row=1, column=1)

        tk.Button(self, text="Somar", command=self.somar).grid(row=2, column=0, columnspan=2, pady=10)
        self.resultado = tk.Label(self, text="Resultado: ")
        self.resultado.grid(row=3, column=0, columnspan=2)

    def somar(self):
        try:
            n1 = float(self.num1.get())
            n2 = float(self.num2.get())
            self.resultado.config(text=f"Resultado: {n1 + n2}")
        except ValueError:
            self.resultado.config(text="Erro: Digite números válidos")

def main():
    app = Calculadora()
    app.mainloop()

if __name__ == "__main__":
    main()