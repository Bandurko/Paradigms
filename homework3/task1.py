'''
 Контекст
Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
время реализовать её. Два игрока по очереди ставят крестики
и нолики на игровое поле. Игра завершается когда кто-то
победил, либо наступила ничья, либо игроки отказались
играть.
 Задача
Написать игру в “Крестики-нолики”. Можете использовать
любые парадигмы, которые посчитаете наиболее
подходящими. Можете реализовать доску как угодно - как
одномерный массив или двумерный массив (массив массивов).
Можете использовать как правила, так и хардкод, на своё
усмотрение. Главное, чтобы в игру можно было поиграть через
терминал с вашего компьютера.
'''

'''
Раз уж изучаем парадигму ООП, то и программу напишем в парадигме ООП.
'''

import sys


class GameException(Exception):
    pass
class EndGameException(GameException):
    pass

class Field:
    def __init__(self):
        self.cells = {i: Cell() for i in range(1, 10)}

    def set_item_in_cell(self, item, cell):
        cell = self._get_cell(cell)
        cell.set_item(item)

    def _get_cell(self, i):
        cell = self.cells.get(i)
        if cell is None:
            raise GameException('\nТакой ячейки нет')
        return cell

    def check_win(self):
        win_routes = (1, 2, 3), (4, 5, 6), (7, 8, 9), \
            (1, 4, 7), (2, 5, 8), (3, 6, 9), \
            (1, 5, 9), (3, 5, 7)

        for route in win_routes:
            cell = self.cells[route[0]]
            for i in route:
                if cell.item is None or self.cells[i].item != cell.item:
                    break
            else:
                raise EndGameException(f'\nПобедитель: {cell.item}!')

    def check_draw(self):
        for cell in self.cells.values():
            if cell.item is None:
                break
        else:
            raise EndGameException('\nВы сыграли вничью.')


class Cell:
    def __init__(self):
        self.item = None

    def set_item(self, item):
        if self.item:
            raise GameException('\nЭта ячейка уже занята')
        self.item = item

class Game:
    def __init__(self, field):
        self.field = field
        self.player1 = Player(chr(10060), False)
        self.player2 = Player(chr(11093), True)

    def move(self, player, cell):
        self.field.set_item_in_cell(player.item, cell)
        self.field.check_win()
        self.field.check_draw()

    def get_active_player(self):
        self.player1.is_active, self.player2.is_active = self.player2.is_active, self.player1.is_active
        if self.player1.is_active:
            return self.player1
        return self.player2

class Player:
    def __init__(self, item, is_active: bool):
        self.item = item
        self.is_active = is_active

class View:
    def __init__(self, game):
        self.game = game

    def start_game(self):
        while True:
            self.show_field()
            player = self.game.get_active_player()
            while True:
                try:
                    cell = int(input(f'Укажите номер ячейки для {player.item}: '))
                    self.game.move(player, cell)
                    break
                except EndGameException as ex:
                    print(ex)
                    self.show_field()
                    sys.exit()
                except GameException as ex:
                    print(ex)
            print()

    def show_field(self):
        print('-' * 10)
        for i in range(0, 9, 3):
            dct = [*self.game.field.cells.items()][i: i + 3]
            print('\t'.join([str(cell[0]) if cell[1].item is None else cell[1].item for cell in dct]))
            print('-' * 10)

game = Game(Field())
view = View(game)
view.start_game()