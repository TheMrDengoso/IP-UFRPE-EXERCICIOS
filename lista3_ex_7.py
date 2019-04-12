pri =0
seg = 0
ter = 0
qua = 0
ler_pri =0
ler_seg =0
ler_qua =0
red_pri =0
n_red_seg =0
livros_pri =0
maior_qtd =0

while True:
    serie int(input("Digite sua serie\n1-Primeira\n2-Segunda\n3-Terceira\n4-Quarta\n0-Para Parar"))
    if(serie==1):
        pri +=1
        ler = int(input("Você Ler livros? \n1 - Sim\n2 - Não\n: "))
        if(ler=="Sim"):
            ler_pri +=1
            qtd = int(input("Quantos por mês: "))
            if(qtd>=1):
                livros_pri +=1
                
        red = int(input("Gosta de fazer redação? \n1-Sim \n2-Não \n: "))
        if(red==1):
            red_pri +=1
    if(serie==2):
        seg+=1
        ler = int(input("Voce Ler livros? \n1-Sim \n2-Não \n: "))
        if(ler==1):
            ler_seg +=1
            qtd = int(input("Quantos por mês: "))
        red = int(input("Gosta de fazer redaçõa? \n1-Sim \n2-Não \n: "))
        if(red==2):
            n_red_seg +=1
    if(serie==3):
        ter+=1
        ler = int(input("Voce Ler livros? \n1-Sim \n2-Não \n: "))
        qtd = int(input("Quantos por mês: "))
        red = int(input("Gosta de fazer redaçõa? \n1-Sim \n2-Não \n: "))
    if(serie==4):
        qua+=1
        ler =int(input("Voce Ler livros? \n1-Sim \n2-Não \n: "))
        if(ler==1):
            ler_qua +=1
            qtd = int(input("Quantos por mês: "))
            if(qtd>maior_qtd):
                maior_qtd = qtd
        red = int(input("Gosta de fazer redaçõa? \n1-Sim \n2-Não \n: "))
    if(serie==0):
        break
porcen = (n_red_seg*100)/seg
print("Quantidade de alunos na terceira serie: {} alunos".format(ter))
print("A maior quantidade de livros lidos por um aluno na quarta serie: {} livros".format(maior_qtd))
print("Porcentagem de alunos da segunda serie que não gosta de redação: {}%".format(porcen))
print("Quantidade de alunos da primeira serie que ler mais de um livro por mes: {} livros".format(livros_pri))
print("Alunos da primeira serie: {} \nAlunos da segunda serie: {} \nAlunos da terceira serie: {} \nAlunos da quarta serie: {}".format(pri, seg, ter, qua))
