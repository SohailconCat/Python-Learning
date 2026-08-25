game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_play():
    print("   a  b  c")
    for count, row in enumerate(game):
        print(count, row)


game_play()

game[0][1]=1

game_play()
