import random

number = 0
counter = 0

random1 = random.randrange(0, 20)
print(random1)

# def randomize():
#
#     while True:
#         if random1 > number and number < 10:
#             print('number is too low')
#
#         elif random1 < number and number > 10:
#             print('number is too high')
#         else:
#             random1 == number
#             print('You win')
#         return
#
# randomize()

def randomizer():

    while True:
        x = number + random1
        y = int(input('Guess number: '))

        if x > y:
            print('Too low')
        elif x < y:
            print('Too high')

        else:
            x == y
            print('You won')

            return

randomizer()





