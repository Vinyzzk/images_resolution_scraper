import os
from PIL import Image


def get_image_resolution(image_path):
    try:
        with Image.open(image_path) as img:
            return img.size  # Retorna uma tupla (largura, altura)
    except Exception as e:
        print(f"Não foi possível abrir a imagem {image_path}: {e}")
        return None


def scan_images_in_directory(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                image_path = os.path.join(dirpath, file)
                resolution = get_image_resolution(image_path)
                if resolution:
                    print(f"Imagem: {image_path}, Resolução: {resolution[0]}x{resolution[1]} pixels")



root_directory = 'images'
scan_images_in_directory(root_directory)
