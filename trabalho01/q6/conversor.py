def real_para_dolar(valor_real, cotacao_dolar):

    if cotacao_dolar <= 0:
        raise ValueError("A cotação do Dólar deve ser maior que zero.")

    valor_dolar = valor_real / cotacao_dolar
    return valor_dolar


def dolar_para_real(valor_dolar, cotacao_dolar):
    if cotacao_dolar <= 0:
        raise ValueError("A cotação do Dólar deve ser maior que zero.")

    valor_real = valor_dolar * cotacao_dolar
    return valor_real
