import datetime


class UserEntity:
    def __init__(self, nome, papel, ativada, ultimo_login):
        self.__nome = nome
        self.__papel = papel
        self.__ativada = ativada
        self.__ultimo_login = ultimo_login

    def __dict__(self):
        return {
            "nome": self.__nome,
            "papel": self.__papel,
            "ativada": self.__ativada,
            "ultimo_login": self.__ultimo_login,
        }

    def format_date(self):
        if self.__ultimo_login != "":
            self.__ultimo_login = datetime.datetime.strptime(
                self.__ultimo_login, "%d/%m/%Y %H:%M"
            ).strftime("%d/%m/%Y %H:%M")
        else:
            self.__ultimo_login = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def papel(self):
        return self.__papel

    @papel.setter
    def papel(self, papel):
        self.__papel = papel

    @property
    def ativada(self):
        return self.__ativada

    @ativada.setter
    def ativada(self, ativada):
        self.__ativada = ativada

    @property
    def ultimo_login(self):
        return self.__ultimo_login

    @ultimo_login.setter
    def ultimo_login(self, ultimo_login):
        self.__ultimo_login = ultimo_login