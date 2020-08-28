from crossword.ai.definition import *


class Crossword:
    def __init__(self, crossword_structure: list, words_file: str):
        self.width = len(crossword_structure[0])
        self.height = len(crossword_structure)
        self.schema = crossword_structure.copy()
        for y in range(self.width):
            for x in range(self.height):
                self.schema[x][y] = True if (crossword_structure[x][y] == '_') else False

        wf = open(words_file, 'r')
        self.words = set(wf.read().upper().splitlines())
        self.definitions = self.definitions_map()
        self.overlaps = self.detect_overlaps(self.definitions)

    def definitions_map(self) -> list:
        map = []
        if not self.schema:
            return map

        # Across definitions
        for y in range(self.height):
            start = stop = False
            previous = False
            for x in range(self.width):
                if not self.schema[y][x] and previous:
                    stop = x - 1
                    if start != stop:
                        map.append(Definition(start, y, stop - start + 1, ACROSS))
                    start = stop = False

                if self.schema[y][x]:
                    if not previous:
                        start = x
                    if x == self.width - 1:
                        stop = x
                        if start != stop:
                            map.append(Definition(start, y, stop - start + 1, ACROSS))
                previous = self.schema[y][x]

        # Down definitions
        for x in range(self.width):
            start = stop = False
            previous = False
            for y in range(self.height):
                if not self.schema[y][x] and previous:
                    stop = y - 1
                    if start != stop:
                        map.append(Definition(x, start, stop - start + 1, DOWN))
                    start = stop = False

                if self.schema[y][x]:
                    if not previous:
                        start = y
                    if y == self.height - 1:
                        stop = y
                        if start != stop:
                            map.append(Definition(x, start, stop - start + 1, DOWN))
                previous = self.schema[y][x]

        return map

    def detect_overlaps(self, definitions: list) -> list:
        maps = []
        for definition in definitions:
            maps.append(definition.get_map(self.width, self.height))

        overlaps = []
        for i in range(len(maps)):
            for j in range(i+1, len(maps)):
                if [x for x in maps[i] if x in maps[j]]:
                    overlaps.append((i, j))

        return overlaps

    def neighborhood(self, definition: Definition) -> list:
        neighbors = []
        for overlap in self.overlaps:
            if definition == self.definitions[overlap[0]]:
                neighbors.append(self.definitions[overlap[1]])
            if definition == self.definitions[overlap[1]]:
                neighbors.append(self.definitions[overlap[0]])

        return neighbors