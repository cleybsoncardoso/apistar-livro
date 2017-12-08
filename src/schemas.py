from apistar import typesystem
from apistar.exceptions import TypeSystemError

class Author(typesystem.Object):
    required = ['name']
    properties = {
        'id': typesystem.Integer,
        'name': typesystem.string(min_length=1, max_length=100),
    }


class Username(typesystem.String):
    min_length = 1


class User(typesystem.Object):
    properties = {
        'username': Username,
    }
