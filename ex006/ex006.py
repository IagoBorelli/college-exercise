#5) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).


meses = ["1 - Janeiro", "2 - Fevereiro", "3 - Março", "4 - Abril", "5 - Maio", "6 - Junho", "7 - Julho", "8 - Agosto", "9 - Setembro", "10 - Outubro", "11 - Novembro", "12 - Dezembro"]
temp = []

for i in range(12): 
  temp.append(float(input(f"Informe a temperatura media do mês {meses[i]}: ")))
  print("----------------------------------------------------")
  sum(temp)

media = sum(temp) / len(temp)

print(f"A média anual das temperaturas é: {media:.2f}° \n")

for j in range(12):
  if (temp[j] > media):
    print(f"A temperatura do mês {meses[j]} foi {temp[j]}° e foi acima da média anual.")
    print("-------------------------------------------------------------------------------")