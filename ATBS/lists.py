spam = ['vampire', 'werewolf', 'harpy', 'witch']
# print('Beware of', spam)
# print('The', spam[1], 'fucked', spam[2] + '.')

ham = [['cat', 'dog'], [10, 20, 30, 40, 50]]
print(ham[0][-2])
print(len(ham[1]))
ham[0][0] = 'cow'
print(ham[0][0])

del spam[1]
print(spam)
