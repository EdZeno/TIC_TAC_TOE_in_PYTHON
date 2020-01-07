from lib.game import Game

def test_game_has_board():
    game = Game()
    assert game.board == [[' ',' ',' '],
                          [' ',' ',' '],
                          [' ',' ',' ']]

def test_display_board():
    game = Game()
    assert game.display_board() == '  |   |  \n–\xa0–\xa0–\xa0– -\n  |   |  \n–\xa0–\xa0–\xa0– -\n  |   |  '
