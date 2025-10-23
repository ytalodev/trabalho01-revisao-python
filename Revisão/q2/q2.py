# Crie uma função que recebe o preõ do produto e aplica um desconto de 10%
# (retorna o valor com o desconto)


def aplicar_desconto(preco):
    desconto = preco * 0.10
    preco_com_desconto = preco - desconto
    return preco_com_desconto


preco_digitado = float(input("Digite o preço do produto: R$ "))
preco_final = aplicar_desconto(preco_digitado)

print(f"Preço com desconto de 10%: R$ {preco_final:.2f}")
