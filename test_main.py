import unittest
from unittest.mock import Mock, patch
from snake import Snake
from food import Food
from score import Score
from turtle import Screen
from main import (
    check_food_collision,
    detect_wall_collision,
    is_game_over
)

class TestMain(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        # Mocking screen to avoid actual rendering
        self.screen = Screen()
        self.snake = Snake()
        self.grid_size = 250
        self.mov_unit = 20        
        self.food = Food(self.grid_size, self.mov_unit)
        self.score = Score()

    def test_food_collision_detection(self):
        """Test if the snake correctly detects collision with the food"""
        # Place food exactly where the snake head is
        self.food.food.goto(self.snake.segments[0].xcor(), self.snake.segments[0].ycor())

        # Get initial segment count
        initial_length = len(self.snake.segments)

        # Call the check_food_collision function
        collision_detected = check_food_collision(self.snake, self.food, self.screen, self.score)

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

    @patch('main.detect_wall_collision')
    def test_game_over(self, mock_detect_wall_collision):
        """Test whether the game over is triggered when there's a collision"""
        # Simulating a Snake self collision
        self.snake.detect_self_collision = Mock(return_value = True)
        mock_detect_wall_collision.return_value = False
        self.assertTrue(is_game_over(self.snake), f"Game Over was not triggered on Snake self collision")

        # Simulating a Snake into Wall collision
        self.snake.detect_self_collision = Mock(return_value = False)
        mock_detect_wall_collision.return_value = True
        self.assertTrue(is_game_over(self.snake), f"Game Over was not triggered on Snake into wall collision")

    def test_initial_score(self):
        """Tests whether the initial score is 0"""
        self.assertEqual(self.score.current, 0, f"The initial score should be 0")

    # @patch('main.is_game_over')
    # def test_reset_score(self, mock_is_game_over):
    #     """Tests whether the score resets to 0 upon a game over"""
    #     self.score.current = 10

    #     mock_is_game_over.return_value = True
    #     self.assertEqual(self.score.current, 0, f"The score was not reset to 0 upon a game over")

    def test_score_increment(self):
        """Tests whether the score incremented by 1 when the snake eats food"""
        expected_score = self.score.current +1

        # Place food exactly where the snake head is
        self.food.food.goto(self.snake.segments[0].xcor(), self.snake.segments[0].ycor())

        # Simulate a collision with food
        check_food_collision(self.snake, self.food, self.screen, self.score)

        self.assertEqual(self.score.current, expected_score, f"The score was not incremented when snake collided with food")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)