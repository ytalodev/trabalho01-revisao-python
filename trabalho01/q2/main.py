# Q2 - Conversor de Temperatura
# Conversão entre Celsius e Fahrenheit
# Obrigração: criar um arquivo conversor.py e importar as funções
from conversor import celsius_para_fahrenheit, fahrenheit_para_celsius


print("Conversor de Temperatura")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

opcao = input("Escolha uma opção (1 ou 2): ")

if opcao == "1":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
