# 4-Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
import math
vetorA = []

def LerNumeros():
    for i in range(10):
        vetorA.append(int(input(f"{i+1} -Digite um numero:")))

def ObterQuadrados(vetor):
    vetorQuadrados = []
    for numero in vetor:
        vetorQuadrados.append(math.pow(numero,2))
    return vetorQuadrados

def SomarValores(vetor):
    soma = 0
    for num in vetor:
        soma += int(num)
    return soma

def MontarRerposta(vetor):
    quadrados = ObterQuadrados(vetor)
    soma = SomarValores(quadrados)

    return f"O vetor lido foi {vetor} \n O quadrado de seus valores sao: {quadrados} \n A soma de seus quadrados é: {soma}"


LerNumeros()
print(MontarRerposta(vetorA))