lista = []
sum = 0
m = 0
for x in range(4):
  nota = float(input("Digite a nota: "))
  lista.append(nota)
  sum += lista[x]
m = sum/4
print("Notas inseridas: {}".format(lista))
print("Média das notas: {:.2f}".format(m))
