#3) Faça um Programa que leia uma lista de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista = []
mult = 1

for i in range(5):
  lista.append (int(input(f"Digite o valor da posição {i}: ")))
  sum(lista)
  mult *= lista[i]

print(f"A soma de todos os valores é: {sum(lista)}")
print(f"A multiplicação de todos os valores é: {mult}")
print("Lista completa: ")
print(lista)