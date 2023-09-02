from tkinter import *
from tkinter import messagebox

def calcularImc() -> None:
    peso = float(entrada_peso.get())
    altura = float(entrada_altura.get())

    resultado = peso / altura**2
    messagebox.showinfo("Resultado", f"Seu IMC é: {resultado:.2f}")
    entrada_peso.delete(0, END)
    entrada_altura.delete(0, END)

janela = Tk()

janela.title("Primeira Janela")

janela.geometry("350x300")

label_peso = Label(janela, text="Peso: ", fg="red", font="Arial 14 bold")
entrada_peso = Entry(janela, font="Arial 13 bold")

label_altura = Label(janela, text="Altura: ", fg="red", font="Arial 14 bold")
entrada_altura = Entry(janela, font="Arial 13 bold")

botao_calcular = Button(janela, text="Calcular", fg="blue", width=7, height=2, font="Arial 14 bold", bg="yellow", command=calcularImc)

label_peso.grid(row=0, column=0)
entrada_peso.grid(row=0, column=1)

label_altura.grid(row=1, column=0)
entrada_altura.grid(row=1, column=1)

botao_calcular.grid(row=2, column=1)

janela.mainloop()
