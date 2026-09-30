import os  # Importa funções para manipulação de arquivos e diretórios

pasta = r"D:\Programação\TCC\datasets\arduino\train1"  # Define o caminho da pasta onde estão as imagens

for arquivo in os.listdir(pasta):  # Percorre todos os arquivos dentro da pasta
    if arquivo.endswith((".jpg",".png",".jpeg")):  # Verifica se o arquivo é uma imagem
        nome = os.path.splitext(arquivo)[0]  # Extrai o nome do arquivo sem a extensão
        label = os.path.join(pasta, nome + ".txt")  # Cria o caminho para o arquivo de label correspondente

        if not os.path.exists(label):  # Verifica se o arquivo de label não existe
            open(label, "w").close()  # Cria um arquivo .txt vazio

print("labels vazios criados")  # Exibe mensagem indicando que os labels foram criados