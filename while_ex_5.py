c =0
n1 = int(input("Digite um valor para a Base: "))
n2 = int(input("Digite um valor para o expoente: "))
s =1
if(n1==0):
    print("Digite um valor maior que 0 para a BASE!")
else:
    while True:
        if(n2==0):
            print("O valor da equação é 1")
        else:
            c+=1
            s *=n1

            if(c==n2):
                break
    print(s)
