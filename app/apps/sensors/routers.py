from django.urls import path
from .consumers import MQTTConsumer

websocket_urlpatterns = [
    path('mqtt/sensor/<str:topic>/', MQTTConsumer.as_asgi()),
]