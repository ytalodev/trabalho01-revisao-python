# Crie um código que possa gerar dois tipos de erro diferentes (ex: ValueError
# e ZeroDivisionError) e trate cada um de forma separada.


def calculadora_divisao():
    try:
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))
        resultado = numerador / denominador

    except ValueError:
        print("Entrada inválida. Você precisa digitar um número valido.")
    except ZeroDivisionError:
        print("Não é possível dividir um número por zero.")

    else:
        print(f"\nO resultado da divisão é: {resultado}")


calculadora_divisao()
