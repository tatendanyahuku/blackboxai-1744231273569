from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/video-call/(?P<room_id>[^/]+)/$', consumers.VideoCallConsumer.as_asgi()),
]
