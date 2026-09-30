import sqlite3
from datetime import datetime

con = sqlite3.connect("deteccoes.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS deteccoes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    objeto TEXT,
    confianca REAL,
    horario TEXT
)
""")

con.commit()
con.close()


def salvar(objeto, confianca):
    con = sqlite3.connect("deteccoes.db")
    cursor = con.cursor()

    cursor.execute("""
    INSERT INTO deteccoes(objeto, confianca, horario)
    VALUES(?,?,?)
    """, (
        objeto,
        confianca,
        datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    ))

    con.commit()
    con.close()