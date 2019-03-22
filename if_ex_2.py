temp = float(input("Digite a temperatura do corpo: "))
if(temp>=39):
    print("Febre Alta!")
elif(temp<39 and temp>=37):
    print("Febril")
else:
    print("Sem febre")