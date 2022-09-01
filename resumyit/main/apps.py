from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'resumyit.main'
    
    def ready(self):
        import resumyit.main.signals
