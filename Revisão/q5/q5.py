# Crie uma função que:
# - receba peso e altura, calcule o IMC e retorne o valor. (peso/(altura**2))
# - Depois, outra função deve classificar o IMC: Abaixo de 18.5 → “Abaixo do
# peso” Entre 18.5 e 24.9 → “Peso normal” 25 ou mais → “Acima do peso”


def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    else:
        return "Acima do peso"


peso_digitada = float(input("Digite seu peso em kg: "))
altura_digitada = float(input("Digite sua altura em metros: "))
imc_calculado = calcular_imc(peso_digitada, altura_digitada)
classificacao = classificar_imc(imc_calculado)
print(f"Seu IMC é: {imc_calculado:.2f}")
print(f"Classificação: {classificacao}")
