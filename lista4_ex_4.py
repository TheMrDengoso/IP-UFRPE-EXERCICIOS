mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
data = str(input("Digite sua data de nascimento: "))
data = data.split("/")
mes_num = int(data[1])
for i in range(12):
  if(mes_num==i+1):
    print("Você nasceu em {} de {} de {}".format(data[0],mes[i],data[2]))
