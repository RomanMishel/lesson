import random

myrandom = random.randrange(1, 10, 1)

user_input = int(input("Enter you guessing number: "))

print(myrandom)

if user_input == myrandom:

    print('You guessed right!')

elif user_input <= myrandom:

    print('You guessed too low')

elif user_input >= myrandom:
    print('You guessed too high')
else:
    print('Error')