user_input = input('Choose a number: ')
answer = input('Are you sure?yes or no? ')

if answer == 'yes':
    print(user_input)
elif answer == 'no':
    print(input('Choose a new number: '))

