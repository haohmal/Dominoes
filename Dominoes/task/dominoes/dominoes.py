import random
from random import shuffle

status_text = ["It's your turn to make a move. Enter your command.", "Computer is about to make a move. Press Enter to continue..."]
over_text = ["Status: The game is over. You won!",
             "Status: The game is over. The computer won!",
             "Status: The game is over. It's a draw!"]

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

def print_game():
    print('=' * 70)
    print("Stock size: {0}".format(len(stock_pieces)))
    print("Computer pieces: {0}".format(len(computer_pieces)))
    print()
    if len(domino_snake) < 7:
        for domino in domino_snake:
            print(domino, end="")
    else:
        print("{0}{1}{2}...{3}{4}{5}".format(domino_snake[0],domino_snake[1],domino_snake[2],domino_snake[-3],domino_snake[-2],domino_snake[-1]))
    print()
    print()
    print("Your pieces:")
    for idx, domino in enumerate(player_pieces):
        print("{0}:{1}".format(idx+1, domino))

    print()
    print("Status: {0}".format(status_text[status]))

def move_player():
    while True:
        domino = choose_domino()
        if domino == 0:
            # if len(stock_pieces) > 0:
            player_pieces.append(stock_pieces.pop())
            break
        elif domino > 0:
            # if domino_snake[-1][1] in player_pieces[domino - 1]:
            domino_snake.append(player_pieces[domino - 1])
            player_pieces.remove(player_pieces[domino - 1])
            break
        else:
            # if domino_snake[0][0] in player_pieces[abs(domino) - 1]:
            domino_snake.insert(0, player_pieces[abs(domino) - 1])
            player_pieces.remove(player_pieces[abs(domino) - 1])
            break
    return


def choose_domino():
    while True:
        try:
            move = int(input())
            if abs(move) <= len(computer_pieces):
                return move
            print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def enter_return():
    move = input()
    return

def move_computer():
    while True:
        domino = random.randint(-(len(computer_pieces)), len(computer_pieces))
        if domino == 0:
            computer_pieces.append(stock_pieces.pop())
            break
        if domino > 0:
            domino_snake.append(computer_pieces[domino - 1])
            computer_pieces.remove(computer_pieces[domino - 1])
            break
        else:
            # if domino_snake[0][0] in player_pieces[abs(domino) - 1]:
            domino_snake.insert(0, computer_pieces[abs(domino) - 1])
            computer_pieces.remove(computer_pieces[abs(domino) - 1])
            break
    return



def analyze_game():
    if len(player_pieces) == 0:
        print(over_text[0])
        return False
    elif len(computer_pieces) == 0:
        print(over_text[1])
        return False
    return  True


# game loop
over = False
print_game()
while over is False:
    if status == 0:
        move_player()
    else:
        enter_return()
        move_computer()

    if status == 0:
        status = 1
    else:
        status = 0
    print_game()
    resume = analyze_game()
    if resume is False:
        break
