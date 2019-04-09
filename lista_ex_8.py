from random import randint

s1 = str(input("1º Palavra: "))
s2 = str(input("2º Palavra: "))
if(s1>s2):
    menor = len(s2)
else:
    menor = len(s1)

pos = randint(0,menor)
print("Posição do Crossover: {}".format(pos))

palvra1 = s1[0:pos] + s2[pos:]
palvra2 = s2[0:pos] + s1[pos:]

print(palvra1)
print(palvra2)