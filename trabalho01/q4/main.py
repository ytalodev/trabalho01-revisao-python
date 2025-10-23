# Questão 4 - Verificador de Números Pares e Ímpares
# Crie uma função que receba um número inteiro e retorne se ele é par ou ímpar.


def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


numero_digitado = int(input("Digite um número inteiro: "))
resultado = verificar_par_ou_impar(numero_digitado)
print(f"O número {numero_digitado} é {resultado}.")
