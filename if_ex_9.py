peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/(altura*2)

if(imc<20):
    print("Abaixo do peso")
elif(imc>20 and imc<=25):
    print("Peso ideal")
elif(imc>25 and imc<=30):
    print("Sobrepeso")
elif(imc>30 and imc<=35):
    print("Obesidade Moderada")
elif(imc>35 and imc<=40):
    print("Obesidade Severa")
elif(imc>40 and imc<=50):
    print("Obesidade Mórbida")
else:
    print("Super Obesidade")