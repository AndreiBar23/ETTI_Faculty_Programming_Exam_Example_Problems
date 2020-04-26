
lista_valori = []

intrare = input("Da Valori Dreptunghiuri: \n").split(" ")

sume_arii = []

def checkPitagora(x,y,z):
    if x** 2 == ((y ** 2) + (z ** 2)):
        return (y * z)/2
    else:
        return None 

for latura in intrare:
    lista_valori.append(int(latura))



for i in range(0, len(lista_valori)):
    for j in range(0, len(lista_valori)):
        for k in range(0, len(lista_valori)):
            if(i != j and i != k and j != i and j != k and k != i and k!= j):
                arie = checkPitagora(lista_valori[i], lista_valori[j], lista_valori[k])
                if arie is not None:
                    sume_arii.append(arie)

  


    

print(int(sum(sume_arii)/2))












