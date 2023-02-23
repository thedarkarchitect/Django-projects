from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumer.ChatConsumer.as_asgi()),
    
]