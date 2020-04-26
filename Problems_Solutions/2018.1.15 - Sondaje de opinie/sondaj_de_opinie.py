from numpy import argmax 
nr_partide, sondaje = input("Da nr partid si sondaje\n ").split()

partid  = []
partid_crescator = [] 
vect_calcul_sondaj = []
for i in range(0, int(nr_partide)):
    partid.append(input("Da date despre partid\n ").split(" "))

for i in range(0, len(partid)):
    crescator = False 
    for j in range(1, int(sondaje)):
        if (int(partid[i][j]) <= int(partid[i][j+1])):
            crescator = True
        else:
            crescator = False
            break
    if crescator == True:
        partid_crescator.append(partid[i][0])
    vect_calcul_sondaj.append(int(partid[i][int(sondaje)]) - int(partid[i][1]))

if len(partid_crescator) == 0:
    print("Nu exista")
else:
    print(partid_crescator)

index = argmax(vect_calcul_sondaj)

print(f"Partid invingator {partid[index][0]}  {int(partid[index][int(sondaje)]) - int(partid[index][1]) }%")
    




