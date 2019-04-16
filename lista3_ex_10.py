A = 0
P = 0
x=1
aluno_str = ""
ausencia = 0
ausencia_str = ""
maiorturma = ""
while True:
    turma = str(input("Digite o nome da turma: \n0-para parar\n: "))
    if(turma == "0"):
        break
    aluno = int(input("Digite a quantidade de alunos: "))
    while(x<=aluno):
        print("O {}º aluno esta 'Ausente' ou 'Presente? \nA = Ausente \nP = Presente".format(x))
        falta = str(input(": "))
        if(falta == "A" or falta == "a"):
            A +=1
        if(falta == "P" or falta == "p"):
            P +=1
        x+=1
    
    ausencia = aluno * (A/100)
    if(ausencia >= 0.05):
        str(ausencia)
        maior = turma + " "
        ausencia_str = ausencia
        print("A turma: {} possui {}% de ausencia".format(maior, ausencia_str))
    else:
        str(ausencia)
        ausencia_str = ausencia
        print("A turma :{} possui {}% de ausencia".format(turma, ausencia_str))
    
