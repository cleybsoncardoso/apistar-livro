from apistar.backends.django_orm import Session
from apistar import http
from src import schemas
from django.conf import settings
from django.contrib.auth import authenticate

class Author(object):

    @staticmethod
    def store(session: Session, author: schemas.Author):
        new_author = session.Author(**author)
        new_author.save()
        return returnDefault(schemas.Author(new_author.__dict__))

    @staticmethod
    def all(session: Session):
        authors = session.Author.objects.all()
        return returnDefault([schemas.Author(authors_current.__dict__) for authors_current in authors])

    @staticmethod
    def get(session: Session, id: int):
        author = session.Author.objects.get(pk=id)
        return returnDefault(schemas.Author(author.__dict__))

    @staticmethod
    def update(session: Session, author: schemas.Author, id: int):
        author_update = session.Author.objects.filter(pk=id)
        author_update.update(**author)
        return returnDefault([schemas.Author(authors_current.__dict__) for authors_current in author_update])

    @staticmethod
    def delete(session: Session, id: int):
        author_delete = session.Author.objects.get(pk=id)
        session.Author.objects.filter(pk=id).delete()
        return returnDefault(schemas.Author(author_delete.__dict__))


class User(object):
    @staticmethod
    def store(user: schemas.User, session: Session):
        if not user:
            return
        new_user = session.User.objects.create_user(**user)
        return returnDefault(schemas.User(new_user.__dict__))

    @staticmethod
    def all(user: schemas.User, session: Session):
        users = session.User.objects.all()
        return returnDefault([schemas.User(user_current.__dict__) for user_current in users])

    @staticmethod
    def login(user: schemas.User, session: Session):
        user = authenticate(username='cleyrerere', password='123')
        if user is not None:
            return returnDefault(schemas.User(user.__dict__))
            # A backend authenticated the credentials
        else:
            return ("erro")


def returnDefault(data, mensagem = None):
    return http.Response(content=dict(success=True, data=data), status=200)
