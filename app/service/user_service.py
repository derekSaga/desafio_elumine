from app.model.user_model import UserModel
from app import db


def register_user(user_entity):
    user_db = UserModel(
        nome=user_entity.nome,
        papel=user_entity.papel,
        ativada=user_entity.ativada,
        ultimo_login=user_entity.ultimo_login,
    )

    db.session.add(user_db)
    db.session.commit()


def get_user_paper():
    users = UserModel.query.all()
    return users
