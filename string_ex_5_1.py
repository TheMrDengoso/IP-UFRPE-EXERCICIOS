s = str(input())

cont = 0
inicio =0
while True:
    pos = s.find("ado",inicio)
    if pos==-1:
        break
    incio = pos +1
    cont +=1

print(cont)