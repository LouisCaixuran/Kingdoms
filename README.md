# About this project

The game is based on the board game Kingdoms by Reiner Knizia


bgg website:https://www.boardgamegeek.com/boardgame/119/kingdoms


#how to run

	$python3 Kingdoms.py


#how to play

First input the two players name(default is player1 and player2)

Then the two players should do your turn alternatively

in each turn you could choose from get a random board to put on the main board or build your own building on the main board 

there are four level of buildings, you have 1 level4, 2 level3, 3 level2, 4 level1

the normal random board contains value from -6 to +6 except 0, with each kind negative board one and each kind of positive board two

the score is calculate the sum of the value on each row and each column, times the sum of level of each players on that row or column

special boards:

1.dg:dragon, the row or column contains this one would only calculate the negative value,one per game

2.mt:mountain, the row or column contains this one would be separated into two rows or columns, two per game

3.wt:witch, the building besides the witch would be strengthened, level +1, one per game

4.gd:gold, the value of row or column contains gold would double.

That's all, enjoy your game :)




#Todo:
	
1.add the other 2 turns to make it as origin rule

2.add Internet related function to make online fight possible

3.add secrete board to each player

4.replace the board words and number with pictures

