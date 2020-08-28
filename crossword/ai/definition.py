ACROSS = 'across'
DOWN = 'down'


class Definition:
    def __init__(self, width: int, height: int, length: int, direction: str):
        self.width = width
        self.height = height
        self.length = length
        self.direction = direction

    def get_map(self, crossword_width, crossoword_height) -> list:
        map = []
        if self.direction == ACROSS:
            for x in range(self.width, self.width + self.length):
                map.append(x + crossword_width * self.height)
        if self.direction == DOWN:
            for y in range(self.height, self.height + self.length):
                map.append(self.width + crossoword_height * y)

        return map