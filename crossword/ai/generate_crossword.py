from crossword.ai.crossword import *
from crossword.ai.models import Dictionary


class GenerateCrossword:
    def __init__(self, crossword: Crossword):
        self.crossword = crossword
        self.domains = []
        # self.domains = [[]] * len(self.crossword.definitions)

    def ac3(self) -> bool:
        queue = self.all_arcs()
        while queue:
            tmp = queue.pop(0)
            x = tmp[0]
            y = tmp[1]
            if self.revise(x, y):
                x_idx = self.crossword.definitions.index(x)
                if not self.domains[x_idx]:
                    return False
                for neighbor in self.crossword.neighborhood(x):
                    if neighbor != y:
                        queue.append((neighbor, x))
        return True

    def all_arcs(self) -> list:
        queue = []
        definitions = self.crossword.definitions.copy()
        for definition in definitions:
            for neighbor in self.crossword.neighborhood(definition):
                queue.append((definition, neighbor))
        return queue

    def generate(self) -> list:
        self.nodes_consistency()
        self.ac3()
        return self.print()

    def get_overlap_step(self, x: Definition, y: Definition) -> list:
        cells_x = []
        for k in range(x.length):
            cells_x.append(
                (x.width + (k if x.direction == ACROSS else 0),
                 x.height + (k if x.direction == DOWN else 0))
            )
        cells_y = []
        for k in range(y.length):
            cells_y.append(
                (y.width + (k if y.direction == ACROSS else 0),
                 y.height + (k if y.direction == DOWN else 0))
            )
        overlap_list = [x for x in cells_x if x in cells_y]
        if not overlap_list:
            return [None, None]

        overlap = [x for x in cells_x if x in cells_y].pop()
        x_idx_step = (overlap[0] if x.direction == ACROSS else overlap[1]) - \
                     (x.width if x.direction == ACROSS else x.height)
        y_idx_step = (overlap[0] if y.direction == ACROSS else overlap[1]) - \
                     (y.width if y.direction == ACROSS else y.height)

        return [x_idx_step, y_idx_step]

    def nodes_consistency(self):
        for definition in self.crossword.definitions:
            # var = {var for var in self.crossword.words.copy() if len(var) == definition.length}
            var = set(t.word for t in Dictionary.objects.filter(word_lenght=definition.length).order_by('?')[:100])
            self.domains.append(var)

    # se non c'è alcuna parola che soddisfi la/le contraint, la elimino dal dominio
    def revise(self, x: Definition, y: Definition) -> bool:
        revised = False
        (x_idx_step, y_idx_step) = self.get_overlap_step(x, y)
        if x_idx_step is None or y_idx_step is None:
            return False

        x_idx_definition = self.crossword.definitions.index(x)
        y_idx_definition = self.crossword.definitions.index(y)

        for x_domain in self.domains[x_idx_definition].copy():
            check = False
            for y_domain in self.domains[y_idx_definition]:
                if not check and x_domain[x_idx_step] == y_domain[y_idx_step] and x_domain != y_domain:
                    check = True
            if not check:
                self.domains[x_idx_definition].discard(x_domain)
                revised = True
        return revised

    def print(self):
        cw = self.crossword.schema.copy()
        for x in range(self.crossword.height):
            for y in range(self.crossword.width):
                cw[x][y] = ' ' if (cw[x][y]) else '#'
        for definition in self.crossword.definitions:
            idx_definition = self.crossword.definitions.index(definition)
            if definition.direction == ACROSS:
                for x in range(definition.length):
                    for string in self.domains[idx_definition]:
                        cw[definition.height][definition.width + x] = string[x].upper()
            else:
                for y in range(definition.length):
                    for string in self.domains[idx_definition]:
                        cw[definition.height + y][definition.width] = string[y].upper()
        # for x in range(self.crossword.height):
        #     for y in range(self.crossword.width):
        #         print(cw[x][y], end=' ')
        #     print()
        return cw
