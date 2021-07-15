"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

"""
Домашняя работа

"""
from random import randint


class Player:
    def __init__(self, name, player_type='computer'):
        self.name = name
        self.type = player_type
        self.card = Card()
        self.numbers_left = 15

    def check_barrel(self, barrel):
        barrel_in_cart = False
        barrel_line = None
        barrel_column = None
        if self.type == 'human':
            answer = input("Is Barrel in your card?")
        else:
            for line_num, line in enumerate(self.card.lines):
                if barrel in line:
                    barrel_in_cart = True
                    barrel_line = line_num
                    barrel_column = line.index(barrel)
                    break

        if barrel_in_cart:
            self.cross_barrel(barrel_line, barrel_column)

    def cross_barrel(self, line, column):
        self.card.lines[line][column] = '-X'
        self.numbers_left -= 1


class Bag:
    def __init__(self):
        self.bag = list(range(1, 91))

    def _calculate_random_position(self):
        return randint(0, len(self.bag)-1)

    def get_barrel(self):
        rand_pos = self._calculate_random_position()
        return str(self.bag.pop(rand_pos))


class Card:
    def __init__(self):
        self.lines = [
            list('__' for j in range(0, 9)) for i in range(3)
        ]
        self._put_numbers()

    def show_lines(self):
        print('- '*9, 'Cart', '- '*9)
        for i in self.lines:
            print(i)
        print('- ' * 9, '++++', '- ' * 9)

    def _gen_numbers(self, number_to_search=15, start=1, end=90):
        continue_search = number_to_search
        my_numbers = []

        while continue_search:
            number = randint(start, end)
            if number not in my_numbers:
                my_numbers.append(number)
                continue_search -= 1

        return my_numbers

    def _put_numbers(self):
        numbers = self._gen_numbers()
        otr1 = numbers[:5]
        otr2 = numbers[5:10]
        otr3 = numbers[10:]
        otrs = [otr1, otr2, otr3]

        for stroka, otr in zip(self.lines, otrs):
            sorted_otr = sorted(otr)

            rand_positions = self._gen_numbers(5, 0, 8)
            rand_positions = sorted(rand_positions)
            for num, pos in zip(sorted_otr, rand_positions):
                stroka[pos] = str(num)


class player2Card(CommonCard):
    def __init__(self, rows_amount=3, cols_amount=9, nums_per_row=5, max_num=90):
        CommonCard.__init__(self)
        self._name = 'Игрок {}'.format(self.get_created_instances_count())
        self._title = ' ' + 'Карточка игрока {}'.format(self.get_created_instances_count()) + ' '
        
        @property
    def name(self):
        return self._name
        
def game():
    player = Player('Bob', 'computer')
    player.card.show_lines()
    player2 = Player('Mike', 'computer')
    player2.card.show_lines()

    bag = Bag()
    while len(bag.bag) > 0:
        print(len(bag.bag))
        barrel = bag.get_barrel()
        player.check_barrel(barrel)
        player2.check_barrel(barrel)
        player.card.show_lines()
        player2.card.show_lines()


# my_card = Card()
# my_card.show_lines()

bag = Bag()
print("Barrel is", bag.get_barrel())

game()