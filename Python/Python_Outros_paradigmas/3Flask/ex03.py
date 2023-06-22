"""
Exercício 3:
    - Exiba a mensagem: 'Olá, programadores!' no endereço raiz de uma página web e apareça a mensagem: 'Entre com dois números'
    - Exiba a mensagem: '0.0' no endereço '/somar/'
    _ Exiba a mensagem: '30.0' no endereço '/somar/10/20' de uma página web.
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    mensagem = '<h1>Olá, programadores</h1>'
    instrucao = '<p>Entre com dois números na URL da página após adicionar o /somar</p>'
    exemplo = '<p>Exemplo: /somar/primeiroNúmero/segundoNúmero</p>'
    return mensagem + instrucao + exemplo

@app.route('/somar/')
@app.route('/somar/<num1>/<num2>')
def soma(num1=0, num2=0):
    resultado = float(num1) + float(num2) # transformando os dados inseridos em float para poder fazer a soma
    mensagem = f'<h1>A soma de {num1} + {num2} = {resultado}</h1>'
    informacao = '<p>Para testar outro resultado, mude os respectivos valores na URL.</p>'
    return mensagem + informacao

if __name__ == '__main__':
    app.run(debug=True)
