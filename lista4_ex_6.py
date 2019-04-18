texto = str(input("Digite o texto: ").lower())
texto_s = texto.replace(" ","")

if(texto_s[::-1]==texto_s):
  print("Polindromo")
else:
  print("Não é Polindromo")
