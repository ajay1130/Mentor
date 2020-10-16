from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter
import HOME.routing

application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            HOME.routing.websocket_urlpatterns
        )
    ),
})