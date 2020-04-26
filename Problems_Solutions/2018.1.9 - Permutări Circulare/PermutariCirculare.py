
def transformare_binar(numar_decimal):
    vect_binar = []
    while(numar_decimal != 0):
        rest = numar_decimal % 2
        vect_binar.append(rest)
        numar_decimal = numar_decimal //2
#inversare vector 
    return vect_binar[::-1]

def back_to_decimal(vector_binar):
    sum = 0
    for cnt , binary in enumerate(vector_binar):
        sum += binary * (2**cnt)
    return sum

def permutare_circulara(vector_binar):
    numar_permutatii  = len(vector_binar)
    vector_out = []
    vector_temp = []

    copie = vector_binar.copy()
    for nr in range(0, numar_permutatii):
            vector_temp.append(copie[len(copie)- 1])
            for parcurgere in range (0, numar_permutatii - 1):
                vector_temp.append(copie[parcurgere])
            vector_out.append(back_to_decimal(vector_temp))
            print(f"Reprezentare binara: {vector_temp}")
            copie = vector_temp.copy()
            vector_temp.clear()
    print(f"Selectie maxim: {vector_out}")
    return max(vector_out)

numar_decimal = int(input("Indroduceti numar decimal: "))
vect_binar = transformare_binar(numar_decimal)

print(f"Numar dupa permutari: {permutare_circulara(vect_binar)}")






