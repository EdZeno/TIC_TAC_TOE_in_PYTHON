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
