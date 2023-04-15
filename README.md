# Sokoban-Game
Developed the rules of the Sokoban game with Python and wrote an additional program that solves the Sokoban puzzles in the shortest sequence of moves

## Gameplay
The player controls a snake and the goal is to push computers around an environment with walls and barriers until every target (yellow flag) is covered with a computer.

To play, run `server.py`.

All gameboard are representated as a dictionary with keys-value pairs being game objects and their locations on the board. The dictionary also contains the size of the game board.

## Solver
The solver will return the shortest sequence of moves ("up", "down", "left", and "right") necessary to reach the victory condition if possible.

## Example
Game interface

<img width="672" alt="Screen Shot 2023-04-15 at 10 15 59" src="https://user-images.githubusercontent.com/105997889/232230336-38d78981-1444-443d-8269-4c10d1f9603f.png">

Gameplay screenshot in victory condition:
<img width="1092" alt="Screen Shot 2023-04-15 at 10 27 31" src="https://user-images.githubusercontent.com/105997889/232230555-709fac55-fd49-49d2-9140-b61513292bf7.png">
