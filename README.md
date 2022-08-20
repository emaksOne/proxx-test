## CORETEKA TEST

### Part 1
To represent a game state I created two classes: Cell and Board

Cell describes following states: is it open, is it black hole and number of adjacent black holes
```
self._is_open = False
self._is_bh = False
self._number_of_adjacent_bh = 0
``` 
Also class contains getter/setter for this fields
and method to increase `_number_of_adjacent_bh` by 1

Board responsible for creating a matrix (list of lists) of Cell objects with specified size. 

### Part 2
For Board class I add `_populate` method. I randomly choose K indexes from array with length N**2 and then convert it to `i,j` (`i = index // N; j = index % N`) for matrix and set cell for this position as a black hole.

### Part 3
For every set black hole I update all neigbor cells by increasing its `_number_of_adjacent_bh` by 1. In this way every non-black-hole cell will contain number of adjacent black hole cells.

### Part 4
Logic for click cell. Firstly I check validity of position and corner cases like clicking on already visible cell or black hole. There is a good place to ask clarifying questions like "How to handle clicking on black hole? Return False, print something or raise an error". I chose to raise an error but it could be discussed. 
Then if we pass all this checks we can make cell visible. If the cell has at least one adjacent black hole then we just set cell as open `board[i][j].set_open()` and we're done. Logic becomes more involving if cell has no adjacent black holes. In this case we need open all neighbors that also has no adjacent black holes and then nighbors of theese neighbors and so on. Until we met non-zero cell. But also we need to open that first-met non-zero cell and stop scaning neigbors for this cell. To implement this idea I apply BFS. To implement it we need queue for adding neghbors and Set for tracking already processed cells. So initialy, we add clicking cell to queue. Then in a loop while we have non-empty queue we get cell from queue then set it as open, mark it as processed by adding to Set and if this is zero-cell we add all its neighbors to queue (except those that we already processed). So in the end we will open all region with zero cells and non-zero cells that are neigbors to that region.



## Demo
For debug or demo purpose I add `play.py`. Here I create board and make several clicks on cells to check if everything works as expected.


