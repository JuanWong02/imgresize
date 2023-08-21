from tkinter import Tk, filedialog, messagebox
from PIL import Image
import os

def resize_images(input_folder, output_folder, max_dimension):
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith(('.jpg', '.png', '.jpeg', 'JPG')):
                img_path = os.path.join(root, filename)
                relative_path = os.path.relpath(img_path, input_folder)
                output_path = os.path.join(output_folder, relative_path)

                try:
                    img = Image.open(img_path)
                except Exception as e:
                    error_message = f"Error al abrir la imagen {filename}: {e}"
                    messagebox.showerror("Error", error_message)
                    
                    continue

                try:
                    width, height = img.size

                    if width > max_dimension or height > max_dimension:
                        target_size = (int(width * 0.4), int(height * 0.4))
                    else: 
                        if width < 1000 or height < 1000:
                            target_size = (int(width * 4), int(height * 4))
                        else:
                            target_size = (1544, 2040)  # Default target size

                    img = img.resize(target_size, Image.LANCZOS)
                except Exception as e:
                    error_message = f"Error al redimensionar la imagen {filename}: {e}"
                    messagebox.showerror("Error", error_message)
                    continue

                try:
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    img.save(output_path)
                except Exception as e:
                    error_message = f"Error al guardar la imagen {filename}: {e}"
                    messagebox.showerror("Error", error_message)

if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal

    input_folder = filedialog.askdirectory(title="Selecciona la carpeta con múltiples carpetas de imágenes originales")
    output_folder = filedialog.askdirectory(title="Selecciona la carpeta de salida para las imágenes redimensionadas")
    max_dimension = 2000  # Specify the maximum dimension

    if input_folder and output_folder:  # Verificar si se seleccionaron carpetas
        resize_images(input_folder, output_folder, max_dimension)
        succes_message = "Imágenes redimensionadas y guardadas en la carpeta de salida."
        messagebox.showinfo("Proceso finalizado exitosamente", succes_message)
