#MÓDULO DE PERSISTENCIA DE DATOS

#Este proyecto utiliza Persistencia Volátil (en Memoria RAM).
#Los datos del historial se mantienen activos únicamente mientras 
#la aplicación esté en ejecución. Al cerrar la ventana, la memoria 
#se libera y el historial se reinicia.

#Este enfoque se seleccionó para mantener el código ligero y rápido

def obtener_tipo_persistencia():
    return "Volátil (RAM)"