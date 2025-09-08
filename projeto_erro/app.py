from flask import Flask, render_template, abort

app = Flask(__name__)

#Rota pricncipal

@app.route("/")

def index():

    return render_template("index.html")

#Para demonstrar o erro 401, vamos criar uma rota que exige login

@app.route("/area-restrita")

def area_restrita():
    print("Tentativa de acesso à área restrita sem autenticação")

    abort(401)

#para demonstrar 403

@app.route("/painel-admin")

def painel_admin():

    #aqui, você verificaria se o usuário logado é um administrador

    #vamos simular que o usuário não é admin e forçar o erro 403

    print("Tentativa de acesso ao painel de administrador sem permissão")
    abort(403)

    #-- Manipuladores de Erro (erro handlers)--

@app.errorhandler(404)

def pagina_nao_encontrada(error):

    #A função recebe o objeto de erro como argumento

    #Retornamos a renerização do nosso template e o código de status 4.

    return render_template("404.html"), 404

@app.errorhandler(401)
def nao_autorizado(error):
    return render_template("401"), 401

@app.errorhandler(403)
def nao_autorizado(error):
    return render_template("4013"), 403


if __name__ == '__main__':
    app.run(debug=True)