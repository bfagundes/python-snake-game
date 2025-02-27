from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score

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

def check_food_collision(snake, food, screen, score):
    """Check if the snake eats the food, and respawn the food if necessary."""
    if snake.segments[0].distance(food.food) < 15:
        # Log and score
        score.increment()
        print(f"Food eaten! Current score: {score.current}")

        # Respawn food
        food.spawn(snake.get_positions()) 

        # Grow snake
        snake.grow()

        # Update the screen immediately
        screen.update()

        return True
    else:
        return False
    
def detect_wall_collision(snake):
    """Checks if the snake has collided with the wall"""
    head = snake.get_head()
    return not (-GRID_SIZE <= head.xcor() <= GRID_SIZE and -GRID_SIZE <= head.ycor() <= GRID_SIZE)

def is_game_over(snake):
    return detect_wall_collision(snake) or snake.detect_self_collision()

def game_loop(screen, snake, food, score):
    """Updates the game every 1 second."""
    snake.move()
    check_food_collision(snake, food, screen, score)

    screen.update()

    if is_game_over(snake):
        print(f"Game Over!")
        score.reset()
        return
    
    # Schedule the next update after 1000 ms (1 second)
    screen.ontimer(lambda: game_loop(screen, snake, food, score), 500)

def main():
    screen = setup_game_window()
    
    score = Score()
    snake = Snake()
    food = Food(GRID_SIZE, snake.mov_unit)

    setup_controls(screen, snake)

    # Start the game loop
    game_loop(screen, snake, food, score)

    screen.mainloop()

if __name__ == "__main__":
    main()