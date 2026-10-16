print('\nkhosh umdid be resturane deniz \n')
print('\tmenu ghaza \n')
pizza = ['pizza:', '1. pizza ghormesabzi', '2. pizza makhlut', '3. pizza makhsus\n']
for pizz in pizza :
    print(pizz)

salad = ['salad:', '1. salad fasl', '2. salad bil', '3. salad shirazi\n']
for saladd in salad:
    print(saladd)

morgh = ['morgh:', '1. morgh sokhari', '2. morgh abpaz', '3. morgh kham\n']
for morghh in morgh:
    print(morghh)

nushidani = ['nushidani:', '1. fanta', '2. mirenda', '3. soda\n']
for nushidunii in nushidani:
    print(nushidunii)

ghazaha = {'pizza ghormesabzi': 280,'pizza makhlut': 210,'pizza makhsus': 260,
            'salad fasl': 110,'salad bil': 130,'salad shirazi': 110,
           'morgh sokhari': 200,'morgh abpaz': 140,'morgh kham': 120,
           'fanta': 35,'mirenda': 30,'soda': 25
           }

print('jahate ettela az gheymate ghaza esme ghazaye khod ra vared konid: \n')
print('brye payane in marhale kalmae "baadi" ra vared konid: \n')

while True:
    ghaza = input()
    if ghaza == 'baadi':
        break
    elif ghaza in ghazaha:
        print(f'gheymat {ghaza} : {ghazaha[ghaza]} toman')
    else:
        print('in ghaza dar system mojud nist')

print('\nps az etmame sefareshetan kalmae "tamam" ra vared konid: \n')

mablaghe_kol = 0
sabad = []

print('sefareshe khod ra vared konid:')

while True :
    ghaza = input()
    if ghaza == 'tamam':
        break
    elif ghaza in ghazaha:
        mablaghe_kol += ghazaha[ghaza]
        sabad.append(ghaza)
    else:
        print('in ghaza dar menu mojud nist')

print('\nsefareshe shoma\n')
for item in sabad:
    print(f'{item} : {ghazaha[item]} toman')

print(f'\nmablaghe kol: {mablaghe_kol} toman')

address = input('\n lotfan address khod ra vared konid: ') 
print('\n peyk motori dar hale ersal sefaresh ast...')

tahvil = input("\nAya sefaresh tahvil dade shod? (yes/no): ").lower()

if tahvil == 'yes':
    print("\n sefaresh ba movafaghiat tahvil dade shod. mamnun az shoma!")
else:
    print("\n sefaresh tahvil dade nashod. lotfan ba resturan tamas bgirid.")