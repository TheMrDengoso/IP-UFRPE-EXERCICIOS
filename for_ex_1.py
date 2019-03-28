c = 0
for i in range(10):
    qnt = int(input("Digite a quantidade itens vendidos pelo vendedor: "))
    if(qnt>0 and qnt<=19):
        c = qnt*0.10
        print("A comissão do {}º vendedor será de: {}%".format(i+1,c))
    elif(qnt>=20 and qnt<50):
        c = qnt*0.15
        print("A comissão do {}º vendedor será de {}%".format(i+1,c))
    elif(qnt>=50 and qnt<75):
        c = qnt*0.20
        print("A comissão do {}º vendedor será de {}%".format(i+1,c))
    else:
        c = qnt*0.25
        print("A comissão do {}º vendedor será de {}%".format(i+1,c))

    