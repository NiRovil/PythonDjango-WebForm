from django.shortcuts import render
from passagens.forms import PassagemForm

def index(request):
    form = PassagemForm()
    dados = {'form':form}
    return render(request, 'index.html', dados)

def retorno_consulta(request):
    if request.method == 'POST':
        form = PassagemForm(request.POST)
        dados = {'form':form}
        return render(request, 'consulta.html', dados)