qtd_bran = 0
qtd_nulo = 0
qtd_A = 0
qtd_B = 0
qtd_C = 0
for i in range(1,1):
    voto = int(input("Digite qual você deseja:\n1-Candidato A\n2-Candidato B\n3-Candidato C\n4-Voto Nulo\n5-Voto Branco\n: "))
    if(voto==1):
        qtd_A +=1
    elif(voto==2):
        qtd_B +=1
    elif(voto==3):
        qtd_C +=1
    elif(voto==4):
        qtd_nulo
    elif(voto==5):
        qtd_bran
    else:
        print("Valor Inválido.")
porce_nulo = (qtd_nulo/15) * 100
porce_bran = (qtd_bran/15) *100
print("Quantidade de Votos Candidato A: {}".format(qtd_A))
print("Quantidade de Votos Candidato B: {}".format(qtd_B))
print("Quantidade de Votos Candidato C: {}".format(qtd_C))
print("Porcentagem de votos brancos: {:.2f} %".format(porce_bran))
print("Pocentagem de votos nulos: {:.2f} %".format(porce_bran))