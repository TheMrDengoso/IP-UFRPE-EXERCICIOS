m = float(input("Digite a quantidade em metros quadrados: "))
qnt = m/3
latas = qnt*80
latas_qnt = qnt//18
div = qnt%18
if div >0:
    latas_qnt+=1
print("M² = {} \nQuantidade de litros: {:.2f} \nQuantidade de latas: {} \nValor a ser pagado: {:.2f}".format(m, qnt,latas_qnt, latas))