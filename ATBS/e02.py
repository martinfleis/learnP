name = 'John'
password = 'swordfish'
age = 50

# if name == 'Mary':
#     print('Hello Mary')
#     if password == 'swordfish':
#         print('Access granted.')
#     else:
#         print('Wrong password')
# elif name == 'Jose':
#     print('Hola Jose')
# else:
#     print('I do not know you.')

if name == 'Alice':
    print('Hello Alice')
elif age < 12:
    print('No way, kiddo.')
elif age > 60:
    print("You're quite old for this aren't you?")
else:
    print("Your age seems to be okay, but you are not Alice.")

spam = 0
while spam < 5:
    print("You need more. You have just", spam)
    spam = spam + 1
if spam >= 5:
    print("Finally!")
