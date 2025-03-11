from rest_framework import generics
from rest_framework import filters
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()  # Pega todos os usuários
    serializer_class = UsuarioSerializer
    filter_backends = (filters.SearchFilter,)  # Habilita a filtragem
    
    search_fields = ['nome']  # Permite busca apenas pelo campo 'nome'
