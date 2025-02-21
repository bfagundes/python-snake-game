class Snake:

    """Models the Snake object"""
    def __init__(self, segments=3, x=0, y=0, direction="r"):
        self.segments = 3
        self.x = 0
        self.y = 0
        self.direction = "right"
        
        # Movement units and direction map
        self.mov_unit = 20
        self.direction_map = {
            "right": (self.mov_unit, 0),
            "left": (-self.mov_unit, 0),
            "up": (0, self.mov_unit),
            "down": (0, -self.mov_unit),
        }

    def move(self):
        # Get movement deltas (dx, dy) based on the current direction
        # E.g. If self.direction == "right", the lookup returns (20, 0), so self.x increases by 20.
        dx, dy = self.direction_map.get(self.direction, (0, 0))

        # Update the snake's position
        self.x += dx
        self.y += dy

    def turn(self, new_direction):
        """Prevent 180-degree turns"""
        opposite_directions = {"right": "left", "left": "right", "up": "down", "down": "up"}

        if new_direction in ["left", "right", "up", "down"] and new_direction != opposite_directions[self.direction]:
            self.direction = new_direction