turma = str(input("Digite o nome da turma: "))
aluno = int(input("Digite a quantidade de alunos: "))
A = 0
P = 0
x=1
while(x<=aluno):
    print("O {}º aluno esta 'Ausente' ou 'Presente? \nA = Ausente \nP = Presente")
    falta = str(input(": "))
    if(falta == "A" or falta == "a"):
        A +=1
    
