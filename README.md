# Calculadora.py
Proyecto Final: Calculadora Básica
Este programa consiste en una calculadora de escritorio interactiva que realiza las operaciones aritméticas básicas (suma, resta, multiplicación y división). Cuenta con un diseño visual estilizado en tonos pastel y fue desarrollado utilizando la librería estándar Tkinter de Python. El proyecto cumple con un enfoque de programación estructurada y modular.

Estructura del Código
Para cumplir con la organización modular, el código se dividió en cuatro archivos independientes. Cada uno tiene una tarea específica dentro del sistema:

main.py: Es el archivo principal y el punto de inicio del programa. Su única función es coordinar el arranque llamando a la configuración de la interfaz.

interfaz.py: En este archivo se encuentra toda la capa visual. Aquí se configura el tamaño de la ventana, la caja donde se ven los números y la lista de botones con sus respectivos colores y funciones de control.

historial.py: Es el encargado de gestionar la memoria del programa. Cada vez que se realiza una operación matemática con éxito, se almacena en este módulo para poder mostrar las operaciones pasadas.

persistencia.py: Es un archivo informativo dentro del código que detalla las características técnicas de la gestión y el almacenamiento de los datos en este programa.

Persistencia de Datos
En este proyecto se optó por utilizar una persistencia de datos volátil, lo que significa que el historial de operaciones se guarda directamente en la memoria RAM del equipo mientras el programa está abierto.

Las ventajas de este enfoque son:

El programa es sumamente ligero, limpio y rápido al ejecutarse.

No genera archivos basura adicionales en la computadora del usuario.

No requiere permisos especiales del sistema operativo para escribir o borrar archivos en el disco duro, evitando posibles errores de ejecución.

Al ser una memoria temporal de sesión, el historial se mantiene activo mientras se usa la calculadora y se libera automáticamente al cerrar la ventana.

Preguntas de la Entrega
¿Qué partes del código implementaste tú?
Implementé la lógica completa de las operaciones matemáticas apoyándome en la función nativa eval() de Python y estructuré el diseño por filas utilizando contenedores individuales para que los botones se alinearan correctamente de forma manual. También configuré la lógica del botón ON/OFF para alternar los estados físicos de la pantalla gráfica y diseñé la acumulación del historial mediante saltos de línea para que las operaciones se muestren de forma ordenada en la ventana emergente (messagebox).

¿Qué aprendiste durante el desarrollo?
Durante este proyecto aprendí la importancia de la modularización, ya que separar el código en archivos diferentes facilita mucho la detección de errores y hace que el desarrollo sea más limpio. También reforcé el uso de variables de control de Tkinter (como StringVar) para conectar la pantalla con las funciones, y comprendí la diferencia entre la persistencia temporal en memoria RAM y el almacenamiento permanente, lo cual es fundamental al diseñar software.
