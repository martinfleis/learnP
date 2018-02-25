myPets = ['Siri', 'Tlapa', 'Herman']
print('Enter pet name:')
name = input()
if name not in myPets:
    myPets = myPets + [name]
else:
    print('Pet already added.')
