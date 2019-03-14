# importando a biblioteca para utilização do sistema operacional
import os.path
basedir = os.path.abspath(os.path.dirname(__file__))
# configuração de debug
DEBUG = True


# Configuração do SQL alchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# configuração da secret_key do formulario
SECRET_KEY = 'crip-to-gra-fa-do'