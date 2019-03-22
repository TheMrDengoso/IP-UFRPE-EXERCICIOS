ano = int(input("Digite um ano: \n#'EX:2000'"))
if(ano<=999 or ano>=10000):
    print("Valor invalido!")
else:
    if(ano%4==0):
        print("O ano {} é bissexto!".format(ano))
    else:
        print("O ano {} não é bissexto!".format(ano))