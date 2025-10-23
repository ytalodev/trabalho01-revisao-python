# Crie uma função que receba a idade de uma pessoa e retorne: "Maior de
# idade" se for 18 anos ou mais. "Menor de idade" caso contrário.


def verificar_idade(idade):
    if idade >= 18:
        return "Você é maior de idade."
    else:
        return "Você é menor de idade."


idade_digitada = int(input("Digite sua idade: "))
resultado = verificar_idade(idade_digitada)
print(resultado)
