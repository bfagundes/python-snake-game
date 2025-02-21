from turtle import Turtle, Screen

# Variables / Config
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRID_SIZE = SCREEN_WIDTH // 2

def setup_game_window():
    screen = Screen()
    screen.title("Snake Game")
    screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
    screen.tracer(0)

    # Establish a grid-based coordinate system
    screen.setworldcoordinates(-GRID_SIZE, -GRID_SIZE, GRID_SIZE, GRID_SIZE)

    return screen

if __name__ == "__main__":
    screen = setup_game_window()
    screen.mainloop()