from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email,EqualTo

class CadastroForm(FlaskForm):
    name= StringField("Nome Completo", validators= [DataRequired()])
    email= StringField("Email", validators= [DataRequired(),Email()])
    senha= PasswordField("Senha",[DataRequired(),EqualTo('confirm',message='Senhas diferentes')])
    confirm= PasswordField('Repita a senha')
    botao=SubmitField('Enviar')
 


class LoginForm(FlaskForm):
    email= StringField("Email", validators= [DataRequired(),Email()])
    senha= PasswordField("Senha",[DataRequired(),EqualTo('confirm',message='Senhas diferentes')])
    botao=SubmitField('Enviar')

