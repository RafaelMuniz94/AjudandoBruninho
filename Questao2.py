# 2-Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.


vetor = []


def LerNumeros():
    for i in range(5):
        vetor.append(int(input(f"{i+1} -Digite um numero:")))


def DefinirTexto(vetor):
    soma = 0
    multiplicacao = 0
    numerosLidos = ', '.join(str(x) for x in vetor)
    for numero in vetor:
        soma += numero
        if(multiplicacao == 0):
            multiplicacao = numero
        else:
            multiplicacao *= numero
    return f"Os numeros sao {numerosLidos}!\n A soma dos numeros é: {soma} \n A multiplicacao dos numeros é: {multiplicacao}"

LerNumeros()
print(DefinirTexto(vetor))
