# 1- Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#  Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.

numero = []
par = []
impar = []

for i in range(4):

    digito = int(input("Digite um número: "))

    numero.append(digito)

    if (digito % 2) == 0:
        par.append(digito)
    else:
        impar.append(digito)

print(numero)
print(par)
print(impar)
