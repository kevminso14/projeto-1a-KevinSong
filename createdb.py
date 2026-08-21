import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS note (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    favorite INTEGER NOT NULL DEFAULT 0
)
""")


conexao.commit()
conexao.close()
