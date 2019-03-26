a = int(input("Digite até que numero você quer saber os pares: "))
while a>= 0:
    a -= 1
    if a%2 != 0:
        continue
    print(a)
    
else:
    print("FIM")