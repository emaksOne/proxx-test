import random
from collections import deque
from typing import Union

from cell import Cell


class Board:
    def __init__(self, size: int):
        """Init Board instance

        Args:
            size (int): size of the board
        """
        self.size = size
        # create (size x size) matrix of cells
        self.board = [[Cell() for _ in range(size)] for _ in range(size)]

    def _update_adjacent(self, bh_i: int, bh_j: int):
        """Helper method to update adjacent cells with +1

        Args:
            bh_i (int): black hole row position
            bh_j (int): black hole col position
        """
        for i in range(max(0, bh_i - 1), min(bh_i + 1, self.size - 1) + 1):
            for j in range(max(0, bh_j - 1), min(bh_j + 1, self.size - 1) + 1):
                if i == bh_i and j == bh_j:
                    continue
                self.board[i][j].increase_number_of_adjacent_bh()

    def populate(self, k: int, seed: Union[int, None] = None):
        """Populate board with K black holes

        Args:
            k (int): number of black holes
            seed (Union[int, None], optional): seed for random. Defaults to None.

        Raises:
            Exception: K is not valid
        """

        if k > self.size**2 or k < 0:
            error = "K is not valid"
            raise Exception(error)

        if seed is not None:
            random.seed(seed)

        # imagine if we unroll matrix to single vector
        # and pick random k indexes in this vector
        indexes = random.sample(list(range(self.size**2)), k)

        for index in indexes:
            # convert vector index to matrix i, j indexes
            i = index // self.size
            j = index % self.size
            self.board[i][j].set_bh()
            # update adjacent cells (+1)
            self._update_adjacent(i, j)

    def click_cell(self, i: int, j: int):
        """Update board when click on cell

        Args:
            i (int): cell's row position
            j (int): cell's col position

        Raises:
            Exception: not valid cell's click position
            Exception: click on the black hole
        """
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

            # for storing processed cells
            seen = set()
            q = deque()

            q.append((i, j))
            while q:
                row, col = q.popleft()
                self.board[row][col].set_open()
                seen.add((row, col))
                # if we encounter not zero cell - stop expanding from this cell
                if self.board[row][col].get_number_of_adjacent_bh() > 0:
                    continue

                # add neighbor cells to queue
                for r in range(max(0, row - 1), min(row + 1, self.size - 1) + 1):
                    for c in range(max(0, col - 1), min(col + 1, self.size - 1) + 1):
                        # skip processed or already open cell
                        if (r, c) in seen or self.board[r][c].is_open():
                            continue
                        q.append((r, c))

    def _show(self, all_opened: bool = False):
        """Display board. For debug purpose

        Args:
            all_opened (bool, optional): If it is True then consider that all cells is open. Defaults to False.
        """
        print("--" * (self.size * 2))
        for line in self.board:
            values = []
            for cell in line:
                if not all_opened and not cell.is_open():
                    values.append("X")
                    continue
                if cell.is_bh():
                    values.append("H")
                    continue
                values.append(str(cell.get_number_of_adjacent_bh()))
            line_str = "| " + " | ".join(values) + " |"
            print(line_str)
            print("--" * (self.size * 2))
