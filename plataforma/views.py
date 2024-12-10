from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from plataforma.models import Imovel


@login_required(login_url='logar')
def home(request):
    imoveis = Imovel.objects.all()

    context = {
        'imoveis': imoveis
    }
    
    return render(request, 'home.html', context)
