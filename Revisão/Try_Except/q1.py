# Peça ao usuário dois números e mostre o resultado da divisão. Use try ...
# except para tratar o caso em que o usuário digite zero no divisor.


def dividir_numeros(dividendo, divisor):
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
    else:
        return f"O resultado da divisão é: {resultado}"


num1 = float(input("Digite o dividendo: "))
num2 = float(input("Digite o divisor: "))
mensagem = dividir_numeros(num1, num2)
print(mensagem)
