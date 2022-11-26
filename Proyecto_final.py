from tkinter import *
import time  


principal = Tk()

password = StringVar()
user = StringVar()
vehiculo= StringVar()
code =StringVar()
placa = StringVar()

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
    #entrada_nombre.delete(0, "end")
    #entrada_codigo.delete(0, "end")
    #entrada_placa.delete(0, "end")
    vehiculo.set("Pulse para ver las permitidas")


######################################################################################################################################
#ventana principal

principal.title("Sistema de Parqueadero UIS")

principal.geometry("1000x500")

principal.resizable(False,False)

principal.config(bg= "lime green")

target2 = Label(principal, text="Define que tipo de usuario eres: ")
target2.place(x=400 , y= 60)

##############################################################################################################################################
# ventana de usuario 

label_usuario=Label(principal, text="Ingresa tu usuario", bg="lime green", fg="black", font=("Arial",15), compound="center")
label_usuario.place(x=400, y= 200)
entrada_usuario=Entry(principal,textvariable=password)
entrada_usuario.config(font=("Arial",20), justify=LEFT, fg="black")
entrada_usuario.focus_set()
entrada_usuario.place(x=400,y=240)

Label_password=Label(principal, text="Ingresa tu contraseña", bg="lime green", fg="black", font=("Arial",15), compound="center")
Label_password.place(x=400, y=290)
entrada_password=Entry(principal,textvariable=user)
entrada_password.config(font=("Arial",20), justify=LEFT, fg="black")
entrada_password.place(x=400,y=330)

button_ingresar=Button(principal,text=("Acceder"))
button_ingresar.place(x=400, y=380)
button_ingresar.config(font=("Arial",15))

######################
#opciones user 
label_titulo=Label(principal, text="Sistema de usuarios, parqueadero UIS", bg="lime green", fg="black", font=("Arial",15), compound="center")
label_titulo.place(x=10, y=10)

#Label_titulo=Label(principal, text="Selecciona una opción", bg="lime green", fg="black", font=("Arial",15), compound="center")
#Label_titulo.place(x=400, y=290)
button_mostrarqr=Button(principal,text=("Ver codigo QR"))
button_mostrarqr.place(x=600, y=380)
button_mostrarqr.config(font=("Arial",15))



#####################################################################
# seleccion de vehiculo con opciones 
tipo_v=OptionMenu(principal, vehiculo, "Automovil", "Motocicleta", "Bicicleta" )
vehiculo.set("Pulse para seleccionar el tipo de vehiculo")
tipo_v.grid(row=2, column=1, sticky= "w", padx=10)
tipo_v.place(x=100, y=450)

##############################################################################################################################################
#ventana admin
label_admin=Label(principal, text="Ingresa tu usuario", bg="lime green", fg="black", font=("Arial",15), compound="center")
label_admin.place(x=400, y= 200)

entrada_admin=Entry(principal,textvariable=password)
entrada_admin.config(font=("Arial",20), justify=LEFT, fg="black")
entrada_admin.focus_set()
entrada_admin.place(x=400,y=240)

Label_password=Label(principal, text="Ingresa tu contraseña", bg="lime green", fg="black", font=("Arial",15), compound="center")
Label_password.place(x=400, y=290)

entrada_password=Entry(principal,textvariable=user)
entrada_password.config(font=("Arial",20), justify=LEFT, fg="black")
entrada_password.place(x=400,y=330)

button_ingresar=Button(principal,text=("Acceder"))
button_ingresar.place(x=400, y=380)
button_ingresar.config(font=("Arial",15))

################
#opciones admin 

label_titulo=Label(principal, text="Sistema de adminisracion de usuarios, parqueadero UIS", bg="lime green", fg="black", font=("Arial",15), 
compound="center")
label_titulo.place(x=10, y=10)

button_agregar=Button(principal,text=("Agregar usuario"), font=("arial", 15))
button_agregar.place(x=10,y=200)
#################################################
########## agregar despliega ventana con seleciones
######## Label_nombre=Label(principal, text="Ingresa el nombre", bg="lime green", fg="black", font=("Arial",15), compound="center")
######## Label_nombre.place(x=400, y=290)
######## entrada_nombre=Entry(principal,textvariable=user)
######## entrada_nombre.config(font=("Arial",20), justify=LEFT, fg="black")
######## entrada_nombre.place(x=400,y=330)

######## Label_codigo=Label(principal, text="Ingresa el codigo", bg="lime green", fg="black", font=("Arial",15), compound="center")
######## Label_codigo.place(x=400, y=290)
######## entrada_codigo=Entry(principal,textvariable=code)
######## entrada_codigo.config(font=("Arial",20), justify=LEFT, fg="black")
######## entrada_codigo.place(x=400,y=380)

######## Label_placa=Label(principal, text="Ingresa la placa", bg="lime green", fg="black", font=("Arial",15), compound="center")
######## Label_placa.place(x=400, y=290)
######## entrada_placa=Entry(principal,textvariable=code)
######## entrada_placa.config(font=("Arial",20), justify=LEFT, fg="black")
######## entrada_placa.place(x=400,y=420)

######## boton_guardar=Button(principal,text=("Guardar"),command=guardar_dato)
######## boton_guardar.place(x=400, y=400)

button_modificar=Button(principal,text=("Modificar usuario"), font=("arial", 15))
button_modificar.place(x=10,y=250)

button_eliminar=Button(principal,text=("Eliminar usuario"), font=("arial", 15))
button_eliminar.place(x=10,y=300)

button_salir=Button(principal,text=("Salir"), font=("arial", 15), command=principal.destroy)
button_salir.place(x=400,y=450)


###############################################################################################################################################
def inicio():
    print("Por favor, ingresa o regístrate.")

boton = Button(principal, text= "Estudiante", command= inicio)
boton.place(x=230 , y=140)

def inicio1():
    print("Por favor digita tus credenciales.")

boton2 = Button(principal, text= "Administrativo", command= inicio1)
boton2.place(x=600 , y=140)

#######################################################################
# Contador reloj

def actualizar_hora():
    hora = time.strftime("%H:%M:%S")
    variable_control.set(hora)
    principal.after(1000, actualizar_hora)

variable_control = StringVar()

reloj = Label(textvariable= variable_control, bg="lime green", fg="white", font=("Arial", 11), padx=20, pady=20, compound="left")

reloj.pack()
reloj.place(x=900, y=1)
actualizar_hora()



# Logo app
##logo = PhotoImage(file= "logo.jpeg")
##lb_logo = Label(principal, image=logo)
##lb_logo.place(x=700, y=300)

principal.mainloop()

