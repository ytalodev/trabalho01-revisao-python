# Crie uma função que
# Recebe como parâmetros Email e Senha
# Retora True se o email='admin' e senha= 'admin'


def autenticar(email, senha):
    if email == "admin" and senha == "admin":
        return True
    else:
        return False


email_digitado = input("Digite o email: ")
senha_digitado = input("Digite a senha: ")

if autenticar(email_digitado, senha_digitado):
    print("Autenticação bem-sucedida!")
else:
    print("Email ou senha incorretos.")
