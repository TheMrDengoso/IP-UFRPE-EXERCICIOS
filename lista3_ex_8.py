nome = str(input("Digite o nome do funcionário: "))
sal = float(input("Digite o salário bruto do funcionário: "))
des = sal *5/100
sal_liq = sal - des
print("Nome do funcionário: {} \nSalário Bruto {:.2f} \nDesconto: {:.2f} \nSalário Líquido: {:.2f}".format(nome, sal, des, sal_liq))
