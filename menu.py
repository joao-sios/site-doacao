import math

# --- Funções para as opções do menu ---

def entrada_e_saida():
    """Demonstra entrada e saída de dados."""
    print("\n--- Entrada e Saída de Dados ---")
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}!")
    idade = input("Digite sua idade: ")
    print(f"Sua idade é: {idade}")

def decisao():
    """Demonstra estrutura de decisão (if/else)."""
    print("\n--- Estrutura de Decisão ---")
    try:
        numero = int(input("Digite um número: "))
        if numero > 0:
            print("O número é positivo.")
        elif numero < 0:
            print("O número é negativo.")
        else:
            print("O número é zero.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

def funcoes_matematicas():
    """Demonstra o uso de funções matemáticas."""
    print("\n--- Funções Matemáticas ---")
    try:
        numero = float(input("Digite um número para ver sua raiz quadrada: "))
        if numero >= 0:
            raiz_quadrada = math.sqrt(numero)
            print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}.")
        else:
            print("Não é possível calcular a raiz quadrada de um número negativo.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

def repeticao_while():
    """Demonstra a estrutura de repetição while."""
    print("\n--- Repetição com 'while' ---")
    contador = 1
    while contador <= 5:
        print(f"Contagem: {contador}")
        contador += 1
    print("Contagem finalizada.")

def repeticao_for():
    """Demonstra a estrutura de repetição for."""
    print("\n--- Repetição com 'for' ---")
    print("Iterando sobre uma lista:")
    frutas = ["Maçã", "Banana", "Laranja"]
    for fruta in frutas:
        print(f"- {fruta}")

def acao_mundo_exemplo():
    """Exemplo de uma ação que interage com dados externos (simulado)."""
    print("\n--- Ação 'Mundo' (Exemplo) ---")
    print("Simulando uma ação que busca dados de um 'mundo'...")
    dados = {
        "cidade": "Votorantim",
        "temperatura": "25°C",
        "status": "Ensolarado"
    }
    print("Dados obtidos:")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")

# --- Menu principal ---

def mostrar_menu():
    """Exibe o menu de opções."""
    print("\n============================")
    print("  MENU DE OPÇÕES EM PYTHON")
    print("============================")
    print("1. Entrada e Saída de Dados")
    print("2. Decisão (if/elif/else)")
    print("3. Funções Matemáticas")
    print("4. Repetição com 'while'")
    print("5. Repetição com 'for'")
    print("6. Ação 'Mundo' (Exemplo)")
    print("0. Sair")
    print("----------------------------")

def main():
    """Função principal que executa o loop do menu."""
    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                entrada_e_saida()
            elif opcao == 2:
                decisao()
            elif opcao == 3:
                funcoes_matematicas()
            elif opcao == 4:
                repeticao_while()
            elif opcao == 5:
                repeticao_for()
            elif opcao == 6:
                acao_mundo_exemplo()
            elif opcao == 0:
                print("Saindo do programa. Até mais!")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

if __name__ == "__main__":
    main()
