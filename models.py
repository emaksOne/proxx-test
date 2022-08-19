import random
from collections import deque


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

    def click_cell(self, i, j):
        if not 0 <= i < self.size or not 0 <= j < self.size:
            error = "Position out of bounds"
            raise Exception(error)

        # check if it is black hole
        if self.board[i][j].is_bh():
            raise Exception("You lose")

        # check if it is already opened
        if self.board[i][j].is_open():
            return
        
        if self.board[i][j].get_number_of_adjacent_bh() > 0:
            self.board[i][j].set_open()
        else:
            # need to open all surrounding zero cells
            # apply BFS
            seen = set()
            q = deque()

            q.append((i,j))
            while q:
                row, col = q.popleft()
                self.board[row][col].set_open()
                seen.add((row, col))
                # if we encounter not zero cell - stop expanding from this cell
                if self.board[row][col].get_number_of_adjacent_bh() > 0:
                    continue

                for r in range(max(0, row-1), min(row+1, self.size-1) + 1):
                    for c in range(max(0, col-1), min(col+1, self.size-1) + 1):
                        if (r, c) in seen:
                            continue
                        q.append((r,c))



    def _show(self, ignore_closed=False):
        print("--"*(self.size*2))
        for line in self.board:
            values = []
            for cell in line:
                if not ignore_closed and not cell.is_open():
                    values.append("X")
                    continue
                if cell.is_bh():
                    values.append("H")
                    continue
                values.append(str(cell.get_number_of_adjacent_bh()))
            line_str = "| " + " | ".join(values) + " |"
            print(line_str)
            print("--"*(self.size*2))
    
    