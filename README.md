# 🐍 Python Snake Game

A classic Snake game implemented in Python using the Turtle module, following Test-Driven Development (TDD) principles. The game features food spawning, collision detection, a scoring system, and keyboard controls.

## Features
- Grid-based movement
- Food spawning with collision avoidance
- Wall & self-collision detecti
- Score tracking with UI displ
- Keyboard controls (Arrow key& WASD)
- TDD-tested with `unittest`

## How to Run
### 1. Clone the Repository
```bash
git clone https://github.com/bfagundes/python-snake-game.git
cd snake-game
```

This game uses Python’s built-in `turtle` module, so no external dependencies are required. Ensure you have Python installed.

### 3. Run the Game
```bash
python main.py
```

## Controls
| Key | Action |
|-----|--------|
| **Arrow Keys** or **WASD** | Move the snake |

## Project Structure
```
snake-game
 ├── main.py           # Game loop & setup
 ├── snake.py          # Snake movement logic
 ├── food.py           # Food spawning logic
 ├── score.py          # Scoreboard system
 ├── test_main.py      # Tests for main game mechanics
 ├── test_snake.py     # Tests for snake behavior
 ├── test_food.py      # Tests for food spawning
 ├── README.md         # Documentation
```

## Running Tests
The game follows TDD (Test-Driven Development), ensuring all logic is properly tested.

### Run all tests:
```bash
python -m unittest discover
```
or
```bash
pytest  # If you prefer pytest
``` 

## Screenshots
Coming soon... 🎮

## 📜 License
This project is **MIT licensed**. Feel free to modify and contribute!