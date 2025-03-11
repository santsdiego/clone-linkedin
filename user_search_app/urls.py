from django.urls import path
from .views import UsuarioListView  # Importa a view


urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),  # Define a URL para listar os usuários
]
