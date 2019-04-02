cedula = int(input())
cem=0
cinq =0
vin =0
dez =0
cinco =0
dois = 0
um =0
if(cedula>=100):
        cem = cedula//100
        cedula -= (cem*100)

elif(cedula>=50 and cedula<100):
        cinq = cedula//50
        cedula -=(cinq*50)
elif(cedula>=20 and cedula<50):
        vin = cedula//20
        cedula -= (vin*20)
elif(cedula>=10 and cedula<20):
        dez = cedula//10
        cedula -= (dez*10)
elif(cedula>=5 and cedula<10):
        cinco = cedula//5
        cedula -= (cinco*5)
elif(cedula>=2 and cedula<5):
        dois = cedula//2
        cedula -= (dois*2)   
elif(cedula==1):
        um = cedula//1
        cedula -= (um*1)

print(cem)
print("{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00".format(cem, cinq, vin, dez, cinco, dois, um))
