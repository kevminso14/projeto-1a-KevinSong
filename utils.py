import json

def load_data(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados

def load_template(nome_arquivo):
    caminho = 'static/templates/' + nome_arquivo
    with open(caminho, "r", encoding= "utf-8") as arquivo:
        conteudo = arquivo.read()
    return conteudo