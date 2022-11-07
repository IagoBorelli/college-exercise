"""
1) Leia um conjunto de números reais, armazenando-o em uma lista. Em seguida, calcule o quadrado de cada elemento dessa lista armazenando esse resultado em outra lista. Os conjuntos têm, no máximo, 20 elementos. Imprima os dois conjuntos de números
"""

lista1 = []
lista2 = []

for i in range(20):
  lista1.append(float(input(f"Informe o {i + 1}º número: ")))
  print("----------------------------------")
  lista2.append(lista1[i] ** 2)

print("Primeiro conjunto: ")
print(lista1)
print("Segundo conjunto: ")
print(lista2)
