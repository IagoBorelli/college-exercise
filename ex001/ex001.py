def alc(a, b):
  if (a <= 20):
    a *= 1.9
    b = a - ((a * 3) / 100)
  else:
    a *= 1.9
    b = a - ((a * 5) / 100)
  return b

def gas(a, b):
  if (a <= 20):
    a *= 2.5
    b = a - ((a * 4) / 100)
  else:
    a *= 2.5
    b = a - ((a * 4) / 100)
  return b

litro = float(input("Informe quantos litros: "))
tipo = input("Informe o tipo de combustível: A - álcool | G - gasolina \n")

if (tipo == "a"):
  alc(litro, tipo)
  print("O valor a ser pago é: ")
  print(alc(litro, tipo))

elif (tipo == "g"):
  gas(litro, tipo)
  print("O valor a ser pago é: ")
  print(gas(litro, tipo))
