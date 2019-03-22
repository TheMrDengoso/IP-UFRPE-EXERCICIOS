n1 = float(input("Digite a 1º nota: "))
n2 = float(input("Digite a 2º nota: "))
m = (n1+n2)/2
if(m==10):
    print("Nota Máxima! \nA nota foi: {:.2f}".format(m))
elif(m>7):
    print("Aprovado! \nA nota foi: {:.2f}".format(m))
else:
    print("Reprovado! \nA nota foi: {:.2f}".format(m))