def destinos_iguais(origem, destino, lista_erros):
    """Verifica se os campos origem e destino são iguais."""

    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não podem ser iguais!'
    
def validacao_nome(valor_campo, nome_campo, lista_erros):
    """Valida se não há nenhum número nos campos de origem e destino."""    

    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = 'Esse campo não pode conter números!'

def validacao_data(data_ida, data_volta, lista_erros):
    """Valida se a data de ida é menor que a data de volta!"""

    if data_ida > data_volta:
        lista_erros['data_volta'] = 'A data de volta não pode ser menor que a data de ida!'

def validacao_data_pesquisa(data_ida, data_pesquisa, lista_erros):
    """Valida se a data de ida é menor que a data da pesquisa!"""

    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = 'A data de ida não pode ser menor que o dia de hoje!'