from random import shuffle

pieces = []
for x in range(7):
    for y in range(7):
        if x <= y:
            pieces.append([x,y])

domino_snake = []
status = None
while status is None:
    shuffle(pieces)
    stock_pieces = pieces[0:14]
    computer_pieces = pieces[14:21]
    player_pieces = pieces[21:]
    for i in range(6):
        domino = [6-i, 6-i]
        if domino in computer_pieces:
            status = "player"
            domino_snake.append(domino)
            computer_pieces.remove(domino)
            break
        elif domino in player_pieces:
            status = "computer"
            domino_snake.append(domino)
            player_pieces.remove(domino)
            break

print("Stock pieces: {}".format(stock_pieces))
print("Computer pieces: {}".format(computer_pieces))
print("Player pieces: {}".format(player_pieces))
print("Domino snake: {}".format(domino_snake))
print("Status: {}".format(status))

