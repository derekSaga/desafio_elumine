from uuid import uuid4

DEBUG = True
USER = "postgres"
SENHA = "Byn^7$Wd*"
HOST = "localhost"
PORT = 5432
SCHEMA = "desafio_elumini"
SQLALCHEMY_DATABASE_URI = f"postgres://{USER}:{SENHA}@{HOST}/{SCHEMA}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SECRET_KEY = str(uuid4())
PROPAGATE_EXCEPTIONS = True
