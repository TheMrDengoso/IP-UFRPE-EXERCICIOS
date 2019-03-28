c=0
while c<5:
    n = int(input("Digite o valor: "))
    if(n<0):
        print("Valor invalido!")
        break
    else:
        print("Valor {} correto positivo".format(n))
        c +=1