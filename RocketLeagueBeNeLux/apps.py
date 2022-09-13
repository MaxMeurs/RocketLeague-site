from django.apps import AppConfig


class RocketleaguebeneluxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RocketLeagueBeNeLux'

    def ready(self):
        import RocketLeagueBeNeLux.signals