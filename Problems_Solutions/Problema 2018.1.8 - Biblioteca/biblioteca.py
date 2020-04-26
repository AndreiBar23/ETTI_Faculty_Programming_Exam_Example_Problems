
rafturi = []
lista_carti = []

capacitate, nr_intrari = input("Capacitate si nr intrari: \n").split(" ")

capacitate = int(capacitate)
nr_intrari = int(nr_intrari)

for loop in range(0, nr_intrari):
    nr_carti, dimensiune = input("Nr carti, nr pagini: \n").split(" ")
    nr_carti = int(nr_carti)
    dimensiune = int(dimensiune)
    lista_carti.append(nr_carti * [dimensiune])

temp = []
for tip_carte in lista_carti:
    for elem in tip_carte:
        temp.append( [elem, 1] )

lista_carti = temp

check = [el[1] for el in lista_carti]

lista_output = []

capacitate_raft = 0 
raft = []
print("\n")
while(sum(check) != 0):
    strVar = ''
    for cnt, carte in enumerate(lista_carti):
        if (capacitate_raft + carte[0] <= capacitate and check[cnt] == 1):
            capacitate_raft += carte[0]
            strVar += str(carte[0]) + " "
            check[cnt] = 0
            
    lista_output.append(strVar)
    capacitate_raft = 0

for cnt, elem in enumerate(lista_output):
    cnt +=1
    print(f"Raft {cnt}: "+ elem)





            


