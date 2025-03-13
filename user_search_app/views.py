from django.core.serializers import serialize
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()  # Pega todos os usuários
    serializer_class = UsuarioSerializer
    filter_backends = (filters.SearchFilter,)  # Habilita a filtragem
    
    search_fields = ['nome']  # Permite busca apenas pelo campo 'nome'


class UsuarioUpdateView(generics.RetrieveUpdateAPIView): #Testar depois o UpdateAPIView se funciona...
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'pk'


