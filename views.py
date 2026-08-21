from utils import load_data, load_template, add_data, delete_data, update_data, update_note, favorite_data


def index():
    note_template = load_template('components/notes.html')
    note_li=[
        note_template.format(
            id=dados['id'],
            title=dados['titulo'],
            details=dados['detalhes'],
            estrela=dados['estrela']
        )
    for dados in load_data()
    ]
    notes= '\n'.join(note_li)
    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    add_data(titulo,detalhes)

def delete(id):
    delete_data(id)

def update(id):
    nota= update_data(id)

    return load_template('update.html').format(
        id=nota["id"],
        titulo=nota["titulo"],
        detalhes=nota["detalhes"]
    )

def save_update(id, titulo, detalhes):
    update_note(id, titulo, detalhes)

def favorite(id):
    favorite_data(id)
