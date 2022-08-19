class Cell:
    def __init__(self):
        """Init cell instance
        By default it is not open,
        not black hole
        and has 0 adjacent black holes
        """
        self._is_open = False
        self._is_bh = False
        self._number_of_adjacent_bh = 0

    def set_open(self):
        """Set cell as open"""
        self._is_open = True

    def is_open(self):
        """Check if cell is open

        Returns:
            bool: is open
        """
        return self._is_open

    def set_bh(self):
        """Set cell as black hole"""
        self._is_bh = True

    def is_bh(self):
        """Check if cell is black hole

        Returns:
            bool: is black hole
        """
        return self._is_bh

    def get_number_of_adjacent_bh(self):
        """Get number of adjacent black holes

        Returns:
            int: number of adjacent black holes
        """
        return self._number_of_adjacent_bh

    def increase_number_of_adjacent_bh(self):
        """Increase number of adjacent black holes by one"""
        self._number_of_adjacent_bh += 1
