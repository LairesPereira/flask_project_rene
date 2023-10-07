from flask import *
from datetime import *

app = Flask(__name__)

nome = 'Laires'

usuarios = []

@app.route('/receberNome', methods=['POST'])
def receberNome():
    nome = str(request.form.get('user'))
    cargo = str(request.form.get('userCargo'))
    senha = str(request.form.get('userPassword'))

    usuarios.append(nome)

    listao = ''

    for user in usuarios:
        listao = listao + '\n' + user

    msg = 'senha nao pode ser igual ao nome'
    if(senha == nome): 
        return render_template('index.html', dev=nome, mensagem=msg)
    
    print(listao)
    return render_template('sucesso.html', lista=listao)


@app.route('/')
def home_page():
    return render_template('index.html', dev=nome)


@app.route('/hora')
def horas():
    data = datetime.now()
    ano = data.year
    mes = data.month
    dia = data.day
    hora = data.hour
    minutos = data.minute
    return f'Hoje, a data é {dia}-{mes}-{ano} e agora é {hora}:{minutos}'

if __name__ == '__main__':
    app.run(debug=True)