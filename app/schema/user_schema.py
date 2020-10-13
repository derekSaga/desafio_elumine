from app import ma
from app.model.user_model import UserModel
from marshmallow import fields, pre_dump


def partition(items, key, container_name):
    return [
        {
            key: index,
            container_name: [
                item for item in items if item.__getattribute__(key) == index
            ],
        }
        for index in set([item.__getattribute__(key) for item in items])
    ]


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel

    id = fields.Integer(dump_only=True)
    nome = fields.String(required=True)
    papel = fields.String(required=False, default="")
    ativada = fields.Boolean(required=True)
    ultimo_login = fields.DateTime(format="%d/%m/%Y %H:%M", allow_none=True)


class UserCategory(ma.Schema):
    user_list = fields.Nested(UserSchema, many=True)

    class Meta:
        fields = ("papel", "user_list")

    @pre_dump(pass_many=True)
    def partition_categories(self, data, many):
        return partition(data, "papel", "user_list")
