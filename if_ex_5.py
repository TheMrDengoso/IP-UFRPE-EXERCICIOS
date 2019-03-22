n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))
n3 = int(input("Digite o 3º valor: "))
if(n1>n2 and n1>n3):
    if(n2>n3):
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
elif(n2>n1 and n2>n3):
    if(n1>n3):
        print(n2,n1,n3)
    else:
        print(n2,n3,n1)
elif(n3>n1 and n3>n2):
    if(n1>n2):
        print(n3,n1,n2)
    else:
        print(n3,n2,n1)
elif(n1==n2):
    if(n3>n1):
        print(n3,n1,n2)
    else:
        print(n1,n2,n3)
elif(n1==n3):
    if(n2>n1):
        print(n2,n1,n3)
    else:
        print(n1,n3,n2)
elif(n2==n3):
    if(n1>n2):
        print(n1,n2,n3)
    else:
        print(n2,n3,n1)
else:
    print("Números iguais!")