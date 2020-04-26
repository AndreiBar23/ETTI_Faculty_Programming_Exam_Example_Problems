from numpy import mean 
from numpy import argmax 

#get input data 
nr_studenti, discipline, burse = input().split(" ")

ordonare = []
ia_bursa = False
lista_medii = []
#populeaza lista cu date 
for i in range(0, int(nr_studenti)):
        nume = input()
        note = input().split(" ")
        ordonare.append([nume, note])
#scoate restantierii din lista
for index,elem in enumerate(ordonare):
    for j in range(0, int(discipline)):
        if int(elem[1][j]) < 5:
            ordonare.pop(index)
            break

medie_temp = []
for student in ordonare:
    for j in range(0, int(discipline)):
        medie_temp.append(int(student[1][j]))
    lista_medii.append(mean(medie_temp))
    medie_temp.clear()

medie_performanta = lista_medii[argmax(lista_medii)]
index_performanta = argmax(lista_medii)
lista_medii.sort()

medie_cnt = 0
for medie in lista_medii:
    if(medie == medie_performanta):
        continue
    if medie >= 8.0:
        medie_cnt +=1
    
    if medie_cnt == int(burse):
        break

print(medie_cnt)
print(ordonare[index_performanta][0] + " " + str(lista_medii[argmax(lista_medii)]))





        