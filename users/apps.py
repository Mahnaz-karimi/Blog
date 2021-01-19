from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): # gøre at signal.py bliver klaret til at opload default billede
        import users.signals
