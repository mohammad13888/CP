import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import djangochat

import djangochat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(djangochat.routing.websocket_urlpatterns)
    )
})
