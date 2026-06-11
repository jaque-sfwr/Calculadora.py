import tkinter as tk

#Variable global para saber si la calculadora esta encendida
encendido= True

#Para cambiar el estado de la calculadora entre encendido y apagado
def toggle_encendido():
    global encendido
    encendido= not encendido
    
    #Cambio de color y texto para el boton on y off según el estado de la calculadora.
    if encendido:
        pantalla_var.set("")
        btn_on_off.config(text="OFF", bg="#FFB7B2", activebackground="#FF9AA2") 
    else:
        pantalla_var.set("")
        btn_on_off.config(text="ON", bg="#B5EAD7", activebackground="#9CE0C7")  


def click(boton):
    global encendido
    
    #Si esta apagada no hace nada
    if not encendido: 
        return 

    #Boton para mostrar el resultado
    if boton == "=":
        try:
            #eval() para hacer la operación automaticamente
            resultado= str(eval(pantalla_var.get()))
            pantalla_var.set(resultado)
            
        #En el caso de dividir entre cero
        except ZeroDivisionError:
            pantalla_var.set("Error")
         #Para otro tipo de errores   
        except Exception:
            pantalla_var.set("Error")
    elif boton == "C":
        pantalla_var.set("") 
    else:
        pantalla_var.set(pantalla_var.get() + boton)

#Configuracion de la venatana
ventana= tk.Tk()
ventana.title("Calculadora")
ventana.geometry("320x450")
ventana.configure(bg="#F9F6F0")
ventana.resizable(False, False)

#Variable para manejar el texto de la ventana
pantalla_var = tk.StringVar()

#Crea una caja de texto
pantalla = tk.Entry(ventana, textvariable=pantalla_var, font=("Helvetica", 28), 
                    bg="#FFFFFF", fg="#4a4a4a", justify="right", bd=0)
pantalla.pack(fill="x", pady=20, padx=15, ipady=10)

#Contenedor de botones
frame_botones = tk.Frame(ventana, bg="#F9F6F0")
frame_botones.pack()

#Lista de los botones de la calculadora
botones = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

#Crea la configuracion de los botones
for fila in botones:
    frame_fila = tk.Frame(frame_botones, bg="#F9F6F0")
    frame_fila.pack(side="top", fill="x")
    for boton in fila:
        #Para definir los distintos colores de los botones
        if boton not in ["/", "*", "-", "+", "="]:
            color_fondo = "#E8DFF5" 
            color_activo = "#D3C5E5"
        else:
            color_fondo = "#FFDAC1" 
            color_activo = "#FFCBA4"
        
        tk.Button(frame_fila, text=boton, font=("Helvetica", 16, "bold"), width=5, height=2, 
                  bd=0, bg=color_fondo, fg="#4a4a4a", activebackground=color_activo, activeforeground="#4a4a4a",
                  command=lambda b=boton: click(b)).pack(side="left", padx=5, pady=5)

#Contenedor para los botones de control(C y on/off)
frame_control= tk.Frame(ventana, bg="#F9F6F0")
frame_control.pack(pady=15)

#Boton para borrar
btn_clear = tk.Button(frame_control, text="C", font=("Helvetica", 14, "bold"), width=6, height=1, 
                      bd=0, bg="#FFF1E6", fg="#4a4a4a", activebackground="#FDE0C7", activeforeground="#4a4a4a",
                      command=lambda: click("C"))
btn_clear.pack(side="left", padx=10)

#Boton para encender y apagar
btn_on_off = tk.Button(frame_control, text="OFF", font=("Helvetica", 14, "bold"), width=6, height=1, 
                       bd=0, bg="#FFB7B2", fg="#4a4a4a", activebackground="#FF9AA2", activeforeground="#4a4a4a", 
                       command=toggle_encendido)
btn_on_off.pack(side="left", padx=10)

#Inicio del programa
ventana.mainloop()