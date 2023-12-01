from entities.lawn_entity import Lawn
class Mower:
    def __init__(self, x: int, y: int, orientation: str, lawn: Lawn):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.lawn = lawn

    def __str__(self):
        return f"{self.x} {self.y} {self.orientation}"

    def move(self, instructions: str):
        for command in instructions:
            if command == 'A':
                if self.orientation == 'N' and self.y < self.lawn.y_max:
                    self.y += 1
                elif self.orientation == 'S' and self.y > 0:
                    self.y -= 1
                elif self.orientation == 'E' and self.x < self.lawn.x_max:
                    self.x += 1
                elif self.orientation == 'W' and self.x > 0:
                    self.x -= 1
            elif command == 'D':
                dict_orientations = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
                self.orientation = dict_orientations[self.orientation]
            elif command == 'G':
                dict_orientations = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
                self.orientation = dict_orientations[self.orientation]


