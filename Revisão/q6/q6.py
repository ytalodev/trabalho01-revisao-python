# 5. Crie uma função que:
# - receba peso e altura, calcule o IMC e retorne o valor. (peso/(altura**2))
# - Depois, outra função deve classificar o IMC: Abaixo de 18.5 → “Abaixo do
# peso” Entre 18.5 e 24.9 → “Peso normal” 25 ou mais → “Acima do peso”


def aplicar_imposto(preco):
    imposto = preco * 0.15
    preco_com_imposto = preco + imposto
    return preco_com_imposto


preco_digitado = float(input("Digite o preço do produto: R$ "))
preco_final = aplicar_imposto(preco_digitado)
print(f"Preço com imposto de 15%: R$ {preco_final:.2f}")
