from django.core.serializers import serialize
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer
    filter_backends = (filters.SearchFilter,) 

    search_fields = ['nome']  # Permite busca apenas pelo campo 'nome'


class UsuarioUpdateView(generics.UpdateAPIView): #Testar depois o RetrieveUpdateAPIView se funciona...
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'pk'


