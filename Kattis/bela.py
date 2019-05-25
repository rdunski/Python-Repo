import sys

dom = {"A":11,"K":4,"Q":3,"J":20,"T":10,"9":14,"8":0,"7":0}
non = {"A":11,"K":4,"Q":3,"J":2,"T":10,"9":0,"8":0,"7":0}

n = input()
n = n.split(" ")
hands = int(n[0])
hands *= 4
suit = n[1]

points = int(0)

for line in sys.stdin:
    card = line.strip('\n')
    card = list(card)
    if card[1] == suit:
        points += dom[card[0]]
    else:
        points += non[card[0]]
    hands -= 1
    if hands == 0:
        break;

print(points)
