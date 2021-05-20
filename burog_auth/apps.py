from django.apps import AppConfig


class BurogAuthConfig(AppConfig):
    name = 'burog_auth'

    def ready(self):
        super(BurogAuthConfig, self).ready()
        import burog_auth.signals
