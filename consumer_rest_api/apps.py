from django.apps import AppConfig
from . import receiver
from apscheduler.schedulers.background import BackgroundScheduler

class ConsumerServiceApisConfig(AppConfig):
    name = 'consumer_rest_api'
    def ready(self):
        # receiver.on_message_receive()
