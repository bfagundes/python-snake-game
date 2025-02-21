import unittest
from snake import Snake

class TestFunctions(unittest.TestCase):
    def setUp(self):
        """Set up a new snake for each test"""
        self.snake = Snake()

    def test_initial_position(self):
        """Test if the snake stats at the correct position."""
        self.assertEqual(self.snake.x, 0)
        self.assertEqual(self.snake.y, 0)

    def test_initial_direction(self):
        """Test if the snake starts with the correct initial direction"""
        self.assertEqual(self.snake.direction, "right")

    def test_move_right(self):
        """Test the snake movement to the right"""
        self.snake.direction = "right"
        expected_x = self.snake.x + self.snake.mov_unit
        self.snake.move()
        self.assertEqual(self.snake.x, expected_x)

    def test_move_left(self):
        """Test the snake movement to the left"""
        self.snake.direction = "left"
        expected_x = self.snake.x - self.snake.mov_unit
        self.snake.move()
        self.assertEqual(self.snake.x, expected_x)

    def test_move_up(self):
        """Test the snake movement up"""
        self.snake.direction = "up"
        expected_y = self.snake.y + self.snake.mov_unit
        self.snake.move()
        self.assertEqual(self.snake.y, expected_y)

    def test_move_down(self):
        """Test the snake movement down"""
        self.snake.direction = "down"
        expected_y = self.snake.y - self.snake.mov_unit
        self.snake.move()
        self.assertEqual(self.snake.y, expected_y)

    def test_turn_restrictions(self):
        """Test that the snake only turns left/right, from pointing position"""
        valid_turns = {
            "right": ["right", "up", "down"],  # Can continue right and turn up or down, but NOT left
            "left": ["left", "up", "down"],   # Can continue left and turn up or down, but NOT right
            "up": ["up", "left", "right"],  # Can continue up and turn left or right, but NOT down
            "down": ["down", "left", "right"] # Can continue down and turn left or right, but NOT up
        }

        for start_direction, allowed in valid_turns.items():
            
            # Testing each allowed turn
            for turn in allowed:
                self.snake.direction = start_direction
                #print(f"Turning from {start_direction} to {turn}")
                self.snake.turn(turn)
                self.assertEqual(self.snake.direction, turn, f"Snake should turn {turn} from {start_direction}")

            # Testing invalid turn (180 degree)
            opposite = {"right": "left", "left": "right", "up": "down", "down": "up"}
            self.snake.direction = start_direction
            self.snake.turn(opposite[start_direction])
            self.assertEqual(self.snake.direction, start_direction, f"Snake should not turn {opposite[start_direction]} from {start_direction}")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)