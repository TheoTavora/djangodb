from django.shortcuts import render
from appmodelo.models import Cliente
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
 

def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'appmodelo/index.html', {'cliente':clientes})


  
    if request.method == 'POST':
        name = request.POST.get('name')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')




