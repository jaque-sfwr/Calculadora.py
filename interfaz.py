import tkinter as tk
import historial  

#Variables de control
encendido = True

def click(pantalla_var, boton):
    if not encendido:
        return
    if pantalla_var.get() == "Error":
        pantalla_var.set(boton)
    else:
        pantalla_var.set(pantalla_var.get() + boton)

def borrar(pantalla_var):
    if not encendido:
        return
    pantalla_var.set("")

def calcular(pantalla_var):
    if not encendido:
        return
    operacion = pantalla_var.get()
    if operacion:
        try:
            resultado = str(eval(operacion))
            #Aqui se registra la operación usando el módulo 'historial'
            historial.registrar_operacion(operacion, resultado)
            pantalla_var.set(resultado)
        except:
            pantalla_var.set("Error")

def toggle_encendido(pantalla_var, btn_on_off):
    global encendido
    encendido = not encendido
    if encendido:
        pantalla_var.set("")
        btn_on_off.config(text="OFF", bg="#FFB7B2")
    else:
        pantalla_var.set("")
        btn_on_off.config(text="ON", bg="#B5EAD7")

def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Calculadora")
    ventana.geometry("320x460")
    ventana.configure(bg="#F9F6F0")
    ventana.resizable(False, False)

    pantalla_var = tk.StringVar()

    pantalla = tk.Entry(ventana, textvariable=pantalla_var, font=("Helvetica", 28), 
                        bg="#FFFFFF", fg="#4a4a4a", justify="right", bd=0)
    pantalla.pack(fill="x", pady=20, padx=15, ipady=10)

    frame_botones = tk.Frame(ventana, bg="#F9F6F0")
    frame_botones.pack()

    fila1 = tk.Frame(frame_botones, bg="#F9F6F0")
    fila1.pack(side="top", fill="x")
    tk.Button(fila1, text="7", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(pantalla_var, "7")).pack(side="left", padx=5, pady=5)
    tk.Button(fila1, text="8", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(pantalla_var, "8")).pack(side="left", padx=5, pady=5)
    tk.Button(fila1, text="9", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(pantalla_var, "9")).pack(side="left", padx=5, pady=5)
    tk.Button(fila1, text="/", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#FFDAC1", fg="#4a4a4a", command=lambda: click(pantalla_var, "/")).pack(side="left", padx=5, pady=5)

    fila2 = tk.Frame(frame_botones, bg="#F9F6F0")
    fila2.pack(side="top", fill="x")
    tk.Button(fila2, text="4", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(pantalla_var, "4")).pack(side="left", padx=5, pady=5)
    tk.Button(fila2, text="5", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(pantalla_var, "5")).pack(side="left", padx=5, pady=5)
    tk.Button(fila2, text="6", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(pantalla_var, "6")).pack(side="left", padx=5, pady=5)
    tk.Button(fila2, text="*", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#FFDAC1", fg="#4a4a4a", command=lambda: click(pantalla_var, "*")).pack(side="left", padx=5, pady=5)

    fila3 = tk.Frame(frame_botones, bg="#F9F6F0")
    fila3.pack(side="top", fill="x")
    tk.Button(fila3, text="1", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(pantalla_var, "1")).pack(side="left", padx=5, pady=5)
    tk.Button(fila3, text="2", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(pantalla_var, "2")).pack(side="left", padx=5, pady=5)
    tk.Button(fila3, text="3", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(pantalla_var, "3")).pack(side="left", padx=5, pady=5)
    tk.Button(fila3, text="-", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#FFDAC1", fg="#4a4a4a", command=lambda: click(pantalla_var, "-")).pack(side="left", padx=5, pady=5)

    fila4 = tk.Frame(frame_botones, bg="#F9F6F0")
    fila4.pack(side="top", fill="x")
    tk.Button(fila4, text="0", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(pantalla_var, "0")).pack(side="left", padx=5, pady=5)
    tk.Button(fila4, text=".", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#E8DFF5", fg="#4a4a4a", command=lambda: click(pantalla_var, ".")).pack(side="left", padx=5, pady=5)
    tk.Button(fila4, text="=", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#FFDAC1", fg="#4a4a4a", command=lambda: calcular(pantalla_var)).pack(side="left", padx=5, pady=5)
    tk.Button(fila4, text="+", font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, bg="#FFDAC1", fg="#4a4a4a", command=lambda: click(pantalla_var, "+")).pack(side="left", padx=5, pady=5)

    frame_control = tk.Frame(ventana, bg="#F9F6F0")
    frame_control.pack(pady=15)

    btn_clear = tk.Button(frame_control, text="C", font=("Helvetica", 14, "bold"), width=5, height=1, bd=0, bg="#FFF1E6", fg="#4a4a4a", command=lambda: borrar(pantalla_var))
    btn_clear.pack(side="left", padx=5)

    btn_on_off = tk.Button(frame_control, text="OFF", font=("Helvetica", 14, "bold"), width=5, height=1, bd=0, bg="#FFB7B2", fg="#4a4a4a")
    btn_on_off.config(command=lambda: toggle_encendido(pantalla_var, btn_on_off))
    btn_on_off.pack(side="left", padx=5)

    btn_historial = tk.Button(frame_control, text="Hist", font=("Helvetica", 14, "bold"), width=5, height=1, bd=0, bg="#B2CEFE", fg="#4a4a4a", command=lambda: historial.mostrar_historial(encendido))
    btn_historial.pack(side="left", padx=5)

    ventana.mainloop()