#Intercalar los elementos de una lista entre los elementos de otra. La intercalación
#deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
#una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
#y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7].

#import random
#def crearlista(n):
#    lista = []
#    for i in range(n):
#        lista.append(random.randint(0, 40))
#    print(lista)
#    return lista

#n = int(input("ingrese la cantidad de valores para la lista"))

lista1= [8, 1, 3]
#lista1 = lista1[1::]
print(lista1)
lista2=[5, 9, 7]
lista1[1:-2] = lista2
print("[8, 5, 1, 9, 3, 7] ")
print(lista1)

#lista2 = crearlista(n)
#lista2[-1:3] = crearlista(n)



#print(lista2)