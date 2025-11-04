# -*- coding: utf-8 -*-

# programa: multiplicador interativo
import os

while True:
    # solicita os dois numero ao usuário
    os.system("cls")
    numero1 = float(input("digite o primeiro numero: "))
    numero2 = float(input("digite o segundo numero:"))

    #calcule a multiplicação
    resultado = numero1 * numero2

    # exibe o resultado
    print(f"\no resultado da multiplicação de {numero1} x {numero2} é = {resultado}\n")

    # pergunta se o usuario deseja continuar
    continuar = input("deseja fazer outro calculo (s/n)").strip.lower()
   
    # se o usuario digitar 'n' , o programa encerra
    if continuar != 's':
        print("\nprograma encerrado. até logo!")
        break

print("-" * 40)  #separador visual