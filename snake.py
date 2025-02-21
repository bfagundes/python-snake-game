from turtle import Turtle

class Snake:

    """Models the Snake object"""
    def __init__(self, initial_segments=3, x=0, y=0, direction="r"):
        self.segments = []
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

        self.create_snake(initial_segments)

    def create_snake(self, initial_segments):
        """Creates the snake as a list of turtle segments"""
        start_positions = []
        offset = 0
        for _ in range(initial_segments):
            pos = (self.x - offset, self.y)
            offset -= self.mov_unit
            start_positions.append(pos)
        
        for position in start_positions:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a segment to the snake"""
        segment = Turtle()
        segment.color("white")
        segment.shape("square")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def turn(self, new_direction):
        """Prevent 180-degree turns"""
        opposite_directions = {"right": "left", "left": "right", "up": "down", "down": "up"}

        if new_direction in ["left", "right", "up", "down"] and new_direction != opposite_directions[self.direction]:
            self.direction = new_direction

    def move(self):
        """Moves the Snake forward in the current direction"""
        for i in range(0, len(self.segments), 1):
            dx, dy = self.direction_map.get(self.direction, (0,0))
            self.segments[i].goto(self.segments[i].xcor() + dx, self.segments[i].ycor() + dy)