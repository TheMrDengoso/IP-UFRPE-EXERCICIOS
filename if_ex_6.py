p1 = float(input("Digite o valor do 1º produto: "))
p2 = float(input("Digite o valor do 2º produto: "))
p3 = float(input("Digite o valor do 3º produto: "))
if(p1<p2 and p1<p3):
    print("Compre o 1º produto")
elif(p2<p1 and p2<p3):
    print("Compre o 2º produto")
elif(p3<p1 and p3<p2):
    print("Compre o 3º produto")
elif(p1==p2 and p2==p3):
    print("Voce pode escolher qualquer um!")
elif(p1==p2 and p1<p3):
    print("Você pode escolher entre o 1º e o 2º produto")
elif(p2==p3 and p2<p1):
    print("Você pode escolher entre o 2º e 3º produto!")
elif(p1==p3 and p1<p2):
    print("Você pode escolher entre o 1º e 3º produto!")