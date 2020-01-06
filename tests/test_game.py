from lib.game import Game

def test_game_has_board():
    game = Game()
    assert game.board == [[' ',' ',' '],
                          [' ',' ',' '],
                          [' ',' ',' ']]
