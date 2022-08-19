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
    
    def increase_number_of_adjacent_bh(self):
        self._number_of_adjacent_bh += 1