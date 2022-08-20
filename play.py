from board import Board


def main():
    board = Board(8, k=10, seed=19)
    print("How it would look if all cells were open")
    board._show(all_opened=True)

    print()
    print("How it looks normaly")
    board._show()

    print()
    print("Click on cell (4,4)")
    board.click_cell(4,4)
    board._show()

    print()
    print("Click on cell (7,3)")
    board.click_cell(7,3)
    board._show()

    print()
    print("Click on cell (0,0)")
    board.click_cell(0,0)
    board._show()

if __name__ == "__main__":
    main()
