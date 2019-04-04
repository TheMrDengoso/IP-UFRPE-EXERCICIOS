x = int(input())
p= x
i=1
c=0
while True:
    y = int(input())
    if(y>x):
        break
while True:
    x = x+i
    if(x>=y):
        break
    i += 1
    c +=1
    
print("X= {}".format(p))
print("Y = {}".format(y))
print("Quantidade: {}".format(c))
