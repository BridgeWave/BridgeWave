from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def pagina_inicial():
 return render_template('index.html')

@app.route('/cursos')
def pagina_cursos():
 return render_template('cursos.html')

@app.route('/noticias')
def pagina_noticias():
 return render_template('noticias.html')

@app.route('/professor')
def pagina_professor():
 return render_template('professor.html')

@app.route('/quem_somos')
def pagina_quem():
 return render_template('quem_somos.html')

if __name__ == '__main__':
 app.run(debug=True, port=5001)