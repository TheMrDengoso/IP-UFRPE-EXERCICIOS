'''
Created on 10 de set de 2015

@author: cleviton
'''
horaInicio = int(input("Hora de início: "))
minutoInicio = int(input("Minuto inicio: "))
horaFim = int(input("Hora Fim: "))
minutoFim= int(input( "Minuto Fim: "))

totalMinutInicio = (horaInicio * 60) + minutoInicio
totalMinutFim = (horaFim * 60) + minutoFim

if horaFim < horaInicio:
    totalMinutFim += (24 * 60)

tempo = totalMinutFim - totalMinutInicio
horasDuracao = tempo / 60
minutosDuracao = tempo % 60

print("Tempo total %d:%d" % (horasDuracao, minutosDuracao))
