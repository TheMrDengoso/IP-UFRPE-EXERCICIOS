par = 0
impar = 0
for i in range(10):
  v = int(input("Digite um valor: "))
  if(v%2==0):
    par +=1
  else:
    impar +=1
print("Quantidade de números pares: {}".format(par))
print("Quantidade de núemros impares: {}".format(impar))
