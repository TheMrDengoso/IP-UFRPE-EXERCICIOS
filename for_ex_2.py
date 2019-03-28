m = 0
f = 0
m_altura =0 
for i in range(15):
    print("M-Masculino \nF-Feminino")
    ent = input("Digite a opção: ")
    altura = float(input("Digite a altura: "))
    m_altura = altura>m_altura
    lista1=[altura]
    lista2=[ent]
    if(ent=='M'or ent=='m'):
        m +=1
    if(ent=='F'or ent=='f'):
        f +=1
print(lista1,lista2)
