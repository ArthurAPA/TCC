import sqlite3
import pandas as pd

con = sqlite3.connect("deteccoes.db")
df = pd.read_sql(
    "SELECT * FROM deteccoes",
    con
)
# Formata a confiança com 2 casas decimais
df["confianca"] = df["confianca"].apply(
    lambda x: f"{x:.2f}%"
)

# Organiza as colunas com espaços entre elas
relatorio = pd.DataFrame()
relatorio["ID"] = df["id"]
relatorio[""] = ""
relatorio["Objeto"] = df["objeto"]
relatorio[" "] = ""
relatorio["Confiança"] = df["confianca"]
relatorio["  "] = ""
relatorio["Horário"] = df["horario"]

# Salva o Excel
relatorio.to_excel(
    "Relatorio.xlsx",
    index=False
)

con.close()
print("Relatório atualizado com sucesso!")