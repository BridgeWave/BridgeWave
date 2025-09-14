from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<pagina>')
def api_pagina(pagina):
    conteudos = {
        "home": "<h2>Bem-vindo à BridgeWave!</h2><p>Sua plataforma de cursos preferida...</p>",
        "cursos": "<h2>Cursos Disponíveis</h2><div class='curso'>Curso 1</div><div class='curso'>Curso 2</div><div class='curso'>Curso 3</div>",
        "noticias": "<h2>Notícias</h2><p>Últimas novidades do mundo BridgeWave...</p>",
        "professor": "<h2>Seja Professor</h2><p>Cadastre-se e ensine conosco!</p>",
        "quem_somos": "<h2>Quem Somos</h2><p>Conheça Eduardo e Guilherme</p>"
    }
    return jsonify({"html": conteudos.get(pagina, "<p>Página não encontrada</p>")})

if __name__ == "__main__":
    app.run(debug=True, port=5001)