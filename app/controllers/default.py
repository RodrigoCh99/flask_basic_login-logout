# Importando o render do flask
from flask import render_template, flash, redirect, url_for
# Importando o login do flask
from flask_login import login_user, logout_user
# Importando app da pasta app
from app import app, db, lm

# Importando tabelas
from app.models.tables import User
# Importando o formulario da pasta forms
from app.models.forms import LoginForm

# decorator relacionado ao flask_login
@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

# rota para index
@app.route("/index")
# rota padrão de Inicialização "/"
@app.route("/")
def index():
    # A função render_template roda o arquivo nformado desde que este esteja na pasta templates
    return render_template('index.html')

# rota para a pagina de login:
@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Loged in.")
            return redirect(url_for("index"))

        else:
            flash('Invalid Login')
    return render_template('login.html', form=form)

# rota para a pagina de logout
@app.route("/logout")
def logout():
    logout_user()
    flash("logged Out.")
    return redirect(url_for('index'))
