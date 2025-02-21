from turtle import Turtle, Screen

# Variables / Config
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

def setup_game_window():
    screen = Screen()
    screen.title("Snake Game")
    screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
    screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.tracer(0)

    return screen

if __name__ == "__main__":
    screen = setup_game_window()
    screen.mainloop()