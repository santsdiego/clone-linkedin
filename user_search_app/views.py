from rest_framework import generics
from rest_framework import filters
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer
    filter_backends = (filters.SearchFilter,) 
    
    search_fields = ['nome']

