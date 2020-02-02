from lib.game import Game

def test_game_has_board():
    game = Game()
    assert game.board == [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def test_display_board():
    game = Game()
    assert game.display_board() == '  |   |  \n–\xa0–\xa0–\xa0– -\n  |   |  \n–\xa0–\xa0–\xa0– -\n  |   |  '

def test_human_moves(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: '3')
        monkeypatch.setattr('builtins.input', lambda x: '3')
        game = Game()
        game.human_moves()
        assert game.board == [[' ',' ',' '],[' ',' ',' '],[' ',' ','X']]

def test_winner_horizontal():
    game = Game()
    board = [['X','X','X'],[' ',' ',' '],[' ',' ',' ']]
    assert game.winner(board) == 'X'

def test_winner_horizontal_none():
    game = Game()
    board = [['X','X',' '],[' ',' ',' '],[' ',' ',' ']]
    assert game.winner(board) == None

def test_winner_horizontal_second():
    game = Game()
    board = [[' ',' ',' '],['O','O','O'],[' ',' ',' ']]
    assert game.winner(board) == 'O'

def test_winner_horizontal_third():
    game = Game()
    board = [[' ',' ',' '],[' ',' ',' '],['X','X','X']]
    assert game.winner(board) == 'X'

def test_winner_vertical():
    game = Game()
    board = [['O',' ',' '],['O',' ',' '],['O',' ',' ']]
    assert game.winner(board) == 'O'

def test_winner_vertical_second():
    game = Game()
    board = [[' ','O',' '],[' ','O',' '],[' ','O',' ']]
    assert game.winner(board) == 'O'

def test_winner_vertical_third():
    game = Game()
    board = [[' ',' ','O'],[' ',' ','O'],[' ',' ','O']]
    assert game.winner(board) == 'O'

def test_winner_diagonal():
    game = Game()
    board = [['O',' ',' '],[' ','O',' '],[' ',' ','O']]
    assert game.winner(board) == 'O'

def test_winner_diagonal_second():
    game = Game()
    board = [[' ',' ','O'],[' ','O',' '],['O',' ',' ']]
    assert game.winner(board) == 'O'

def test_draw():
    game = Game()
    board = [['X','X','O'],['O','O','X'],['X','O','O']]
    assert game.draw(board) == 'Draw'

def test_draw_fail():
    game = Game()
    board = [['X','X','O'],['O','O',' '],['X','O','O']]
    assert game.draw(board) == 'Make your move'

# def test_trial():
#     empty_cells = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1]]
#     game = Game()
#     assert game.trial(empty_cells) == [1]

# def test_trial():
#     empty_cells = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,3]]
#     board = [[' ',' ',' '],
#              [' ',' ',' '],
#              [' ',' ',' ']]
#     turns = ['X']
#     game = Game()
#     assert game.trial(board, empty_cells, turns) == [1]
