lista = []
maior = 0
menor = 100
for x in range(20):
  v = int(input("Digite a idade: "))
  lista.append(v)
  if(v>maior):
    maior = v
  if(v<menor):
    menor = v
print("A maior idade: {}\nA menor idade: {}".format(maior, menor))
