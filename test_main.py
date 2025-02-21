import unittest
from unittest.mock import Mock
from snake import Snake
from food import Food
from turtle import Screen
from main import (
    check_food_collision
)

class TestFoodCollision(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        # Mocking screen to avoid actual rendering
        self.screen = Screen()
        self.snake = Snake()
        self.grid_size = 250
        self.mov_unit = 20        
        self.food = Food(self.grid_size, self.mov_unit)

    def test_food_collision_detection(self):
        """Test if the snake correctly detects collision with the food"""
        # Place food exactly where the snake head is
        self.food.food.goto(self.snake.segments[0].xcor(), self.snake.segments[0].ycor())

        # Get initial segment count
        initial_length = len(self.snake.segments)

        # Call the check_food_collision function
        collision_detected = check_food_collision(self.snake, self.food, self.screen)

        # Check if the snake grew by 1 segment
        self.assertTrue(collision_detected, "Snake did not collided with the food")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)