from PIL import Image
import os

pasta = r"D:\seu_dataset"

for raiz, dirs, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if arquivo.lower().endswith((".jpg", ".jpeg")):
            caminho = os.path.join(raiz, arquivo)

            try:
                img = Image.open(caminho)
                img.verify()

            except Exception as e:
                print(f"Imagem corrompida: {caminho}")
                print(e)