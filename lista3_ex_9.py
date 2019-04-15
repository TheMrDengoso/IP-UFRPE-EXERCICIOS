modelo = str(input("Digite o modelo do carro: "))
ano = int(input("Digite o ano do carro: "))
placa = input("Digite a placa do carro: ")
preço = float(input("Digite o preço sugerido: "))

if(modelo == "Ferrari" and ano >=2015):
    aum = 40/100
    final = preço + (preço*aum)
    print("Modelo: {} \nAno: {} \nPlaca: {} \nAluguel: {:.2f} R$/dia".format(modelo, ano, placa, final))
if(modelo == "Ferrari"):
    aum = 20/100
    final = preço + (preço*aum)
    print("Modelo: {} \nAno: {} \nPlaca: {} \nAluguel: {:.2f} R$/dia".format(modelo, ano, placa, final))
if(ano >= 2015):
    aum = 20/100
    final = preço + (preço*aum)
    print("Modelo: {} \nAno: {} \nPlaca: {} \nAluguel: {:.2f} R$/dia".format(modelo, ano, placa, final))
if(ano<= 2000):
    dim = 10/100
    final = preço - (preço*dim)
    print("Modelo: {} \nAno: {} \nPlaca: {} \nAluguel: {:.2f} R$/dia".format(modelo, ano, placa, final))
if(ano>2000 and ano<2015):
    print("Modelo: {} \nAno: {} \nPlaca: {} \nAluguel: {:.2f} R$/dia".format(modelo, ano, placa, preço))
