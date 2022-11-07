#6) Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos e qual deles é o maior.

lista = []
maior = 0

for i in range(3):
  lista.append(int(input(f"Digite o valor {i + 1}: ")))
  sum(lista)
  if(maior < lista[i]):
    maior = lista[i]


print(f"A soma dos três números é: {sum(lista)}")
print(f"O maior número é: {maior}")

