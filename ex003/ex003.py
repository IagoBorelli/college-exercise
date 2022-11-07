#2) Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista1 = []
par = []
impar = []

for a in range(20):
  lista1.append (int(input(f"Informe o valor da posição {a}: ")))
  if(lista1[a] % 2 == 0):
    par.append (lista1[a])
  else:
    impar.append (lista1[a])

print("Primeiro vetor: ")
print(lista1)
print("Vetor par: ")
print(par)
print("Vetor ímpar: ")
print(impar)
