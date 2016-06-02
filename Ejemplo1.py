print("Escuela Politecnica Nacional")
print("Escuela de Formacion de Tecnologos")
print(" Programación Avanzada")
print ("Arias Michelle\n Criollo Katherine")
print("")

def hello():
    print ("Hola a todos")

from tkinter import *
tk = Tk()
btn = Button(tk, text="click me", command=hello)
btn.pack()
 