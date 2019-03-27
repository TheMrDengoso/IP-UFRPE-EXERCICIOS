s=1
n = int(input("Digite um valor para fatorar: "))

if(n<=20):
    while(n>=1):
        if(n==1):
            break
        else:
            s *= n
            n-=1
            
    print(s)    
    
else:
    print("Digite um valor menor ou igual a 20!")    