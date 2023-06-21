"""
Exercício 1:
    - Exiba a mensagem: 'Página principal' no endereço raiz de uma página web.
    - Exiba a mensagem: 'Olá, mundo!' no endereço: '/ola/' de uma página web.
    - Exiba a mensagem: 'Olá, usuário!' no endereço: '/ola/nome_do_usuário' de uma página web.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Página principal'

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola(nome='mundo'):
    return f'Olá, {nome}!'

if __name__ == '__main__':
    app.run()
