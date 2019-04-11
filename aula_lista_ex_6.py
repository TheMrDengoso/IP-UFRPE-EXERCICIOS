temp = []
mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
sum = 0
m= 0
for x in range(12):
  print("Informe a temperatura do {}º mês".format(x+1))
  v = float(input(": "))
  temp.append(v)
  sum += v
m = sum/12
print("A média do ano foi: {:.2f}".format(m))
for i,p in enumerate(temp):
  if(p>=m):
    print(i+1,"º -",mes[i], "=",p,"º")
