# Python code to demonstrate the Application of 
# randrange()

import random

p1_sum = 0
p2_sum = 0
count = 0
flag = 0

while (1):
    # generate random number at each turn 1-10
    r1 = random.randrange(1, 10)
    r2 = random.randrange(1, 10)

    # adding to account of players
    p1_sum = p1_sum + r1
    p2_sum = p2_sum + r2
    count = count + 1
    print("Total score of Player 1 after turn %d is :  %d " % (count, p1_sum))

    # break when player 1 reaches 100 
    if p1_sum >= 100:
        flag = 1
        break
    print("Total score of Player 2 after turn %d is :  %d" % (count, p2_sum))

    # break when player 2 reaches 100 
    if p2_sum >= 100:
        flag = 2
        break

if flag == 1:
    print("\nPlayer 1 wins the game")
else:
    print("\nPlayer 2 wins the game")
