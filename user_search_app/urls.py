from django.urls import path
from .views import UsuarioListView  # Importa a view
from .views import UsuarioUpdateView


urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),  # Define a URL para listar os usuários
    path('usuarios/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario-update') # Define a URL para atualizar os usuários
]
