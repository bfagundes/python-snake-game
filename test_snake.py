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

    def test__head_movement(self):
        """Test the Snake's Head movement"""
        movement_cases = {
            "right": (self.snake.mov_unit, 0),
            "left": (-self.snake.mov_unit, 0),
            "up": (0, self.snake.mov_unit),
            "down": (0, -self.snake.mov_unit)
        }

        for direction, (dx, dy) in movement_cases.items():
            with self.subTest(direction=direction): 
                self.snake.direction = direction
                
                # Get initial position of the head
                head = self.snake.segments[0]
                initial_x, initial_y = head.xcor(), head.ycor()
                
                # Move the snake
                self.snake.move()

                # Expected new position
                expected_x = initial_x + dx
                expected_y = initial_y + dy

                # Check if the head moved correctly
                self.assertEqual(head.xcor(), expected_x, f"Snake did not move correctly in {direction}")
                self.assertEqual(head.ycor(), expected_y, f"Snake did not move correctly in {direction}")

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

    def test_add_segment(self):
        """Test if a segment is correctly added to the snake"""
        initial_length = len(self.snake.segments)  # Count segments before adding

        new_position = (100, 100)  # Arbitrary position for testing
        self.snake.add_segment(new_position)

        # Check if the segment count increased by 1
        self.assertEqual(len(self.snake.segments), initial_length + 1, "Segment was not added correctly")

        # Check if the last segment was placed correctly
        last_segment = self.snake.segments[-1]
        self.assertEqual(last_segment.xcor(), new_position[0], "Segment X position is incorrect")
        self.assertEqual(last_segment.ycor(), new_position[1], "Segment Y position is incorrect")

    def test_snake_body_movement(self):
        """Test if the snake's body follows the head correctly"""

        # Store initial positions
        initial_positions = [(seg.xcor(), seg.ycor()) for seg in self.snake.segments]  

        # Move forward once
        self.snake.move()

        # Check if the head moved correctly
        head_x, head_y = initial_positions[0]
        dx, dy = self.snake.direction_map[self.snake.direction]
        expected_head_pos = (head_x + dx, head_y + dy)
        self.assertEqual((self.snake.segments[0].xcor(), self.snake.segments[0].ycor()), expected_head_pos, "Head did not move correctly")

        # Check if each body segment followed the one ahead
        for i in range(1, len(self.snake.segments)):

            # Each segment should be where the one ahead used to be
            expected_pos = initial_positions[i - 1]  
            self.assertEqual((self.snake.segments[i].xcor(), self.snake.segments[i].ycor()), expected_pos, f"Segment [{i}] did not follow correctly")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)