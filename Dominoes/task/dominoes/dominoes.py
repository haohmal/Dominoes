from random import shuffle

status_text = ["It's your turn to make a move. Enter your command.", "Computer is about to make a move. Press Enter to continue..."]

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
            status = 0
            domino_snake.append(domino)
            computer_pieces.remove(domino)
            break
        elif domino in player_pieces:
            status = 1
            domino_snake.append(domino)
            player_pieces.remove(domino)
            break

# print("Stock pieces: {}".format(stock_pieces))
# print("Computer pieces: {}".format(computer_pieces))
# print("Player pieces: {}".format(player_pieces))
# print("Domino snake: {}".format(domino_snake))
# print("Status: {}".format(status))

print('=' * 70)
print("Stock size: {0}".format(len(stock_pieces)))
print("Computer pieces: {0}".format(len(computer_pieces)))
print()
print("{0}".format(domino_snake[0]))
print()
print("Your pieces:")
for idx, domino in enumerate(player_pieces):
    print("{0}:{1}".format(idx+1, domino))

print()
print("Status: {0}".format(status_text[status]))