from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

# Criando um roteador e registrando a ViewSet
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)  # Registra a rota "/usuarios/"

urlpatterns = [
    path('', include(router.urls)),  # Inclui todas as rotas registradas no router
]
