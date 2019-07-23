from django.shortcuts import render

# Create your views here.

def pagina_inicial(request):
    context = {"nome": "eric", 'cachorros': ['Tobias', 'Totó', 'blas', 'kdjks', 'lsklask']}

    return render(request, 'index.html', context)