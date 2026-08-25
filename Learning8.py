game =[[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],]


def game_play(game_map, player_move=0, row=0, column=0, just_display=False):
	print("   a  b  c")
	if not just_display:
		game_map[row][column]=player_move #if just_display = True then skips and it just displays
	for count, row in enumerate(game):
			print(count, row)
	return game_map

game = game_play(game,just_display=True)

game = game_play(game,1,0,2)


















'''game = "I want to play a Game"



def game_play(player_move=0, row=0, column=0, just_display=False):
	global game
	game = "A Game"
	print(id(game))
	print(game)


game_play()
print(game)
print(id(game))


'''











'''game =[[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],]


def game_play(player_move=0, row=0, column=0, just_display=False):
	print("   a  b  c")
	if not just_display:
		game[row][column]=player_move #if just_display = True then skips and it just displays
	for count, row in enumerate(game):
			print(count, row)


game_play(just_display=True)

game_play(1,0,2)
'''







