def sentenceit(someList):
    sentence = ''
    for i in someList:
        if i in someList[0:-1]:
            sentence = sentence + i + ', '
        else:
            sentence = sentence + 'and ' + i
    print(sentence)


spam = ['apples', 'bananas', 'tofu', 'cats', 'lambs']
sentenceit(spam)
