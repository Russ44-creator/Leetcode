# https://www.1point3acres.com/bbs/thread-772442-1-1.html
'''
We’re building a simple match-3 game. The game board comprises of tiles of different colors. 
The aim of the game is to align three or more tiles of the same color so that they can be 
removed from the game.
This is an example state of the board:
// G B B B G
// G Y R B G
// G Y B G Y
// R Y Y Y R
// B Y R G Y
//Where G=Green, B=Blue, R=Red, and Y=Yellow tile.
Tiles are removed from the board if there are three or more consecutive tiles 
of the same color. In the example above, the highlighted tiles satisfy this condition.
Requirements
Write a function that takes the state of the board as input, and returns a 
list of tiles that must be removed from the board. Note that we want to just 
identify the tiles, not remove them.
The matches can only be horizontal or vertical. We don’t care about diagonal matches.
You can store the board any way you like, but keep it simple.
The implementation should be able to work for any number of distinct tile colors, 
and any board size.
Please include comments to make it easier to u‍‌‍‍‍‌‌‍‌‌‍‌‍‍‌‍‌‍‍‍nderstand your code.
Bonus Points
Write unit tests to test your implementation.
'''

# feel like number of islands

