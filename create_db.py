import sqlite3
conn = sqlite3.connect('banco_dados.db')
print("Banco de dados 'banco_dados.db' criado com sucesso!")

conn.close()