import tkinter as tk
from tkinter import messagebox

#Variables globales
encendido= True
historial_texto= ""

#Funcion cuando se presiona un botón 
def click(boton):
    if not encendido:
        return
        
    if pantalla_var.get() == "Error":
        pantalla_var.set(boton)
    else:
        pantalla_var.set(pantalla_var.get() + boton)

#Funcion para borrar la pantalla
def borrar():
    if not encendido:
        return
    pantalla_var.set("")

#Funcion para calcular el resultado
def calcular():
    global historial_texto
    if not encendido:
        return
        
    operacion = pantalla_var.get()
    if operacion:
        try:
            resultado = str(eval(operacion))
            
            #Guardar en la variable de historial
            historial_texto = historial_texto + f"{operacion} = {resultado}\n"
            
            pantalla_var.set(resultado)
        except:
            pantalla_var.set("Error")

#Funcion para mostrar el historial en una ventanita
def mostrar_historial():
    if not encendido:
        return
        
    if historial_texto == "":
        messagebox.showinfo("Historial", "No hay operaciones todavia.")
    else:
        messagebox.showinfo("Historial", historial_texto)

#Funcion para prender y apagar
def toggle_encendido():
    global encendido
    encendido = not encendido
    
    if encendido:
        pantalla_var.set("")
        btn_on_off.config(text="OFF", bg="#FFB7B2")
    else:
        pantalla_var.set("")
        btn_on_off.config(text="ON", bg="#B5EAD7")

#Para la interfaz grafica
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("320x460")
ventana.configure(bg="#F9F6F0")
ventana.resizable(False, False)

pantalla_var = tk.StringVar()

#Caja de texto de la pantalla
pantalla = tk.Entry(ventana, textvariable=pantalla_var, font=("Helvetica", 28), 
                    bg="#FFFFFF", fg="#4a4a4a", justify="right", bd=0)
pantalla.pack(fill="x", pady=20, padx=15, ipady=10)

#Contenedor principal de botones
frame_botones = tk.Frame(ventana, bg="#F9F6F0")
frame_botones.pack()

fila1 = tk.Frame(frame_botones, bg="#F9F6F0")
fila1.pack(side="top", fill="x")

tk.Button(fila1, text="7", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click("7")).pack(side="left", padx=5, pady=5)
tk.Button(fila1, text="8", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click("8")).pack(side="left", padx=5, pady=5)
tk.Button(fila1, text="9", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click("9")).pack(side="left", padx=5, pady=5)
tk.Button(fila1, text="/", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#FFDAC1", fg="#4a4a4a", command=lambda: click("/")).pack(side="left", padx=5, pady=5)

fila2 = tk.Frame(frame_botones, bg="#F9F6F0")
fila2.pack(side="top", fill="x")

tk.Button(fila2, text="4", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click("4")).pack(side="left", padx=5, pady=5)
tk.Button(fila2, text="5", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click("5")).pack(side="left", padx=5, pady=5)
tk.Button(fila2, text="6", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click("6")).pack(side="left", padx=5, pady=5)
tk.Button(fila2, text="*", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#FFDAC1", fg="#4a4a4a", command=lambda: click("*")).pack(side="left", padx=5, pady=5)

fila3 = tk.Frame(frame_botones, bg="#F9F6F0")
fila3.pack(side="top", fill="x")

tk.Button(fila3, text="1", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click("1")).pack(side="left", padx=5, pady=5)
tk.Button(fila3, text="2", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click("2")).pack(side="left", padx=5, pady=5)
tk.Button(fila3, text="3", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click("3")).pack(side="left", padx=5, pady=5)
tk.Button(fila3, text="-", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#FFDAC1", fg="#4a4a4a", command=lambda: click("-")).pack(side="left", padx=5, pady=5)

fila4 = tk.Frame(frame_botones, bg="#F9F6F0")
fila4.pack(side="top", fill="x")

tk.Button(fila4, text="0", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click("0")).pack(side="left", padx=5, pady=5)
tk.Button(fila4, text=".", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(".")).pack(side="left", padx=5, pady=5)
tk.Button(fila4, text="=", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#FFDAC1", fg="#4a4a4a", command=calcular).pack(side="left", padx=5, pady=5)
tk.Button(fila4, text="+", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#FFDAC1", fg="#4a4a4a", command=lambda: click("+")).pack(side="left", padx=5, pady=5)

#Fila de controles. (C, OFF, HISTORIAL
frame_control = tk.Frame(ventana, bg="#F9F6F0")
frame_control.pack(pady=15)

btn_clear = tk.Button(frame_control, text="C", font=("Helvetica", 14, "bold"), width=5, height=1, bd=0, bg="#FFF1E6", fg="#4a4a4a", command=borrar)
btn_clear.pack(side="left", padx=5)

btn_on_off = tk.Button(frame_control, text="OFF", font=("Helvetica", 14, "bold"), width=5, height=1, bd=0, bg="#FFB7B2", fg="#4a4a4a", command=toggle_encendido)
btn_on_off.pack(side="left", padx=5)

btn_historial = tk.Button(frame_control, text="Hist", font=("Helvetica", 14, "bold"), width=5, height=1, bd=0, bg="#B2CEFE", fg="#4a4a4a", command=mostrar_historial)
btn_historial.pack(side="left", padx=5)

ventana.mainloop()