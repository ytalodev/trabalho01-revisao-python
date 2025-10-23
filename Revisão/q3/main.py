# Seu sistema deverá ser composto por 2 arquivos (main.py e
# funcoes_bolsa.py)
# a. Em funcoes_bolsa deverá existir uma função que verifique se o valor recebido nesta é > que
# 150.99. Caso positivo retorne: “Ação está cara! Compre com cuidado.”. Caso negativo: “Ação
# está barata!”
# b. No main.py permita que o usuário digite o valor da ação e envie para função que você criou
# para validar se está cara ou barata


from funcoes_bolsa import verificar_valor_acao

valor_acao_digitada = float(input("Digite o valor da ação: R$ "))
resultado = verificar_valor_acao(valor_acao_digitada)
print(resultado)
