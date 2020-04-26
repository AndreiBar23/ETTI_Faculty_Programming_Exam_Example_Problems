nr_persoane = int(input("zi numarul de persoane\n"))

lista_date_nastere = []
for i in range(0, nr_persoane):
    zi, luna = input("zi ziua si data \n").split("-")
    lista_date_nastere.append(luna+zi)

#sort the birthday list in ascending order 
lista_date_nastere.sort()

#remove duplicates from birthday lists 
lista_date_nastere = list(dict.fromkeys(lista_date_nastere))

#first 2 chars is month, last 2 chars are day, reorder that 
for elem in lista_date_nastere:
    print(elem[2:4] + "-" + elem[0:2])






