from django.apps import AppConfig


class DatasetsConfig(AppConfig):
    name = 'apps.datasets'

    def ready(self):
        import apps.datasets.signals
