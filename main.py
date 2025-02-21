from turtle import Turtle, Screen
from snake import Snake

# Variables / Config
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRID_SIZE = SCREEN_WIDTH // 2

def setup_game_window():
    screen = Screen()
    screen.title("Snake Game")
    screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    # Establish a grid-based coordinate system
    screen.setworldcoordinates(-GRID_SIZE, -GRID_SIZE, GRID_SIZE, GRID_SIZE)

    return screen

def setup_controls(screen, snake):
    """Binds keyboard controls to snake movement"""
    screen.listen()
    screen.onkey(lambda: snake.turn("up"), "Up")
    screen.onkey(lambda: snake.turn("down"), "Down")
    screen.onkey(lambda: snake.turn("left"), "Left")
    screen.onkey(lambda: snake.turn("right"), "Right")

    screen.onkey(lambda: snake.turn("up"), "w")
    screen.onkey(lambda: snake.turn("down"), "s")
    screen.onkey(lambda: snake.turn("left"), "a")
    screen.onkey(lambda: snake.turn("right"), "d")

def game_loop(screen, snake):
    """Updates the game every 1 second."""
    screen.update()  # Refresh screen
    snake.move()
    
    # Schedule the next update after 1000 ms (1 second)
    screen.ontimer(lambda: game_loop(screen, snake), 500)

def main():
    screen = setup_game_window()
    snake = Snake()
    setup_controls(screen, snake)

    # Start the game loop
    game_loop(screen, snake)

    screen.mainloop()

if __name__ == "__main__":
    main()