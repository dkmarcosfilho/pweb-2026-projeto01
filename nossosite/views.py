from django.shortcuts import render

def index(request):
    return render(request, 'nossosite/index.html')

def elenco(request):
    return render(request, 'nossosite/elenco.html')

def sobre(request):
    return render(request, 'nossosite/sobre.html')
