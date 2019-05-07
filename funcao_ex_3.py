def argumento(num):
  c = ''
  if num >0:
    c = 'P'
  else:
    c = 'N'
  return c

v = int(input("Digite o valor: "))
x = argumento(v)
print(x)
