lista = []
for x in range(5):
  v = int(input("Digite o valor: "))
  lista.append(v)
for i,p in enumerate(lista):
  print(i+1, "º = ",p)
