texto = "Na próxima quarta-feira é feriado"

a1 = texto.count('a')
a2 = texto.count('á')
a3 = texto.count('à')
a4 = texto.count('ã')
a5 = texto.count('A')
a6 = texto.count('Á')
a7 = texto.count('À')
a8 = texto.count('Ã')
final_a = a1+a2+a3+a4+a5+a6+a7+a8

e1 = texto.count('e')
e2 = texto.count('é')
e3 = texto.count('è')
e4 = texto.count('E')
e5 = texto.count('É')
e6 = texto.count('È')
final_e = e1+e2+e3+e4+e5+e6

i1 = texto.count('i')
i2 = texto.count('í')
i3 = texto.count('ì')
i4 = texto.count('I')
i5 = texto.count('Í')
i6 = texto.count('Ì')
final_i = i1+i2+i3+i4+i5+i6

o1 = texto.count('o')
o2 = texto.count('ó')
o3 = texto.count('ò')
o4 = texto.count('õ')
o5 = texto.count('O')
o6 = texto.count('Ó')
o7 = texto.count('Ò')
o8 = texto.count('Õ')
final_o = o1+o2+o3+o4+o5+o6+o7+o8

u1 = texto.count('u')
u2 = texto.count('ú')
u3 = texto.count('ù')
u4 = texto.count('U')
u5 = texto.count('Ú')
u6 = texto.count('Ù')
final_u = u1+u2+u3+u4+u5+u6

print("a: ","*"*final_a,"({})".format(final_a))
print("e: ","*"*final_e,"({})".format(final_e))
print("i: ","*"*final_i,"({})".format(final_i))
print("o: ","*"*final_o,"({})".format(final_o))
print("u: ","*"*final_u,"({})".format(final_u))
