# 5-Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.


vetorA = []
vetorB = []

def LerNumeros():
    for i in range(10):
        vetorA.append(int(input(f"{i+1}A -Digite um numero:")))
        vetorB.append(int(input(f"{i+1}B -Digite um numero:")))

def IntercalarVetores(vetor1,vetor2):
    vetor3 = []
    for i in range(10):
        vetor3.append(vetor1[i])
        vetor3.append(vetor2[i])
    return vetor3

def MontarResposta(vetor1,vetor2):
    return f"Os vetores originais sao: VetorA:{vetor1} e VetorB:{vetor2} \n O vetor intercalado é: VetorC:{IntercalarVetores(vetor1,vetor2)}"

LerNumeros()
print(MontarResposta(vetorA,vetorB))