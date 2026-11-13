from ultralytics import YOLO  # Importa a classe YOLO da biblioteca ultralytics

def main():  # Define a função principal do programa
    model = YOLO("yolov8n.pt")  # Carrega um modelo YOLO pré-treinado (versão leve)

    model.train(data=str(Path(__file__).parent / "arduino.yaml", epochs=150, device=0)  # Treina o modelo usando o dataset especificado por 150 epochs na GPU (device=0)
    metrics = model.val()  # Avalia o desempenho do modelo usando o conjunto de validação

if __name__ == '__main__':  # Verifica se o script está sendo executado diretamente
    main()  # Chama a função principal
