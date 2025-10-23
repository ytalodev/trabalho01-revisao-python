# Crie uma função chamada dividir(a, b) que: Retorne o resultado de a / b Use
# try...except para evitar erro de divisão por zero Retorne uma mensagem de
# erro se isso acontecer


def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
    else:
        return f"O resultado da divisão é: {resultado}"


valor_a = float(input("Digite o valor de a: "))
valor_b = float(input("Digite o valor de b: "))
mensagem = dividir(valor_a, valor_b)
print(mensagem)
