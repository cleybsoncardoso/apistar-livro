from src.routes import routes
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.backends import django_orm

settings = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    },
    'INSTALLED_APPS': ['src', 'django.contrib.contenttypes', 'django.contrib.auth'  ],
    'JWT': {
        'SECRET': 'jwt-secret',
        'USERNAME': 'username',
        'ID': 'user'
    }
}


app = App(routes=routes,
          settings=settings,
          commands=django_orm.commands,  # Install custom commands.
          components=django_orm.components  # Install custom components.
          )


if __name__ == '__main__':
    app.main()
