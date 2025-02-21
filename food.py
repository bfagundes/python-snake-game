from turtle import Turtle
import random

class Food:
    """Represents the food for the Snake"""
    def __init__(self, grid_size, mov_unit):
        self.food = Turtle()
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()

        # Make it a little smaller
        self.food.shapesize(stretch_wid=0.5, stretch_len=0.5)

        self.grid_size = grid_size
        self.mov_unit = mov_unit

        # Store the last spawn
        self.spawn_position = (0,0)
        
    def random_position(self):
        """Generates a random position within the grid"""
        max_coord = self.grid_size // self.mov_unit
        x = random.randint(-max_coord, max_coord) * self.mov_unit
        y = random.randint(-max_coord, max_coord) * self.mov_unit
        return (x,y)
    
    def spawn(self, snake_positions):
        """Spawns a Food object at a random location"""
        while True:
            new_position = self.random_position()

            # Ensure food is not colliding with the snake
            if new_position not in snake_positions:
                self.food.goto(new_position)
                self.spawn_position = new_position
                break