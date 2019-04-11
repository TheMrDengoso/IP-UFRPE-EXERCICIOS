qtd_bran = 0
qtd_nulo = 0
qtd_A = 0
qtd_B = 0
qtd_C = 0
for i in range(15):
    voto = int(input("Digite qual você deseja:\n1-Candidato A\n2-Candidato B\n3-Candidato C\n4-Voto Nulo\n5-Voto Branco\n: "))
    if(voto==1):
        qtd_A +=1
    elif(voto==2):
        qtd_B +=1
    elif(voto==3):
        qtd_C +=1
    elif(voto==4):
        qtd_nulo +=1
    elif(voto==5):
        qtd_bran +=1
    else:
        print("Valor Inválido.")
porce_nulo = (qtd_nulo/15) * 100
porce_bran = (qtd_bran/15) *100
print("Quantidade de Votos Candidato A: {}".format(qtd_A))
print("Quantidade de Votos Candidato B: {}".format(qtd_B))
print("Quantidade de Votos Candidato C: {}".format(qtd_C))
print("Quantidade de Votos Nulos: {}".format(qtd_nulo))
print("Quantidade de Votos Brancos: {}".format(qtd_bran))
print("Porcentagem de votos brancos: {:.2f} %".format(porce_bran))
print("Pocentagem de votos nulos: {:.2f} %".format(porce_bran))
