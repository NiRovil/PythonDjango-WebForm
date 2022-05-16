from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.validation import *
from passagens.models import Passagem, Pessoa


tipos_passagem = {(1, 'Ecônomica'), (2, 'Executiva'), (3, 'Primeira classe')}

class PassagemForm(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today)
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {'data_ida':'Data de ida', 'data_volta': 'Data de volta','classe_viagem':'Classe da viagem', 'informacoes':'Informações extras'}
        widgets = {'data_ida':DatePicker(), 'data_volta':DatePicker()}
    
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

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['email']