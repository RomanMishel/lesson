import random



def rps():
    Rock = 'Rock'
    Paper = 'Paper'
    Scissors = 'Scissors'

    counter = 0
    while counter <=4:
        my_random = random.randrange(1, 4, 1)
        user_input = input('Enter your move:Rock, Paper, Scissors? ---> ')
        print(my_random)
        if user_input == 'Rock' and my_random == 1:
            print('Draw')
            counter += 0

        elif user_input == 'Rock' and my_random == 2:
            print('Rock lose to Paper,You lose!')
            counter += 1

        elif user_input == 'Rock' and my_random == 3:
            print('Rock breaks the Scissors,You won!')
            counter += 1

        elif user_input == 'Paper' and my_random == 1:
            print('Paper covers the Rock,You won!')
            counter += 1

        elif user_input == 'Paper' and my_random == 2:
            print('Draw')
            counter += 0

        elif user_input == 'Paper' and my_random == 3:
            print('Paper get cut by Scissors,You lose!')
            counter += 1

        elif user_input == 'Scissors' and my_random == 1:
            print('Scissors breaks on Rock,You lose!')
            counter += 1

        elif user_input == 'Scissors' and my_random == 2:
            print('Scissors cut the Paper,You won!')
            counter += 1

        elif user_input == 'Scissors' and my_random == 3:
            print('Draw')
            counter += 1

        else:
            print('Error,Type the correct move')
            break

rps()