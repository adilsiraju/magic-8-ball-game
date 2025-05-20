# The Choices

answers = [
    'Yes - definitely.', 
    'It is decidedly so.', 
    'Without a doubt', 
    'Reply hazy', 
    'try again.', 
    'Ask again later.', 
    'Better not tell you now.', 
    'My sources say no.', 
    'Outlook not so good.', 
    'Very doubtful.'
    ]

import random
num = random.randint(0, 8)

question = input('Question: ')
print('Magic 8 Ball: '+ answers[num])