from django.urls import path
from plataforma import views


urlpatterns = [
    path('', views.home, name='home'),
    path('imovel/<str:id>/', views.imovel, name="imovel"),
]
