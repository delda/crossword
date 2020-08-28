import sys
import os

from crossword.ai.crossword import *
from crossword.ai.generate_crossword import *


class HandleCrossword:
    def __init__(self, crossword_structure: list):
        script_dir = os.path.dirname(__file__)
        rel_path = 'data/words0.txt'
        abs_file_path = os.path.join(script_dir, rel_path)
        self.crossword = Crossword(crossword_structure, abs_file_path)
        self.generator = GenerateCrossword(self.crossword)

    def generate(self) -> list:
        return self.generator.generate()
