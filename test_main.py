import unittest
from unittest.mock import Mock
from snake import Snake
from food import Food
from turtle import Screen
from main import (
    check_food_collision,
    detect_wall_collision,
    is_game_over
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

    def test_snake_self_collision(self):
        """Test if the Snake correctly detects a collision to its own body"""
        self.snake.add_segment((self.snake.segments[0].xcor(), self.snake.segments[0].ycor()))
        self.assertTrue(self.snake.detect_self_collision(), f"Snake self-collition was not detected")

    def test_snake_wall_collision(self):
        """Test if the Snake correctly detects a collision with the wall"""
        self.snake.segments[0].goto(self.grid_size + 20, 0)
        self.assertTrue(detect_wall_collision(self.snake), f"Snake collision with the wall was not detected")

    def test_game_over(self):
        # Simulating a Snake self collision
        self.snake.detect_self_collision = Mock(return_value = True)
        detect_wall_collision = Mock(return_value = False)
        self.assertTrue(is_game_over(self.snake), f"Game Over was not triggered on Snake self collision")

        # Simulating a Snake into Wall collision
        self.snake.detect_self_collision = Mock(return_value = False)
        detect_wall_collision = Mock(return_value = True)
        self.assertTrue(is_game_over(self.snake), f"Game Over was not triggered on Snake into wall collision")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)