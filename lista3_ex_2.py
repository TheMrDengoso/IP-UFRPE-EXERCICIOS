a=0
l=[0,0,0,0,0,0,0,0,0,0]
soma = 0
media= 0
m = 0
qnt = 0
while a < 10:
    n = int(input("Digite um valor qualquer inteiro: "))
    l[a]=n
    a+=1
    if(n%2==0):
        print("{} é par!".format(n))
        soma += l[a]
    else:
        print("{} é impar!".format(n))
        qnt = len(l)
        m += l[a]
        media = m/qnt
        

print(l)
print(soma)
print(media)