scores = input().split()
# put your python code here
loses = 0
last =  0
for i in range(len(scores)):
    if scores[i] == 'I':
        loses += 1
        if loses == 3:
            print("Game over")
            print(str(scores[0:i].count('C')))
            break
else:
    print("You won")
    print(str(scores.count('C')))