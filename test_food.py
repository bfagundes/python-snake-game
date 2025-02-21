import unittest
from food import Food
from snake import Snake

class TestFunctions(unittest.TestCase):
    def setUp(self):
        """Initialize a Food object before each test"""
        self.grid_size = 250
        self.mov_unit = 20        
        self.food = Food(self.grid_size, self.mov_unit)

    def test_food_within_bounds(self):
        """Test if food spawns withing the grid boundaries"""
        # Testing multiple times to ensure randomness
        for _ in range(100):
            x,y = self.food.random_position()
            max_coord = self.grid_size // self.mov_unit * self.mov_unit

            self.assertTrue(-max_coord <= x <= max_coord, f"X coord out of bounds: {x}")
            self.assertTrue(-max_coord <= y <= max_coord, f"Y coord out of bounds: {y}")

    def test_food_does_not_spawn_on_snake(self):
        """Test if the food does not spawn colliding with the Snake"""
        # Specific fixed position
        snake_positions = [(0,0),(-20,0),(-40,0)]

        # Testing multiple times to ensure randomness
        for _ in range(10):
            self.food.spawn(snake_positions)
            self.assertNotIn(self.food.spawn_position, snake_positions, f"Food spawned within the Snake!")

    def test_food_spawn_randomness(self):
        """Test if the food doesn't sapwn at the same location"""
        past_positions = set()

        # Testing multiple times to ensure randomness
        for _ in range(10):
            self.food.spawn([])
            past_positions.add(self.food.spawn_position)

        self.assertGreater(len(past_positions), 5, f"Food is spawning in the same position too often!")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)