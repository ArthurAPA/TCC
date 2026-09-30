import sqlite3
import os


# Conecta ao banco
con = sqlite3.connect("deteccoes.db")

cursor = con.cursor()


# Apaga todas as detecções salvas
cursor.execute(
    "DELETE FROM deteccoes"
)


# Reinicia o contador do ID
cursor.execute(
    "DELETE FROM sqlite_sequence WHERE name='deteccoes'"
)


con.commit()
con.close()


# Remove o relatório antigo
if os.path.exists("Relatorio.xlsx"):
    os.remove("Relatorio.xlsx")


print("Relatório apagado com sucesso!")