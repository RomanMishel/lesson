password = 'secret1234'
username = 'adminstrator'
counter = 3

pwd_usernameinput = input('username:  ')
pwd_input = input('password: ')

while password != pwd_input or username != pwd_usernameinput:
    counter -= 1
    print(f'access denied!you have {counter} tries left')

    if counter == 0:
        print('You have no more tries left!')
        exit()

    pwd_usernameinput = input('username:  ')
    pwd_input = input('password:  ')



if pwd_input == password and pwd_usernameinput == username:
    print('Welcome')
    exit()