imie = 'Danusia'
ile = 4
przedmiot = 'kwiat'

if ile == 1:
    print('{0} ma {1}a' .format(imie, przedmiot))
elif ile == 2:
    print('{0} ma {1} {2}y' .format(imie, ile, przedmiot))
else:
    print('{0} ma {1} {2}ow' .format(imie, ile, przedmiot))

if  'at' in przedmiot:
    print('Zaczyna sie na kw')
    
