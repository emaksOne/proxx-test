import random


class Cell:
    def __init__(self):
        self._is_open = False
        self._is_bh = False
        self._number_of_adjacent_bh = 0

    def set_open(self):
        self._is_open = True
    
    def is_open(self):
        return self._is_open

    def set_bh(self):
        self._is_bh = True

    def is_bh(self):
        return self._is_bh

    def get_number_of_adjacent_bh(self):
        return self._number_of_adjacent_bh
    
    def increase_number_of_adjacent_bh(self, num):
        self._number_of_adjacent_bh += num


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[Cell() for _ in range(size)] for _ in range(size)]
    
    def _update_adjacent(self, bh_i, bh_j):
        for i in range(max(0, bh_i-1), min(bh_i+1, self.size-1) + 1):
            for j in range(max(0, bh_j-1), min(bh_j+1, self.size-1) + 1):
                if i == bh_i and j == bh_j:
                    continue
                self.board[i][j].increase_number_of_adjacent_bh(1)

    def populate(self, k, seed=None):
        if k > self.size ** 2:
            error = "K cannot be bigger then number of cells in the board. " + \
                f"Choose K less or equal than {self.size ** 2}"
            raise Exception(error)

        if seed is not None:
            random.seed(seed)

        indexes = random.sample(list(range(self.size**2)), k)

        for index in indexes:
            i = index // self.size
            j = index % self.size
            self.board[i][j].set_bh()
            self._update_adjacent(i, j)
 

    