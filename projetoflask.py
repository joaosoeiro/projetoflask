from flask import Flask, render_template, url_for
app=Flask(__name__)

posts = [
    {
        'autor': 'João Vitor',
        'titulo': 'Primeira publicação',
        'conteudo': 'Primeiro conteúdo do post',
        'data_postagem': '25 de fevereiro de 2020'
    },
     {
        'autor': 'Joao Vitor',
        'titulo': 'Segunda publicação',
        'conteudo': 'Segundo conteúdo do post',
        'data_postagem': '26 de fevereiro de 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title = 'Home')

@app.route('/sobre')
@app.route('/about')
def sobre():
    return render_template('about.html', title = 'Sobre')
