nr_zile = int(input("Da nr de zile: "))

bani = input("Da banii: ").split(" ")


print(bani)
print("\n")

suma_bani = int(bani[0])
gradFericire = 0 
vect_fericire = []
for i in range(0, nr_zile):
    cost, fericire = input("Baga Cost si fericire: ").split(" ")
    vect_fericire.append(int(fericire))
    if((suma_bani - int(cost)) >= 0):
        gradFericire += int(fericire)
        print(f"Grad fericire: {gradFericire}")
        suma_bani -=  int(cost)
    else:
        for elem in vect_fericire[:len(vect_fericire) - 1]:
            if(int(fericire) > elem):
                gradFericire -= int(fericire)
                break
                
            
    if(i <= nr_zile - 2):
        suma_bani += int(bani[i+1])
    print(f"Ziua {i+1}, Suma bani: {suma_bani}")
    print("\n")

print(f"Grad fericire final: {gradFericire}\n")

