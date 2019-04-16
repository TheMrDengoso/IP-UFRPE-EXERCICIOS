vogais_a = ['A','Á','À','Ã','á','à','ã','a']
vogais_e = ['E','É','È','e','é','è']
vogais_i = ['I','Í','Ì','i','í','ì']
vogais_o = ['O','Ó','Ò','Õ','o','ó','ò','õ']
vogais_u = ['U','Ú','Ù','u','ú','ù']
a=0
e=0
i=0
o=0
u=0

texto = str(input("Digite um texto qualquer: "))
espaço = texto.count(" ")
print(espaço)
qtd_a = len(vogais_a)
for i in range(qtd_a):
  a += texto.count(vogais[i])
for i in range(qtd_e):
  e += texto.count(vogais[i])
for i in range(qtd_i):
  i += texto.count(vogais[i])
for i in range(qtd_o):
  o += texto.count(vogais[i])
for i in range(qtd_u)
  u += texto.count(vogais[i])







print("Quantidade de vogais A ={} \nQuantidade de vogais E ={} \nQuantidade de vogais I ={} \nQuantidade de vogais O = {} \nQuantidade de vogais U = {}".format(a,e,i,o,u))
