#-*- coding: utf-8 -*-
import os
import math
import random


# função para calcular a raiz quadrada
def raiz_quadrada():
    numero = float(input("digite um nùmero para calcular a raiz quadrada: "))
    if numero < 0:
        print("não é possivel calcular a a raiz quadrada de número negativo")
    else:
        resultado = math.sqrt(numero)
        print(f"a raiz quadrada de {numero} é {resultado}")
    input("pressione qualquer tecla para continuar...")
    

    # função para calcular a potência
def potencia():
        base = float(input("digiite o expoente: "))
        expoente = float(input("digite o expoente: "))
        resultado = math.pow(base, expoente)
        print(f"{base} elevado a {expoente} é igual a {resultado}")
        input("pressione qualquer tecla para continuar...")

        # função para gerar um numero randômico
def numero_aleatório():
            inicio = int(input("digite o valor inicial do intervalo: "))
            if inicio > fim:
                print("o valor inicial deve ser menor ou igual ao valor final! ")
            else:
                numero = random.randint(inicio, fim)
                print(f"numero aleatório gerado entre {inicio} e {fim}: {numero}")
                input("pressione qualquer troca para continuar...")

                # programa principal com menu
def main():

    while True:
        os.system("cls")
        print("\n=== menu de operações ===")
        print("1 - raiz quadrada")
        print("2 - potencia")
        print("3 - numero randômico")
        print("4 - sair")

        opcao = input("escolha uma opção: ")

        if opcao== '1':
            raiz_quadrada()
        elif opcao== '2': #elseif opcao == '2':
            potencia()   
        elif opcao== '3':
            numero_aleatorio() 
        elif opcao== '4':
            print("saindo do programa... até logo!")
            break
        else:
            print("opção inválida! tente novamente.")

        # execute o programa
if __name__ == "__main__":
        main()
