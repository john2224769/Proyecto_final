from tkinter import *
import numpy as np
import os
import io
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import messagebox

def guardar_dato():
    user_name=user.get() 
    user_code=code.get()
    user_placa=placa.get()
    tipo=vehiculo.get()
    newfile=open("matriz.txt", "a")
    newfile.write(user_name)
    newfile.write(" \t ")
    newfile.write(tipo)
    newfile.write(" \t ")
    newfile.write(user_code)
    newfile.write(" \t ")
    newfile.write(user_placa)
    newfile.close()
    entrada_nombre.delete(0, "end")
    entrada_codigo.delete(0, "end")
    entrada_placa.delete(0, "end")
    vehiculo.set("Pulse para ver las permitidas")

principal = Tk()

password = StringVar()
user = StringVar()
vehiculo= StringVar()
code =StringVar()
placa = StringVar()


principal.title("Sistema de Parqueadero UIS")

principal.geometry("1000x500")

principal.resizable(False,False)

principal.config(bg= "lime green")

target2 = Label(principal, text="Define que tipo de usuario eres: ")
target2.place(x=400 , y= 60)

label_titulo=Label(principal, text="Sistema de adminisracion de usuarios, parqueadero UIS", bg="lime green", fg="black", font=("Arial",15), 
compound="center")
label_titulo.place(x=10, y=10)

button_agregar=Button(principal,text=("Agregar usuario"), font=("arial", 15))
button_agregar.place(x=10,y=200)
#
## agregar despliega ventana con seleciones
Label_nombre=Label(principal, text="Ingresa el nombre", bg="lime green", fg="black", font=("Arial",15), compound="center")
Label_nombre.place(x=400, y=200)
entrada_nombre=Entry(principal,textvariable=user)
entrada_nombre.config(font=("Arial",20), justify=LEFT, fg="black")
entrada_nombre.place(x=400,y=230)

Label_codigo=Label(principal, text="Ingresa el codigo", bg="lime green", fg="black", font=("Arial",15), compound="center")
Label_codigo.place(x=400, y=270)
entrada_codigo=Entry(principal,textvariable=code)
entrada_codigo.config(font=("Arial",20), justify=LEFT, fg="black")
entrada_codigo.place(x=400,y=290)

Label_placa=Label(principal, text="Ingresa la placa", bg="lime green", fg="black", font=("Arial",15), compound="center")
Label_placa.place(x=400, y=340)
entrada_placa=Entry(principal,textvariable=placa)
entrada_placa.config(font=("Arial",20), justify=LEFT, fg="black")
entrada_placa.place(x=400,y=360)


boton_guardar=Button(principal,text=("Guardar"),command=guardar_dato)
boton_guardar.place(x=400, y=400)

button_modificar=Button(principal,text=("Modificar usuario"), font=("arial", 15))
button_modificar.place(x=10,y=250)

button_eliminar=Button(principal,text=("Eliminar usuario"), font=("arial", 15))
button_eliminar.place(x=10,y=300)

button_salir=Button(principal,text=("Salir"), font=("arial", 15), command=principal.destroy)
button_salir.place(x=400,y=450)

principal.mainloop()