from django.shortcuts import render


def radiocomunicacao(request):
    return render(request, 'radiocomunicacao.html')
    
def mapa(request):
    return render(request, 'mapa.html')
