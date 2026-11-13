import cv2
import time
from ultralytics import YOLO
from banco import salvar
from collections import defaultdict
import os

# CONFIGURAÇÕES
BASE = Path(__file__).resolve().parent
MODELO = BASE / "modelo" / "best.pt"

nomes = {
    0: "Arduino",
    1: "Protoboard",
    2: "Chave de fenda"
}

LINHA = 250

ids_salvos = set()

# Tempo mínimo entre duas detecções
TEMPO_ESPERA = 3
ultima_deteccao = 0

contador = {
    "Arduino": 0,
    "Protoboard": 0,
    "Chave de fenda": 0
}

# Guarda histórico dos objetos para rastros
rastros = defaultdict(list)

# CARREGAR MODELO

model = YOLO(MODELO)

# CÂMERA

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao abrir câmera")
    exit()

print("Sistema iniciado")

# LOOP PRINCIPAL

while True:

    ret, frame = cap.read()

    if not ret:
        break

    resultados = model.track(
        frame,
        persist=True,
        verbose=False
    )

    resultado = resultados[0]

    # Desenha linha de contagem
    cv2.line(
        frame,
        (0, LINHA),
        (frame.shape[1], LINHA),
        (0, 255, 0),
        2
    )

    if resultado.boxes is not None:

        for box in resultado.boxes:

            # Confiança
            confianca = float(box.conf[0])

            if confianca < 0.5:
                continue

            # Classe detectada
            classe = int(box.cls[0])
            nome = nomes.get(classe, "Desconhecido")

            # ID do rastreamento
            if box.id is None:
                continue

            id_objeto = int(box.id[0])

            # Coordenadas da caixa
            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            # Centro do objeto
            centro_x = int((x1 + x2) / 2)
            centro_y = int((y1 + y2) / 2)

            # Guarda rastro
            rastros[id_objeto].append(
                (centro_x, centro_y)
            )

            if len(rastros[id_objeto]) > 30:
                rastros[id_objeto].pop(0)

            # Desenha rastro
            for i in range(
                1,
                len(rastros[id_objeto])
            ):
                cv2.line(
                    frame,
                    rastros[id_objeto][i - 1],
                    rastros[id_objeto][i],
                    (255, 0, 0),
                    2
                )

            # CONTAGEM NA LINHA
            if centro_y > LINHA:

                tempo_atual = time.time()

                # Verifica:
                # 1. Se esse ID ainda não foi salvo
                # 2. Se já passaram 3 segundos desde a última detecção

                if (
                    id_objeto not in ids_salvos
                    and tempo_atual - ultima_deteccao >= TEMPO_ESPERA
                ):

                    ids_salvos.add(id_objeto)

                    # Atualiza o momento da última detecção
                    ultima_deteccao = tempo_atual

                    contador[nome] += 1

                    print(
                        f"{nome} detectado. "
                        f"ID: {id_objeto} "
                        f"Confiança: {confianca:.2f}"
                    )

                    salvar(
                        nome,
                        confianca * 100
                    )

            # Desenhar caixa
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            texto = (
                f"{nome} "
                f"{confianca:.2f}"
            )

            cv2.putText(
                frame,
                texto,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Mostrar contadores

    y = 30

    for nome_obj, quantidade in contador.items():

        cv2.putText(
            frame,
            f"{nome_obj}: {quantidade}",
            (10, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        y += 30

    cv2.imshow(
        "Sistema TCC",
        frame
    )

    # sair apertando Q

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# FINALIZAÇÃO

cap.release()
cv2.destroyAllWindows()

print("\nResultado final:")

for nome_obj, quantidade in contador.items():

    print(
        nome_obj,
        ":",
        quantidade
    )

# Gera Excel automaticamente

subprocess.run([sys.executable, str(BASE / "gerar_excel.py")], cwd=BASE)
