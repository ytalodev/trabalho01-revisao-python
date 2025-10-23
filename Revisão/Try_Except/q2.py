# Peça ao usuário para digitar um número. Use try ... except para tratar a
# exceção caso ele digite algo que não seja número (ex: texto).


def usuario_numero():
    try:
        numero = float(input("Digite um número: "))
    except ValueError:
        return "Erro: Entrada inválida. Por favor, digite um número válido."
    else:
        return f"Você digitou o número: {numero}"


mensagem = usuario_numero()
print(mensagem)
