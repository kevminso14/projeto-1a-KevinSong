from utils import load_data, load_template
import json

def index():
    note_template = load_template('components/notes.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('static/data/notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    nova_anotacao= {"titulo":titulo,
        "detalhes":detalhes}
    dados = load_data('static/data/notes.json')
    dados.append(nova_anotacao)
    with open('static/data/notes.json', "w", encoding="utf-8") as arquivo:
        json.dump(dados,arquivo)
