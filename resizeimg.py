from tkinter import Tk, filedialog
from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size,max_dimension):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png', '.jpeg', 'JPG')):
            img_path = os.path.join(input_folder, filename)

            try:
                img = Image.open(img_path)
            except Exception as e:
                print(f"Error al abrir la imagen {filename}: {e}")
                continue

            try:
                width, height = img.size
                
                if width > max_dimension or height > max_dimension:
                    new_size = (int(width * 0.4), int(height * 0.4))
                else:
                    new_size = target_size
                
                img = img.resize(new_size, Image.LANCZOS)
            except Exception as e:
                print(f"Error al redimensionar la imagen {filename}: {e}")
                continue
            
            try:
                output_path = os.path.join(output_folder, filename)
                img.save(output_path)
            except Exception as e:
                print(f"Error al guardar la imagen {filename}: {e}")

if __name__ == "__main__":
      root = Tk()
      root.withdraw()  # Ocultar la ventana principal


      input_folder = filedialog.askdirectory(title="Selecciona la carpeta de imágenes originales")
      output_folder = filedialog.askdirectory(title="Selecciona la carpeta de salida para las imágenes redimensionadas")
      target_size = (1530, 2040)  # Tamaño final
      max_dimension = 2000 #Tamaño maximo permitido

    

if input_folder and output_folder:  # Verificar si se seleccionaron carpetas
        resize_images(input_folder, output_folder, target_size, max_dimension)
        print("Imágenes redimensionadas y guardadas en la carpeta de salida.")