j1 = input("Rodada 1, Jogue jogador 1: ")
j2 = input("Rodada 1, Jogue jogador 2: ")
g1=0
g2=0
if(j1=="Pedra" and j2=="Tesoura"):
    g1+=1
    print("Jogador 1 ganhou")
elif(j1=="Pedra" and j2=="Papel"):
    g2+=1
    print("Jogador 2 ganhou")
elif(j1=="Tesoura" and j2=="Papel"):
    g1+=1
    print("Jogador 1 ganhou")
elif(j1=="Tesoura" and j2=="Pedra"):
    g2+=1
    print("Jogador 2 ganhou")
elif(j1=="Papel" and j2=="Pedra"):
    g1+=1
    print("Jogador 1 ganhou")
elif(j1=="Papel" and j2=="Tesoura"):
    g2+=1
    print("Jogador 2 ganhou")
else:
    print("Empate")
j1 = input("Rodada 2, Jogue jogador 1: ")
j2 = input("Rodada 2, Jogue jogador 2: ")
if(j1=="Pedra" and j2=="Tesoura"):
    g1+=1
    print("Jogador 1 ganhou")
elif(j1=="Pedra" and j2=="Papel"):
    g2+=1
    print("Jogador 2 ganhou")
elif(j1=="Tesoura" and j2=="Papel"):
    g1+=1
    print("Jogador 1 ganhou")
elif(j1=="Tesoura" and j2=="Pedra"):
    g2+=1
    print("Jogador 2 ganhou")
elif(j1=="Papel" and j2=="Pedra"):
    g1+=1
    print("Jogador 1 ganhou")
elif(j1=="Papel" and j2=="Tesoura"):
    g2+=1
    print("Jogador 2 ganhou")
else:
    print("Empate")
j1 = input("Rodada 3, Jogue jogador 1: ")
j2 = input("Rodada 3, Jogue jogador 2: ")
if(j1=="Pedra" and j2=="Tesoura"):
    g1+=1
    print("Jogador 1 ganhou")
elif(j1=="Pedra" and j2=="Papel"):
    g2+=1
    print("Jogador 2 ganhou")
elif(j1=="Tesoura" and j2=="Papel"):
    g1+=1
    print("Jogador 1 ganhou")
elif(j1=="Tesoura" and j2=="Pedra"):
    g2+=1
    print("Jogador 2 ganhou")
elif(j1=="Papel" and j2=="Pedra"):
    g1+=1
    print("Jogador 1 ganhou")
elif(j1=="Papel" and j2=="Tesoura"):
    g2+=1
    print("Jogador 2 ganhou")
else:
    print("Empate")
if(g1>g2):
    print("O jogador 2 lava a louça")
elif(g1==3):
    print("Jogador 2 lavar a louça duas vezes")
elif(g2==3):
    print("Jogador 1 lava louça duas vezes")
elif(g2>g1):
    print("O jogador 1 lava a louça")
else:
    print("Os dois lavam a louça")