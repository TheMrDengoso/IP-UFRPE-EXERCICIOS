def qtd(num):
  c = 0
  while True:
    y = num//10
    num = y
    c += 1
    if y ==0:
      break
  return c

n = int(input("Digite o numero: "))
x = qtd(n)
print(x)
