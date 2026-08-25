game =[[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],]


def game_play(player_move=0, row=0, column=0, just_display=False):
	print("   a  b  c")
	if not just_display:
		game[row][column]=player_move #if just_display = True then skip this step and it just displays
	for count, row in enumerate(game):
			print(count, row)


game_play(just_display=True)

game_play(1,0,2)
