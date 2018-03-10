birhtdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (leave blank to quit)')
    name = input()
    if name == '':
        break
    if name in birhtdays:
        print(birhtdays[name] + ' is the birthday of ' + name)
    else:
        print('I don not have that information for ' + name)
        print('Can you add it?')
        bday = input()
        birhtdays[name] = bday
        print('Database updated.')
