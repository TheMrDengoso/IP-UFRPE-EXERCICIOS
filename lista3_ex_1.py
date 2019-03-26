nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
altura = float(input("Digite a altura do aluno: "))
peso = float(input("Digite o peso do aluno: "))
end = input("Digite o endereço do aluno: ")
curso = input("Digite o curso do aluno: ")

print("-{}, residente no endereço {}, é aluno do curso de {}. Ele tem {} anos e {:.2f}m de altura e pesa {:.2f}kg".format(nome, end, curso, idade, altura, peso))