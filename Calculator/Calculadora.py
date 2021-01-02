from tkinter import *


# Ventana
win = Tk()
win.title("Pculator")
win.configure(background="#363636")
win.resizable(width=False, height=False)
win.iconbitmap("iconbitmap.ico")

# Input
input = Entry(win, width=27, font="Sans 13 bold", bg="Black", fg="White")
input.grid(column=0, row=0, columnspan=4)

# Definicion de variables:

# Al apretar un boton
def boton(numero):
    numeroanterior0 = input.get()
    input.delete(0, END)
    input.insert(0, str(numeroanterior0) + str(numero))

# Al apretar =
def igual():
    segunnum = input.get()
    input.delete(0, END)
    if mate == "sumar":
        input.insert(0, int(p_num) + int(segunnum))
    if mate == "multiplicar":
        input.insert(0, int(p_num) * int(segunnum))
    if mate == "restar":
        input.insert(0, int(p_num) - int(segunnum))
    if mate == "dividir":
        input.insert(0, int(p_num) / int(segunnum))

# Al apretar +

def suma():
    primernum = input.get()
    input.delete(0, END)
    global p_num
    global mate
    mate = "sumar"
    p_num = primernum

# Al apretar -

def resta():
    primernum = input.get()
    input.delete(0, END)
    global p_num
    global mate
    mate = "restar"
    p_num = primernum

# Al apretar /

def div():
    primernum = input.get()
    input.delete(0, END)
    global p_num
    global mate
    mate = "dividir"
    p_num = primernum

# Al apretar *

def multi():
    primernum = input.get()
    input.delete(0, END)
    global p_num
    global mate
    mate = "multiplicar"
    p_num = primernum


# Creacion de Botones con sus respectivos numeros

boton_1 = Button(win, text=1, width=7, height=3, bg="grey", fg="white", command=lambda: boton(1))
boton_1.grid(column=0, row=1, padx=2, pady=2)
boton_2 = Button(win, text=2, width=7, height=3, bg="grey", fg="white", command=lambda: boton(2))
boton_2.grid(column=1, row=1, padx=1, pady=1)
boton_3 = Button(win, text=3, width=7, height=3, bg="grey", fg="white", command=lambda: boton(3))
boton_3.grid(column=2, row=1, padx=1, pady=1)
boton_4 = Button(win, text=4, width=7, height=3, bg="grey", fg="white", command=lambda: boton(4))
boton_4.grid(column=0, row=2, padx=1, pady=1)
boton_5 = Button(win, text=5, width=7, height=3, bg="grey", fg="white", command=lambda: boton(5))
boton_5.grid(column=1, row=2, padx=1, pady=1)
boton_6 = Button(win, text=6, width=7, height=3, bg="grey", fg="white", command=lambda: boton(6))
boton_6.grid(column=2, row=2, padx=1, pady=1)
boton_7 = Button(win, text=7, width=7, height=3, bg="grey", fg="white", command=lambda: boton(7))
boton_7.grid(column=0, row=3, padx=1, pady=1)
boton_8 = Button(win, text=8, width=7, height=3, bg="grey", fg="white", command=lambda: boton(8))
boton_8.grid(column=1, row=3, padx=1, pady=1)
boton_9 = Button(win, text=9, width=7, height=3, bg="grey", fg="white", command=lambda: boton(9))
boton_9.grid(column=2, row=3, padx=1, pady=1)
boton_0 = Button(win, text=0, width=7, height=3, bg="grey", fg="white", command=lambda: boton(0))
boton_0.grid(column=0, row=4, padx=2, pady=2)

# Creacion de los Botones igual/suma/multiplicar/restar/dividir/limpiar

boton_igual = Button(win, text="=", width=7, height=3, bg="black", fg="white", command=lambda: igual())
boton_igual.grid(column=3, row=4)

boton_suma = Button(win, text="+", width=7, height=3, bg="black", fg="white", command=lambda: suma())
boton_suma.grid(column=2, row=4)

boton_multi = Button(win, text="*", width=7, height=3, bg="black", fg="white", command=lambda: multi())
boton_multi.grid(column=3, row=3)

boton_div = Button(win, text="/", width=7, height=3, bg="black", fg="white", command=lambda: div())
boton_div.grid(column=3, row=2)

boton_restar = Button(win, text="-", width=7, height=3, bg="black", fg="white", command=lambda: resta())
boton_restar.grid(column=1, row=4)

boton_limpiar = Button(win, text="Limpiar", width=7, height=3, bg="black", fg="white", command=lambda: input.delete(0, END))
boton_limpiar.grid(column=3, row=1)

# Cierre del proceso
win.mainloop()
