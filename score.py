import turtle

class Score:
    """Represents the Score for the Snake game"""
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def reset(self):
        self.current = 0