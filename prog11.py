kwiaty = ['wrzos', 'chryzantema']

print(" petla 2 po indexie ")
for idx in range( len(kwiaty) ):
    print(kwiaty[idx])

print("== listy -> string ==")
print(";" .join(kwiaty))

print("== listy -> lista ==")
import_kwiaty = "tulipan, krokus, gozdzik"
lista = import_kwiaty.split('.')
print(lista)
