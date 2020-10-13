from app import db


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    papel = db.Column(db.String)
    ativada = db.Column(db.Boolean, nullable=False)
    ultimo_login = db.Column(db.TIMESTAMP, nullable=True)
