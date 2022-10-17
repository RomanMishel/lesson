import random
#generate number
rand_new = str(random.randrange(0, 10000)).zfill(4)
# #put output in a list
# rannum_list = [rand_new]

def cows_n_bulls():
    # cows empty
    cows = 0
    #game continues until the count not equals to 4
    while cows != 4:
        #ask a user for a guess
        user_input = str(input('Guess a number: '))
        #for each element in list
        for i in range(len(user_input)):
            #if user wants to end the game
            if user_input == 'exit':
                break
            #if user guessed right some of digits
            elif user_input[i] == rand_new[i]:
                cows += 1
                print(f'you guessed right {cows} out of 4')
            #if user guessed all correctly
            elif user_input == rand_new:
                cows += 4
                print('You guessed all correct!')
                break
            #if user didnt guess anything right
            elif user_input[i] != rand_new:
                print('You didnt guessed any digit, right again!')

            else:
                return





cows_n_bulls()





