lista = []
for x in range(10):
  v = float(input("Digite um valor: "))
  lista.append(v)
lista.reverse()
for i,p in enumerate(lista):
  print(i+1,"º = ",p)
