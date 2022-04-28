# whats really easy to get into and hard to get out of? timeout
# tom father has three sons jim john and whats the third one's name? tom
# a girl fell offa 20-foot ladder she wasnt hurt why? safety first

import time
time.sleep(1)

Q1 = input('whats really easy to get into and hard to get out of?')
if Q1 == 'timeout':
    time.sleep(1)
    print ("answer is right")
else:
    print("your answer is wrong")
    quit()

Q2 = input('tom father has three sons jim john and whats the third ones name?')
if Q2 == 'tom':
    time.sleep(1)
    print ("answer is right ")
else:
    print("your answer is wrong")
    quit()

Q3 = input('a girl fell off 20-foot ladder she wasnt hurt why?')
if Q3 == 'safety first':
    time.sleep(1)
    print ("answer is right")
else:
    print("your answer is wrong")
    quit()

