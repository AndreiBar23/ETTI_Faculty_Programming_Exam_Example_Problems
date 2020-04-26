zaruri = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,}

inputList = input("give input: \n").split(" ")

for elem in inputList[1:]:
    zaruri[elem] += 1

lista_aparitii = []
for elem in zaruri.items():
    lista_aparitii.append(elem[1])

dif = max(lista_aparitii) - min(lista_aparitii)
if(dif * 10 > 10):
    print("Zaruri Masluite")
else:
    print("Nu a fost Masluit")