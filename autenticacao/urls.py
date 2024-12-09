from django.urls import path
from autenticacao import views


urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar')
]
