import string

vect = string.ascii_uppercase

alfabet = []

#punem litera cu litera pentru a forma vector nou 
for elem in vect:
    alfabet.append(elem)
mesaj = input("Introduceti string codat: ")
cnt = 0
out_string = ''
while(cnt < len(mesaj)):
    #luam doua cate doua 
    var_decoded = int(mesaj[cnt:cnt+2])
    if (var_decoded <= 26 and var_decoded is not 0):
        out_string += alfabet[var_decoded - 1]
        cnt +=2
    elif var_decoded == 0:
        out_string += " "
        cnt +=2
    else:
        out_string += alfabet[int(mesaj[cnt]) - 1]
        cnt += 1

#output 
print("Decoadare: " + out_string)
