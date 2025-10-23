# Q6 - Conversor de Moedas
# Crie a função que converte reais para dólares e dólares para reais (arquivo conversor.py)
# real_para_dolar e dolar_para_real. Caso o usuário não passe o tipo (real_para_dolar ou dolar_para_real) o default deve ser real_para_dolar <- padrão
# Nome do arquivo: main.py

import conversor

print("Conversor de Moedas")
print("1. Reais para Dólares")
print("2. Dólares para Reais")

entrada = input("Escolha uma opção [Padrão: 1]: ")

if entrada == "":
    opcao = 1
else:
    opcao = int(entrada)

if opcao == 1:
    valor = float(input("Digite o valor em Reais (R$): "))
    cotacao = float(input("Digite a cotação do Dólar (ex: 5.20): "))

    resultado = conversor.real_para_dolar(valor, cotacao)

    print("\n--- Resultado ---")
    print(f"R$ {valor:.2f} equivalem a US$ {resultado:.2f}")

elif opcao == 2:
    valor = float(input("Digite o valor em Dólares (US$): "))
    cotacao = float(input("Digite a cotação do Dólar (ex: 5.20): "))

    resultado = conversor.dolar_para_real(valor, cotacao)

    print("\n--- Resultado ---")
    print(f"US$ {valor:.2f} equivalem a R$ {resultado:.2f}")

else:
    print("Opção inválida. Escolha 1 ou 2.")
