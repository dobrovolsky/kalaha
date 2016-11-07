from Board import Board
from Player import Player
from AlphaBeta import best_move, finder


class TestBoard:
    def test_board_is_over(self):
        board = Board(Player(9, (0, 0, 0, 0, 0, 0)), Player(15, (0, 1, 0, 1, 3, 3)))
        assert board.is_over()

    def test_board_player_move_additional_move(self):
        board = Board(Player(), Player())
        assert board.player_move(True, 1)
        assert not board.player_move(True, 2)

    def test_board_player_move(self):
        board = Board(Player(), Player())
        board.player_move(True, 2)
        board.player_move(False, 3)
        board2 = Board(Player(1, (7, 1, 7, 7, 7, 7)), Player(1, (7, 7, 7, 0, 6, 7)))
        assert board == board2

    def test_board_get_children(self):
        board = Board(Player(), Player())
        assert len(board.get_children(True)) == 6

    def test_board_get_score(self):
        board = Board(Player(9, (0, 0, 0, 0, 0, 0)), Player(15, (0, 1, 0, 1, 3, 3)))
        assert board.get_score() == board.player1.bean_count - board.player2.bean_count


class TestAlphaBeta:
    def test_finder(self):
        board = Board(Player(), Player())
        assert finder(board, 3, float('-Inf'), float('Inf'), True) == 1

    def test_best_move(self):
        board = Board(Player(), Player())
        assert best_move(1, board, True) == 1
