from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('meu_app.urls')),  # Isso inclui as rotas do `meu_app`
]
