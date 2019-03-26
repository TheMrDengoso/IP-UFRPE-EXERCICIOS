qnt_alunos = 0
qnt_altura = 0
while True:
    idade = int(input("Digite a idade: "))
    if(idade<=100 and idade>0):
        altura = float(input("Digite a altura: "))
        if(altura==0):
            break            
        if(idade>=13):
            qnt_alunos +=1
            if(altura>=1.5):
                qnt_altura +=1
    else:
        print("Digite uma idade valida!")

print("Quantidade de alunos com mais de 13 anos: {} \nE maiores de que  1.50m: {}".format(qnt_alunos, qnt_altura))

    
