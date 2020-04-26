fete_zar = [x for x in range(1,7)]

nr_zaruri = int(input("Da nr zaruri\n"))

fete_vizibile = []
for i in range(0, nr_zaruri):
    fete_vizibile.append(input("Da fetele care se vad\n").split(" "))

output_sum = 0
for fata_vizibila in fete_vizibile:
    total_sum = sum([1,2,3,4,5,6])
    for elem in fata_vizibila:
        total_sum -= int(elem)
    output_sum += total_sum


print(output_sum)