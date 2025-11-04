# Pede ao usuário que digite seu nome e armazena na variável 'nome'
nome = input("Digite seu nome: ")

# Pede ao usuário que digite sua idade e armazena na variável 'idade'
idade_str = input("Digite sua idade: ")

# Converte a string da idade para um número inteiro
idade = int(idade_str)

# Exibe uma mensagem de boas-vindas usando os dados fornecidos
print(f"Olá, {nome}! Você tem {idade} anos.")
