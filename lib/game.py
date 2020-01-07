class Game():
    board = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]

    def display_board(self):
      board_copy = self.board.copy()
      board_copy.insert(1, ['– – – – -'])
      board_copy.insert(3, ['– – – – -'])
      pretty_board = ''.join('\n'.join([' | '.join([str(elem) for elem in list]) for list in board_copy]))
      return pretty_board

    def human_moves(self):
      row = input("Drawing an X\nSelect a row  1-3 (from top to buttom)  ")
      cell = input("Select a cell 1-3 (from left to right)  ")
      self.board[int(row)-1][int(cell)-1]="X"
      return print(self.display_board())
