from app.schema.user_schema import UserSchema
from app.entity.user_entity import UserEntity
from app.service.user_service import register_user
from flask_restful import Resource
from flask import request, make_response, jsonify
from app import api
from app.service import upload_service
import numpy as np

ALLOWED_EXTENSIONS = {"txt", "csv", "xlsx"}
ALLOWED_SEP = {",", "|", ";", "\t"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


class Upload(Resource):
    def post(self):
        try:
            if "file" not in request.files:
                msg = "No file part"
                return make_response(jsonify({"msg": msg}), 400)

            file = request.files["file"]

            if file.filename == "":
                msg = "No selected file"
                return make_response(jsonify({"msg": msg}), 400)
            if file and allowed_file((file.filename)):
                msg = "upload complete"

                usecols = request.args.get("usecols", None)
                skiprows = int(request.args.get("skiprows", 0))
                sep = request.args.get("sep", ",")

                df = upload_service.load_file_df(file, sep, usecols, skiprows)

                df = df.replace(np.nan, "")

                df["Ativada"] = df["Ativada"].replace(1, True)
                df = df.loc[
                    (df["Nome completo"] != "Total")
                    & (df["Nome completo"] != "")
                    & (df["Ativada"] != "")
                ]

                for iter in df.to_dict(orient="records"):
                    user_entity = UserEntity(
                        iter["Nome completo"],
                        iter["Papel"],
                        iter["Ativada"],
                        iter["Último login"],
                    )

                    user_entity.format_date()

                    try:
                        us = UserSchema()

                        validate = us.validate(user_entity.__dict__())
                        print(user_entity.__dict__())
                        if validate:
                            return make_response(jsonify(validate), 400)

                        register_user(user_entity)
                    except Exception as e:
                        print(e)

                return make_response(jsonify({"msg": msg}), 200)
        except Exception as e:
            return make_response(jsonify({"msg": "internal error", "error": e}), 500)


api.add_resource(Upload, "/v1/upload")
