from typing import Tuple, Union

from flask import Flask, request


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        _name = "name"
        database = dict()

        @app.route("/user", methods=["POST"])
        def create_user() -> Tuple[dict, int]:
            body = request.json

            if _name not in body.keys():
                return {"errors": {"name": "This field is required"}}, 422

            name = body[_name]
            database[name] = {"age": 27}

            return {"data": f"User {name} is created!"}, 201

        @app.route("/user/<name>")
        def read_user(name: str) -> Tuple[dict, int]:
            if name not in database.keys():
                return {"errors": {"name": f"User {name} not found"}}, 404

            return {"data": f"My name is {name}"}, 200

        @app.route("/user/<name>", methods=["PATCH"])
        def update_user(name: str) -> Tuple[dict, int]:
            if name not in database.keys():
                return {"errors": {"name": f"User {name} not found"}}, 404

            body = request.json

            if _name not in body.keys():
                return {"errors": {"name": "This field is required"}}, 422

            new_name = body[_name]
            data = database.pop(name)
            database[new_name] = data

            return {"data": f"My name is {new_name}"}, 200

        @app.route("/user/<name>", methods=["DELETE"])
        def delete_user(name: str) -> Tuple[Union[str, dict], int]:
            if name not in database.keys():
                return {"errors": {"name": f"User {name} not found"}}, 404

            _ = database.pop(name)
            return "", 204
