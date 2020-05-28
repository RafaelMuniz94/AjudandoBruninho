# 3-Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
#  Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []


def LerIdadeEAltura():

    for i in range(5):
        idade = input(f"{i+1} -Qual sua idade? ")
        altura = input(f"{i+1} -Qual sua altura? ")
        alturas.append(altura)
        idades.append(idade)


def MontarTextoExibido():
    txtIdades = ""
    txtAlturas = ""
    for i in range(4, -1, -1):
        txtIdades += (str(idades[i]) + ',')
        txtAlturas+= (str(alturas[i]) + ',')
    return f"As alturas lidas, na ordem reversa sao {txtAlturas} \n As idades lidas, na ordem reversa sao: {txtIdades}"


LerIdadeEAltura()
print(MontarTextoExibido())
