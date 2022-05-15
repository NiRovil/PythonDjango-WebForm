from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.validation import *

tipos_passagem = {(1, 'Ecônomica'), (2, 'Executiva'), (3, 'Primeira classe')}

class PassagemForm(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today)
    classe_voo = forms.ChoiceField(label='Classe do Vôo', choices=tipos_passagem)
    informacoes = forms.CharField(label='Informações extras', max_length=200,widget=forms.Textarea(), required=False)
    email = forms.EmailField(label='Email', max_length=100)

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_erros = {}
        destinos_iguais(origem, destino, lista_erros)
        validacao_nome(origem, 'origem', lista_erros)
        validacao_nome(destino, 'destino', lista_erros)
        validacao_data_pesquisa(data_ida, data_pesquisa, lista_erros)
        validacao_data(data_ida, data_volta, lista_erros)
        if lista_erros is not None:
            for erro in lista_erros:
                mensagem = lista_erros[erro]
                self.add_error(erro, mensagem)
        return self.cleaned_data    