def somaimposto(taxa, custo):
  taxaimp = (taxa / 100)
  final = custo + (custo*taxaimp)
  return final

t = int(input("Digite a porcentagem do imposto: "))
c = float(input("Digite o custo: "))

x = somaimposto(t,c)
print(x)
