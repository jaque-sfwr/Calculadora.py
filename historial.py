import tkinter as tk
from tkinter import messagebox

#Variable global 
historial_texto = ""

def registrar_operacion(operacion, resultado):
    """Suma una nueva operación al historial en memoria."""
    global historial_texto
    historial_texto = historial_texto + f"{operacion} = {resultado}\n"

def mostrar_historial(encendido):
    """Muestra la ventana emergente con el historial acumulado."""
    if not encendido:
        return
        
    if historial_texto == "":
        messagebox.showinfo("Historial", "No hay operaciones todavia.")
    else:
        messagebox.showinfo("Historial", historial_texto)