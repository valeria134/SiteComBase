from flask import Flask, render_template, request, flash, redirect, url_for
from formulario import CadastroForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user
 
app = Flask (__name__)
app.config['SECRET_KEY'] = 'dkshvfdikhgolfhvljh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MeuSite.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(12), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)
  
@property
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cadastro', methods=["GET", "POST"])
def Cadastro():
    formulario=CadastroForm()
    if formulario.validate_on_submit():
        usuario = formulario.usuario.data
        email = formulario.email.data
        password = formulario.password.data

        user = User (usuario=usuario, email=email, password=password)
        db.session.add(user)
        db.session.commit()

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