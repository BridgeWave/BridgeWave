from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-segura'

@app.route('/formulario', methods = ['GET', 'POST'])
def formulario():

    if request.method == 'POST':

        nome = request.form.get('nome')
        email = request.form.get('email')

        print(f"Os dados recebidos no formulario: Nome={nome}, Email={email}")

        flash(f"Obrigado por se cadastrar, {nome}!")

        return redirect(url_for('formulario'))
    
    return render_template('formulario.html')