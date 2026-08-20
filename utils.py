import json
import sqlite3

def load_data():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute("select * from note")
    dados = cursor.fetchall()

    dados_formatador=[]
    for dado in dados:
        dados_formatador.append({
            "id": dado[0],
            "titulo": dado[1],
            "detalhes": dado[2]
        })

    conexao.close()
    return dados_formatador

def add_data(titulo,detalhes):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute(
    "insert into note (title, content) values(?,?)",
    (titulo,detalhes)
    )
    conexao.commit()
    conexao.close()

def delete_data(id):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('delete from note where id=?',(id,))

    conexao.commit()
    conexao.close()

def update_data(id):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('select * from note where id=?', (id,))
    dado = cursor.fetchone()
    conexao.close()
    return {
        "id": dado[0],
        "titulo": dado[1],
        "detalhes": dado[2]
    }

def update_note(id, titulo, detalhes):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('update note set title=? ,content=? where id =?',(titulo,detalhes,id))
    conexao.commit()
    conexao.close()

def load_template(nome_arquivo):
    caminho = 'static/templates/' + nome_arquivo
    with open(caminho, "r", encoding= "utf-8") as arquivo:
        conteudo = arquivo.read()
    return conteudo
