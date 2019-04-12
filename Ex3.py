'''
Created on 22 de mar de 2016
Esse algoritmo faz o cálculo mais simples. Ou seja, ele não considera os anos bisextos nem os meses com 28, 29 e 31 dias.

@author: cleviton
'''
anos = int(input("Informe quantos anos completos você têm: "))
meses = int(input("Informe quantos meses completos você tem, desconsiderando os anos: "))
dias = int(input("Informe quantos dias completos você tem, desconsiderando os anos e os meses"))
idadeEmDias = (anos * 365) + (meses * 30) + (dias)
print(idadeEmDias)

'''
Como calcular certo? (considerando bisextos e meses com quantidade de dias diferentes?)
É preciso saber a data de nascimento da pessoa, para a partir daí fazer o cálculo preciso.
Como seria? 
'''