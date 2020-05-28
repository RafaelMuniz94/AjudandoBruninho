# 10-Utilize uma lista para resolver o problema a seguir.
# Uma empresa paga seus vendedores com base em comissões. O vendedor recebe 200 por semana mais 9 por cento de suas vendas brutas daquela semana.
# Por exemplo, um vendedor que teve vendas brutas de 3.000 em uma semana recebe 200 mais 9 por cento de 3.000, ou seja, um total de 470.
# Escreva um programa (usando uma lista de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# 200 - 299
# 300 - 399
# 400 - 499
# 500 - 599
# 600 - 699
# 700 - 799
# 800 - 899
# 900 - 999
# 1000 em diante
# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

#Formula = 200 + (0.09*vendasBrutas)

l= [0, 0, 0, 0, 0, 0, 0, 0, 0]
inter = ["1 - 200-299",
         "2 - 300-399",
         "3 - 400-499",
         "4 - 500-599",
         "5 - 600-699",
         "6 - 700-799",
         "7 - 800-899",
         "8 - 900-999",
         "9 - 1000 em diante"]
x = 0
while True:
  n=float(input('Informe o salário %d° R$:'%(x+1)))
  if 200 <= n <=299:
    l[0]+=1
  elif 300 <= n <=399:
    l[1]+=1
  elif 400 <= n <=499:
    l[2]+=1
  elif 500 <= n <=599:
    l[3]+=1
  elif 600 <= n <699:
    l[4]+=1
  elif 700 <= n <=799:
    l[5]+=1
  elif 800 <= n <=899:
    l[6]+=1
  elif 900 <= n <=999:
    l[7]+=1
  elif n>= 1000:
     l[8]+=1
  x+=1
  d = input("Continuar o cálculo?(sim ou não)")
  if d == 'n':
      break
print("\n")
print("Informando a quantidade de cada salario:\n")
for key,b in enumerate(l):
    print(str(inter[key])+" : "+str(b))
