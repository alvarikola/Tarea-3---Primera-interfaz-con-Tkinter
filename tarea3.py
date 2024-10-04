import os
import random
import tkinter as tk
from PIL import Image, ImageTk




root = tk.Tk()
root.title("Tarea 3")

directorioImagenes = os.listdir('hiragana') # C:\Users\root\OneDrive\Imágenes\hiragana\hiragana  /// /home/alumno/Imágenes/hiragana/
print(directorioImagenes)
imagenesSeleccionadas = random.sample(directorioImagenes, 10)
print(imagenesSeleccionadas)
puntos = 0
indiceActual = 0


respuesta = tk.Entry(root)
respuesta.pack()


labelImagen = tk.Label(root)
labelImagen.pack()


def mostrarImagen():
    global indiceActual
    imagenActual = imagenesSeleccionadas[indiceActual]
    imagenPath = os.path.join('hiragana', imagenActual)
    img = Image.open(imagenPath)
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    labelImagen.config(image=img_tk)
    labelImagen.image = img_tk


def comprobarTraduccion():
    global indiceActual, puntos
    correcto = imagenesSeleccionadas[indiceActual].split('.')
    print(correcto)
    traduccionUsuario = respuesta.get()

    if traduccionUsuario == correcto[0]:
        puntos += 1

    indiceActual += 1

    if indiceActual < len(imagenesSeleccionadas):
        mostrarImagen()
    else:
        root.destroy()
        resultados = tk.Tk()
        resultados.title("Resultados")

        if puntos < 5:
            mensaje = f"Suspenso: {puntos}/10"
            rutaImagen = 'memes/suspenso.jpg'
            imagen = Image.open(rutaImagen)
            imagen = imagen.resize((300, 300))
            imagen_tk = ImageTk.PhotoImage(imagen)
            label_imagen = tk.Label(resultados, image=imagen_tk)
            label_imagen.pack(padx=20, pady=20)
        elif puntos == 5:
            mensaje = f"Suficiente: {puntos}/10"
            ruta_imagen = 'memes/suficiente.jpg'
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((300, 300))
            imagen_tk = ImageTk.PhotoImage(imagen)
            label_imagen = tk.Label(resultados, image=imagen_tk)
            label_imagen.pack(padx=20, pady=20)
        elif puntos == 6:
            mensaje = f"Bien: {puntos}/10"
            ruta_imagen = 'memes/bien.jpg'
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((300, 300))
            imagen_tk = ImageTk.PhotoImage(imagen)
            label_imagen = tk.Label(resultados, image=imagen_tk)
            label_imagen.pack(padx=20, pady=20)
        elif puntos in [7, 8]:
            mensaje = f"Notable: {puntos}/10"
            ruta_imagen = 'memes/notable.jpg'
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((300, 300))
            imagen_tk = ImageTk.PhotoImage(imagen)
            label_imagen = tk.Label(resultados, image=imagen_tk)
            label_imagen.pack(padx=20, pady=20)
        else:
            mensaje = f"Sobresaliente: {puntos}/10"
            ruta_imagen = 'memes/sobresaliente.jpg'
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((300, 300))
            imagen_tk = ImageTk.PhotoImage(imagen)
            label_imagen = tk.Label(resultados, image=imagen_tk)
            label_imagen.pack(padx=20, pady=20)

        label_resultado = tk.Label(resultados, text=mensaje, font=("Arial", 16))
        label_resultado.pack(padx=20, pady=20)


        resultados.mainloop()


botonComprobar = tk.Button(root, text="Comprobar", command=comprobarTraduccion)
botonComprobar.pack()

mostrarImagen()


root.mainloop()




