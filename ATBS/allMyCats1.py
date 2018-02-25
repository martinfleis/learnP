# print('Enter the name of cat 1')
# catName1 = input()
# print('Enter the name of cat 2')
# catName2 = input()
# print('Enter the name of cat 3')
# catName3 = input()
# print('The cat names are:', catName1 + ',', catName2, 'and', catName3)

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothign to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # adding value to list
print('The cat names are:')
for i in catNames:
    print('•' + i)
