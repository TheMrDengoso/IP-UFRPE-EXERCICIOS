lista = [15,55,94,523,654,846,10,4,45,65,84,26,19,20,75,965,753,486,987,1156]
par = []
impar = []
for x in range(20):
  if(lista[x]%2==0):
    par.append(lista[x])
  else:
    impar.append(lista[x])
print("Números Pares: {}".format(par))
print("Núemros impares: {}".format(impar))
