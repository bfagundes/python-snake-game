from turtle import Turtle

class Snake:

    """Models the Snake object"""
    def __init__(self, initial_segments=3, x=0, y=0, direction="r"):
        self.segments = []
        self.x = x
        self.y = y
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

    def get_positions(self):
        return [(seg.xcor(), seg.ycor()) for seg in self.segments]

    def create_snake(self, initial_segments):
        """Creates the snake as a list of turtle segments"""
        start_positions = []
        start_x = self.x
        start_y = self.y
        offset = 0

        for _ in range(initial_segments):
            offset -= self.mov_unit
            x = start_x + offset
            y = start_y

            pos = (x, y)
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

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def turn(self, new_direction):
        """Prevent 180-degree turns"""
        opposite_directions = {"right": "left", "left": "right", "up": "down", "down": "up"}

        if new_direction in ["left", "right", "up", "down"] and new_direction != opposite_directions[self.direction]:
            self.direction = new_direction

    def move(self):
        """Moves the Snake forward in the current direction"""
        # Store current positions of all segments before moving
        segment_pos_log = [(seg.xcor(), seg.ycor()) for seg in self.segments]
    
        # Get movement deltas (dx, dy) based on the current direction
        # E.g. If self.direction == "right", the lookup returns (20, 0), so self.x increases by 20.
        dx, dy = self.direction_map.get(self.direction, (0,0))

        # Move the head to the next position
        head = self.segments[0]
        head.goto(head.xcor() + dx, head.ycor() + dy)

        # Move the body segments (iterate backward)
        for i in range(len(self.segments) - 1, 0, -1):
            # Move to previous segment's old position
            self.segments[i].goto(segment_pos_log[i - 1]) 