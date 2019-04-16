def exibir_matriz(m):
    for l in range(len(m)):
        linha = ""
        for c in range(len(m[l])):
            linha += str(m[l][c]) + " "
        print("[{}]".format(linha[:-1]))
        
c = int(input("Digite a quantidade de colunas que deseja: "))
l = int(input("Digite a quantidade de linhas que deseja: "))

m = []

for i in range(l):
    m.append([0]*c)



for i in range(l):
    for j in range(c):
        print("Digite um valor para [{}], [{}]".format(i, j))
        m[i][j] = int(input(": "))
        
exibir_matriz(m)
