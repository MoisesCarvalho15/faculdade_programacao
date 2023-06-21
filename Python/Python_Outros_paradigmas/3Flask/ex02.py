"""
Exercício 2: 
    - Exiba a mensagem: 'Olá, programadores!', no endereço raiz de uma página web e apareça o link '/user/Usuário'
    - Exiba a mensagem: 'Olá, Usuário!', no endereço 'user/' e exiba a mensagem: 'Altere o nome no endereço do browser e recarregue a página'
    - Exiba a mensagem: 'Olá, nome_usuário!', no endereço '/user/nome_do_usuário' de uma página web.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    boas_vindas = '<h1>Olá, programadores!</h1>'
    link = '<p><a href="user/Usuário">Clique Aqui</a></p>'
    return boas_vindas + link

@app.route('/user/')
@app.route('/user/<nome>')
def user(nome='Usuário'):
    personalizar = f'<h1>Olá, {nome}</h1>'
    instrucao = '<p>Altere o nome no endereço do browser e recarregue a página.</p>'
    return personalizar + instrucao

if __name__ == '__main__':
    app.run(debug=True)
    