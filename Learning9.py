game =[[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],]


def game_play(game_map, player_move=0, row=0, column=0, just_display=False):
    try:
        print("   a  b  c")
        if not just_display:
            game_map[row][column]=player_move #if just_display = True then skip this step and it just displays
        for count, row in enumerate(game):
                print(count, row)
        return game_map
    except :
        print("Error: row and column = 0,1 or 2")    

game = game_play(game,just_display=True)

game = game_play(game,player_move=1,row=3,column=2)

