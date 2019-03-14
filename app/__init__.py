# Importando as bibliotecas
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager


# Variavel contendo o flask
app = Flask(__name__)
# configuração do bd para o flask partindo de uma página especifica de config
app.config.from_object('config')

# Variavel contenco o SQL alchemy
db = SQLAlchemy(app)

# Variavel contenco o # flask_migrate, "cuida das migrações"
migrate = Migrate(app, db)

# Variavel contenco o flask_script, "Comandos para inicialisar a aplicação"
manager = Manager(app)

# passando o comando para migrar
manager.add_command('db', MigrateCommand)

# Intanciando o login manager
lm = LoginManager(app)

# Importando as tabelas
from app.models import tables, forms

# Importando as demais informações do default
from app.controllers import default
