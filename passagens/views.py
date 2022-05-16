from django.shortcuts import render
from passagens.forms import PassagemForm, PessoaForm

def index(request):
    form = PassagemForm()
    email = PessoaForm()
    dados = {'form':form, 'email':email}
    return render(request, 'index.html', dados)

def retorno_consulta(request):
    if request.method == 'POST':
        form = PassagemForm(request.POST)
        email = PessoaForm(request.POST)
        if form.is_valid():
            dados = {'form':form, 'email':email}
            return render(request, 'consulta.html', dados)
        else:
            dados = {'form':form, 'email':email}
            return render(request, 'index.html', dados)