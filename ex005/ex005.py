#4) Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


idade = []
altura = []
cont = 0

for i in range(30):
  idade.append(int(input(f"Informe a idade do aluno {i + 1}: ")))
  altura.append(float(input(f"Informe a altura do aluno {i + 1}: ")))
  print("---------------------------------------------")
  sum(altura)

media = sum(altura) / len(altura)

for j in range(30):
  if(idade[j] > 13) and (altura[j] < media):
    cont += 1

print(f"A media de altura é {media:.2f}")    
print(f"{cont} aluno(s) possue(em) mais de 13 anos e está(ão) abaixo da media de altura ")
