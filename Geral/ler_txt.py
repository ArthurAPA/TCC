import os

# Caminho da pasta onde estão as labels
labels_path = DATASET / "train"

# Contadores de imagens por classe
contagem = {
    0: 0,  # Arduino
    1: 0,  # Protoboard
    2: 0   # Chave de fenda
}

# Percorre todos os arquivos
for arquivo in os.listdir(labels_path):
    if arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(labels_path, arquivo)

        classes_na_imagem = set()  # evita contar repetido na mesma imagem

        with open(caminho_arquivo, "r") as f:
            for linha in f:
                classe = int(linha.split()[0])
                classes_na_imagem.add(classe)

        # Conta 1 vez por imagem
        for classe in classes_na_imagem:
            if classe in contagem:
                contagem[classe] += 1

# Resultado
print("Quantidade de imagens por classe:")
print(f"Arduino (0): {contagem[0]}")
print(f"Protoboard (1): {contagem[1]}")
print(f"Chave de fenda (2): {contagem[2]}")
