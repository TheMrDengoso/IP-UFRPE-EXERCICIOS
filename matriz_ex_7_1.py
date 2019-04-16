def exibir_matriz(m):
    for l in m:
        print(l)
        
c = int(input("Digite a quantidade de colunas que deseja: "))
l = int(input("Digite a quantidade de linhas que deseja: "))

m = []
for i in range(l):
    m.append([0]*c)

exibir_matriz(m)
