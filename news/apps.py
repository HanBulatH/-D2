# from news.signals import * не работает рассылка писем через сигналс, делала все как в примере
from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    # def ready(self):
    #     import news.signals