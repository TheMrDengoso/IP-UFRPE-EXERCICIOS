maior = 0
menor = 0
m = 0
sum =0
for x in range(10):
  print("Informe a {}º temperatura".format(x+1))
  temp = float(input(": "))
  if(temp>maior):
    maior = temp
  else:
    menor = temp
    sum +=temp
m = sum/10
print("A média é de: {:.2f}º".format(m))
print("A maior temperatura é de: {}º".format(maior))
print("A menor temperatura é de: {}".format(menor))
