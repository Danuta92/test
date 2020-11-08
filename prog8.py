kwiaty = ['wrzos', 'chryzantema']
#lotto = [4, 2, 5]

print(kwiaty[0])
print(kwiaty[1])

print("===petla 1 ===")
for k in kwiaty:
    print(k)

for idx in [0,1]:
    print(kwiaty[idx])

print("=== petla 2 po indexie === ")
for idx in range( len(kwiaty) ):
    print(kwiaty[idx])

for idx in range( len(kwiaty)):
    print( " {0} {1}" .format(idx, kwiaty[idx]))

lista = range(len(kwiaty))
print(lista)

print(" == listy -> string ==")
import_kwiaty = "wrzos;chryzantema;"
import_kwiaty.split(';')
print(lista)







# print("== petla 2 po indexie === ")
# print("len: {0}".format(len(samochody)))
# print("range: {0}".format(range(3)))
#
# for idx in range( len(samochody)):
#     print("{0} {1}".format(idx, samochody[idx]))
