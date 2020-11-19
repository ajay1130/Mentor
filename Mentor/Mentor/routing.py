from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

# from channels.routing import ProtocolTypeRouter,URLRouter
# from django.urls import path
# from chat.consumers import EchoConsumer

# application = ProtocolTypeRouter({
#     'websocket':URLRouter([
#         path('ws/chat/',EchoConsumer)
#     ])
# })