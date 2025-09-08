from rich_pixels import Pixels
from PIL import Image
import os


def resize(caminho, tamanho):
    size = tamanho, tamanho

    if not os.path.exists(caminho):
        print(f"Imagem não encontrada: {caminho}")
        return False

    try:
        im = Image.open(caminho)
        im.thumbnail(size, Image.Resampling.LANCZOS)
        novo_caminho = f"{caminho.split('.')[0]}copia.{caminho.split('.')[1]}"
        if os.path.exists(novo_caminho):
            os.remove(novo_caminho)
        im.save(novo_caminho)
    except ValueError:
        print(caminho)
        print(novo_caminho)
        return False, novo_caminho
    return True, novo_caminho


def gerar_pixel(caminho, tamanho):
    bool, novo_caminho = resize(caminho, tamanho)
    if bool:
        try:
            pixels = Pixels.from_image_path(novo_caminho)
            if os.path.exists(novo_caminho):
                os.remove(novo_caminho)
            return pixels
        except Exception:
            print(f"Erro ao gerar pixels")
            return None
    return None
