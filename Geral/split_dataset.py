import os  # Importa funções para manipulação de arquivos e diretórios
import random  # Importa funções para operações aleatórias
import shutil  # Importa funções para mover/copiar arquivos

source_dir = r"D:\Programação\TCC\datasets\arduino\train1"  # Define o diretório de origem onde estão imagens e labels

train_dir = r"D:\Programação\TCC\datasets\arduino\train"  # Define o diretório de destino para treino
val_dir = r"D:\Programação\TCC\datasets\arduino\val"  # Define o diretório de destino para validação

os.makedirs(train_dir, exist_ok=True)  # Cria a pasta de treino caso não exista
os.makedirs(val_dir, exist_ok=True)  # Cria a pasta de validação caso não exista

files = os.listdir(source_dir)  # Lista todos os arquivos do diretório de origem

images = [f for f in files if f.endswith((".jpg", ".png", ".jpeg"))]  # Filtra apenas arquivos de imagem

random.shuffle(images)  # Embaralha a lista de imagens aleatoriamente

split = int(len(images) * 0.7)  # Calcula o índice de divisão para 70% treino e 30% validação

train_images = images[:split]  # Seleciona as imagens para treino
val_images = images[split:]  # Seleciona as imagens para validação

for img in train_images:  # Percorre cada imagem de treino

    label = os.path.splitext(img)[0] + ".txt"  # Gera o nome do arquivo de label correspondente

    shutil.move(os.path.join(source_dir, img), os.path.join(train_dir, img))  # Move a imagem para a pasta de treino

    label_path = os.path.join(source_dir, label)  # Define o caminho do arquivo de label
    if os.path.exists(label_path):  # Verifica se o arquivo de label existe
        shutil.move(label_path, os.path.join(train_dir, label))  # Move o label para a pasta de treino

for img in val_images:  # Percorre cada imagem de validação

    label = os.path.splitext(img)[0] + ".txt"  # Gera o nome do arquivo de label correspondente

    shutil.move(os.path.join(source_dir, img), os.path.join(val_dir, img))  # Move a imagem para a pasta de validação

    label_path = os.path.join(source_dir, label)  # Define o caminho do arquivo de label
    if os.path.exists(label_path):  # Verifica se o arquivo de label existe
        shutil.move(label_path, os.path.join(val_dir, label))  # Move o label para a pasta de validação

print("Divisão concluída")  # Exibe mensagem indicando que a divisão foi finalizada