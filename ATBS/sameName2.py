# def spam():
#     global eggs
#     eggs = 'spam'
#
#
# eggs = 'global'
# spam()
# print(eggs)


def spam():
    global eggs  # global before means - use global variable
    eggs = 'spam'


def bacon():
    eggs = 'bacon'


def ham():
    print(eggs)


eggs = 42
spam()
ham()
