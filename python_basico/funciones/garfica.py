import tkinter as tk

# Creamos una ventana principal
ventana = tk.Tk()
ventana.title('Mi primera ventana con Tkinter')
ventana.geometry("400x300")  # Ancho x Alto en píxeles

# Creamos un label (como en etapa 1 en Formularios ¿lo recordás?)
etiqueta = tk.Label(ventana, text='¡Hola, mundo!', font=('Arial', 20))
etiqueta.pack()

# Iniciamos el bucle principal de nuestra aplicación
ventana.mainloop()
