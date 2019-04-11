num = int(input("Digite o valor do número que você deseja saber a tabuada.: "))
x=0
t = ""
while x<11:
    print("{} X {} = {}".format(num, x, (num*x)))
    x+=1
    if(x==10):
        t = str(input("Deseja realizar uma nova tabuada?\ns/n\n"))
        if(t == "s" or t == "S"):
            num2 = int(input("Digite o valor da nova tabuada: "))
            num = num2
            x=0
        else:
            print("Fim.")