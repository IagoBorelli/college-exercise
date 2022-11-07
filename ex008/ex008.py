#7) Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.


def valor(a):
  if(a > 0):
    b = "P - POSITIVO"
  else:
    b = "N - NEGATIVO0"
    
  return b

number = int(input("Informe um número: "))
print(valor(number))