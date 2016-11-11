import copy
import math
from Player import Player


class Board:
    def __init__(self, p1=None, p2=None):
        """
        :param p1: object of class Player
        :param p2: object of class Player
        """
        if p1 is None or p2 is None:
            self.player1 = Player()
            self.player2 = Player()
        else:
            self.player1 = p1
            self.player2 = p2
            self.player2.array = list(
                reversed(self.player2.array))  # used reversed because last element must be first in game

    def __eq__(self, other):
        if self.player1.bean_count != other.player1.bean_count:
            return False
        if self.player2.bean_count != other.player2.bean_count:
            return False
        for i in range(6):
            if self.player1.array[i] != other.player1.array[i]:
                return False
            if self.player2.array[i] != other.player2.array[i]:
                return False
        return True

    def draw(self):
        """
        This method shows board
        :return: None
        """
        print('----------Player 2----------')
        for i in reversed(self.player2.array):
            if i < 10:
                print('\t0{0}'.format(i), end=' ')
            else:
                print('\t{0}'.format(i), end=' ')
        print()
        print(self.player2.bean_count, '\t' * 7, self.player1.bean_count)
        for i in self.player1.array:
            if i < 10:
                print('\t0{0}'.format(i), end=' ')
            else:
                print('\t{0}'.format(i), end=' ')
        print()
        print('----------Player 1----------')

    def ask_for_move(self, player):
        def type_value(message=''):
            while True:
                try:
                    value = int(input(message))
                    if value < 1 or value > 6:
                        raise ValueError
                except ValueError:
                    print('You entered not right value! Try again!')
                else:
                    return value
        if player:
            print('player 1: ')
        else:
            print('player 2: ')
        while True:
            choice = type_value('Enter the number of the hole you want to remove pebbles (1-6): ')
            if player:  # check if choice have stone
                if not self.player1.array[choice - 1] == 0:
                    break
            if not player:
                if not self.player2.array[choice - 1] == 0:
                    break
            print('You entered not right value! Try again')
        return self.player_move(player, choice)

    def is_terminal(self):
        """
        Method checks if position is terminal (doesn't have move)
        :return: bool
        """
        self.is_over()

    def is_over(self):
        """
        Check if player doesn't have stones or some player has more than half of all stones
        :return bool
        """
        return sum(self.player1.array) == 0 or sum(self.player2.array) == 0

    def finish_game(self):
        """
        Sums up the game
        :return: None
        """
        for i in range(6):
            self.player1.bean_count += self.player1.array[i]
            self.player1.array[i] = 0
            self.player2.bean_count += self.player2.array[i]
            self.player2.array[i] = 0

    def player_move(self, player, choice):
        """
        Game logic
        make move this choice
        :param player: (bool) player (min or max)
        :param choice: (int)
        :return: (bool) True if player has additional move
        """
        choice -= 1
        if self.is_over(): return False
        if player:
            if self.player1.array[choice] == 0:
                raise ValueError('choice with empty position')
            bean_count = self.player1.array[choice]
            self.player1.array[choice] = 0
        else:
            if self.player2.array[choice] == 0:
                raise ValueError('choice with empty position')
            bean_count = self.player2.array[choice]
            self.player2.array[choice] = 0
            choice += 7
        for i in range(bean_count):
            choice += 1
            if choice < 6:
                self.player1.array[choice] += 1
            elif choice == 6 and player:
                self.player1.bean_count += 1
            elif (choice > 6) and (choice < 13):
                self.player2.array[int(math.fabs(choice - 7))] += 1
            elif choice == 13 and not player:
                self.player2.bean_count += 1
            elif choice == 14:
                choice = 0
                self.player1.array[choice] += 1
            else:
                if not player:
                    choice = 7
                    self.player2.array[int(math.fabs(choice - 7))] += 1
        if player:
            if choice == 6:
                return True
        if not player:
            if choice == 13:
                return True
        if choice < 6 and self.player1.array[choice] == 1 and self.player2.array[int(math.fabs(choice - 5))] != 0:
            if player:
                self.player1.bean_count += self.player2.array[int(math.fabs(choice - 5))] + 1
                self.player1.array[choice] = 0
                self.player2.array[int(math.fabs(choice - 5))] = 0
        if (choice > 6) and choice < 13 and self.player2.array[int(math.fabs(choice - 7))] == 1 and self.player1.array[
            int(math.fabs(choice - 7 - 5))] > 0:
            if not player:
                self.player2.bean_count += self.player1.array[int(math.fabs(choice - 7 - 5))] + 1
                self.player2.array[int(math.fabs(choice - 7))] = 0
                self.player1.array[int(math.fabs(choice - 7 - 5))] = 0
        return False

    def get_score(self):
        """
        :return: calculated score
        """
        return self.player1.bean_count - self.player2.bean_count

    def get_children(self, player):
        """

        :param player: (bool) player (min or max)
        :return: array of boards with every move for player
        """
        array = []
        for i in range(1, 7):
            tmp_board = copy.deepcopy(self)
            try:
                tmp_board.player_move(player, i)
            except ValueError:
                continue
            array.append(tmp_board)
        return array

