from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def open_image(img_path):
    try:
        img = Image.open(img_path)
        return img
    except Exception as e:
        error_message = f"Error al abrir la imagen {os.path.basename(img_path)}:\n{e}"
        messagebox.showerror("Error", error_message)
        return None

def resize_and_save_image(img, output_path, target_size):
    try:
        img_resized = img.resize(target_size, Image.LANCZOS)
        img_resized.save(output_path)
    except Exception as e:
        error_message = f"Error al redimensionar o guardar la imagen {os.path.basename(output_path)}:\n{e}"
        messagebox.showerror("Error", error_message)

def resize_images(input_path, output_folder, max_dimension):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if os.path.isdir(input_path):
        # Process images in the directory
        for filename in os.listdir(input_path):
            if filename.endswith(('.jpg', '.png', '.jpeg', 'JPG')):
                img_path = os.path.join(input_path, filename)
                img = open_image(img_path)
                if img:
                    width, height = img.size
                    cuadrado = width - height <= abs(300)
                    if cuadrado:
                        if width > max_dimension or height > max_dimension:
                            target_size = (int(width * 0.4), int(height * 0.4))
                   
                        if width < 1000 or height < 1000:
                            target_size = (int(width * 4), int(height * 4))
                        
                        else: 
                            target_size = (width,height)
                    else:
                        target_size = (1530,2040)
                    output_path = os.path.join(output_folder, filename)
                    resize_and_save_image(img, output_path, target_size)
    elif os.path.isfile(input_path):
        # Process a specific image file
        img = open_image(input_path)
        if img:
            width, height = img.size
            cuadrado = width - height <= abs(300)
            if cuadrado:
                        if width > max_dimension or height > max_dimension:
                            target_size = (int(width * 0.4), int(height * 0.4))
                   
                        if width < 1000 or height < 1000:
                            target_size = (int(width * 4), int(height * 4))
                        
                        else: 
                            target_size = (width,height)
            else:
                 target_size = (1530,2040)
            output_path = os.path.join(output_folder, os.path.basename(input_path))
            resize_and_save_image(img, output_path, target_size)
    else:
        messagebox.showerror("Error", "La ruta seleccionada no es válida.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    input_path = filedialog.askopenfilename(title="Selecciona una imagen o una carpeta")
    output_folder = filedialog.askdirectory(title="Selecciona la carpeta de salida para las imágenes redimensionadas")
    max_dimension = 600

    if input_path and output_folder:
        resize_images(input_path, output_folder, max_dimension)
        success_message = "Proceso completado."
        messagebox.showinfo("Proceso completado", success_message)
