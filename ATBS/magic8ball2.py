import random

messages = ['It is certain',
            'it is decidedly so',
            'yes definitely',
            'reply hazy try again',
            'ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good'
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
