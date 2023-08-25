
from random import *

def amount_roll():
    while True:
        try:
            num_dice = input("Number of dice: ")
            valid_value = ['1','2','one','two']
            if num_dice not in valid_value:
                raise ValueError('1 or 2 only')
            else:
                return num_dice
        except ValueError as err:
            print(err)

def roll_dice():
    max_value = 6
    min_value = 1
    again_roll = 'Yes'

    while again_roll.lower() == 'yes' or again_roll.lower() == 'y':

        amount = amount_roll()

        if amount == '2' or amount == 'two':
            print('Rolling dice...')
            dice_1 = randint(min_value,max_value)
            dice_2 = randint(min_value, max_value)
            print('Dice one: ', dice_1)
            print('Dice two: ', dice_2)
            print('Total: ', dice_1 + dice_2)
        else:
            print('Rolling dice...')
            dice_1 = randint(min_value,max_value)
            print(f'The value is: {dice_1}')

        again_roll = input('Roll again? ')

if __name__ == '__main__':
   roll_dice()


