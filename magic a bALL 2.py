import random





answers = ['yes','no','maybe so']
while True:
    print('ASK ME A QUESTION!!!')
    question = input('> ')
    if 'love' in question:
        print("who am i,GOD")
    elif 'die' in question:
        print("I cannot predict death")
    else:   
        answer = random.choice(answers)

        print(answer)
