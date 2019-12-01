from flask import Flask, render_template
from formulario import CadastroForm, LoginForm

 
app = Flask (__name__)
app.config['SECRET_KEY'] = 'dkshvfdikhgolfhvljh'
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cadastro', methods=["GET", "POST"])
def Cadastro():
    formulario=CadastroForm()
    return render_template(
        'cadastro.html',
        formulario=formulario
        )


@app.route('/login', methods=["GET", "POST"])
def Login():
    formulario=LoginForm()
    return render_template(
        'login.html',
         formulario=formulario
         )    
@app.route('/materiais', methods=["GET", "POST"])
def Materiais():
    return render_template('materiais.html')
@app.route('/assunto', methods=["GET", "POST"])
def Assunto():
    return render_template('assunto.html')
          

if (__name__ =='__main__'):
    app.run(debug=True, port = 5001)