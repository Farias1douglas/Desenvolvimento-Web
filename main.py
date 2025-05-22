from flask import Flask, render_template, request
app = Flask(__name__)
idade = 2
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/primeiro')
def primeiro():
    return render_template('primeiro.html')

@app.route('/segundo')
def segundo():
    return render_template('segundo.html')

@app.route('/terceiro')
def terceiro():
    return render_template('terceiro.html')

@app.route('/quarto')
def quarto():
    return render_template('quarto.html')
#Abaixo teste de formulario#
@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['GET'])
def recebedados():
    nome = request.args.get("nome")
    email = request.args.get("email")
    return "{} - {}".format(nome, email)
#Abaixo ser teste de Condicionais#
@app.route('/Verificador/<int:idade>')
def verificador(idade):
    return "você tem" + idade +"de idade."

if __name__ == '__main__':
    app.run(debug=True)