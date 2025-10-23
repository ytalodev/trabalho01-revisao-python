# Questão 3: Sistema de autenticação simples
# Usuários e senhas pré-definidos. Criar uma função para autenticar.

usuarios = {"admin": "1234", "joao": "senha123", "maria": "abc@2024"}


def autenticar(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    else:
        return False


usuario_digitado = input("Digite o nome de usuário: ")
senha_digitada = input("Digite a senha: ")

if autenticar(usuario_digitado, senha_digitada):
    print("Autenticação bem-sucedida!")
else:
    print("Falha na autenticação. Usuário ou senha incorretos.")
