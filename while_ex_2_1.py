print("'99'Para Break.")
while True:
    n = int(input("Digite um valor inteiro: "))
    if(n==99):
        break
    elif(n%2==0):
        print("Este {} é par!".format(n))
    else:
        print("Este {} é impar!".format(n))