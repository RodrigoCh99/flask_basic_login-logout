# Importando as funções especifcas flask para formularios
from flask_wtf import FlaskForm
# importando as diferenças em formularios como as bolinhas na senha e o check binario
from wtforms import StringField, PasswordField, BooleanField
# validadores para o formulario conferir se estão preenchidos os campos
from wtforms.validators import DataRequired


# Classe Formulario!
class LoginForm(FlaskForm):


    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")