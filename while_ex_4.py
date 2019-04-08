g=0
n=1
print("2\n3\n5")
while True:
    n+=1
    if(n%2!=0):
        if(n%3!=0):
            if(n%5!=0):
                g+=1
                print(n)
                if(g==15):
                    break
