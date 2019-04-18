from random import randint
s1 = str(input("Digite o 1º texto: ").replace("",""))
s2 = str(input("Digite o 2º texto: ").replace("",""))
len_s1 = len(s1)
len_s2 = len(s2)
print(len_s1)
menor = len_s1
if(len_s2<menor):
  menor = len_s2
r = randint(0,menor)
print(r)
