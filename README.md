# Snake Game - GUI Based

A classic snake game implemented in Python using tkinter GUI framework.

## Features

- **Classic Gameplay**: Navigate the snake to eat food and grow longer
- **Smooth Controls**: Use arrow keys for smooth, responsive movement
- **Score Tracking**: Keep track of your score (10 points per food)
- **Progressive Difficulty**: Game speed increases slightly as you earn more points
- **Pause/Resume**: Press SPACE to pause and resume the game
- **Collision Detection**: Game ends when snake hits walls or itself
- **Restart Option**: Press 'R' to restart the game after game over

## Requirements

- Python 3.x
- tkinter (included with standard Python installation)

## How to Run

```bash
python snake_game.py
```

## Controls

- **Arrow Keys** - Move the snake (↑ Up, ↓ Down, ← Left, → Right)
- **SPACE** - Pause/Resume the game
- **R** - Restart after game over

## Game Rules

1. The snake starts in the middle of the board moving right
2. Red squares are food - eat them to grow and earn 10 points
3. The snake grows by 1 segment each time it eats food
4. The game ends if the snake:
   - Hits the wall (border of the game area)
   - Collides with itself
5. The game speed increases slightly as you progress

## Game Settings

You can customize the game by modifying these values in `SnakeGame.__init__()`:

- `WINDOW_WIDTH` / `WINDOW_HEIGHT` - Game board size (default: 600x600)
- `GRID_SIZE` - Size of each grid square (default: 20)
- `speed` - Initial game speed in milliseconds (default: 100)

## Gameplay Tips

- Try to create a snake pattern that doesn't trap yourself
- Keep an eye on the snake's position relative to walls
- Remember you can pause the game to plan your moves!

Enjoy the game!
