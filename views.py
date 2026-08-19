from utils import load_data, load_template, add_data, delete_data
import json

def index():
    note_template = load_template('components/notes.html')
    note_li=[
        note_template.format(
            id=dados['id'],
            title=dados['titulo'],
            details=dados['detalhes']
        )
    for dados in load_data()
    ]
    notes= '\n'.join(note_li)
    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    add_data(titulo,detalhes)

def delete(id):
    delete_data(id)