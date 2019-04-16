v_inicial = int(input("Digite a velocidade inicial: "))
v_final = 0
tempo = 0
gravidade = 10
while True:
  v_final = v_inicial-(gravidade*tempo)
  print("Tempo = {} --------- Velocidade = {} m/s".format(tempo, v_final))
  if(v_final==0):
    break
  tempo+=1
  
