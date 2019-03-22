km = float(input("Digite quantos km foi percorrido: "))
horas = float(input("Digite a quantidade de horas: "))
vm = km/horas
print(vm)
if(vm>=110):
    print("Muito Rápido!")
else:
    print("Velocidade Normal!")