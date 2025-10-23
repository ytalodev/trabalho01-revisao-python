# Questão 1 - Manipulação de listas e strings


def contar_palavras(frase, palavra):
    frase_minuscula = frase.lower()
    palavra_minuscula = palavra.lower()
    palavras_frase = frase_minuscula.split()
    quantidade = 0
    for p in palavras_frase:
        if p == palavra_minuscula:
            quantidade += 1
    return quantidade


frase_digitada = input("Digite uma frase: ")
palavra_digitada = input("Digite uma palavra para buscar: ")

quantidade_encontrada = contar_palavras(frase_digitada, palavra_digitada)

# Quantidade de Palavras
print(f"A palavra '{palavra_digitada}' aparece {quantidade_encontrada} vez(es).")
