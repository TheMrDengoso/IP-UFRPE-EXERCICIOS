anos = int(input("Digite quantos anos você tem: "))
meses = int(input("Digite quantos meses: "))
dias = int(input("Digite quantos dias: "))
anos = anos*365
meses = meses*30
t = anos+meses+dias
print("Você tem de vida: {} dias".format(t))
