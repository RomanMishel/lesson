def db_custom(username, password):
    user_db = {'Roman': '123456', 'Admin': 'admin', 'Guest': '12345'}



    for i in user_db:
        if i in user_db.keys() == username and i in user_db.values() == password:
            db_custom = True
            return db_custom
        else:
            db_custom = False
            return db_custom

username = input('Enter your username: ')
password = input('Enter your password: ')

if db_custom(username, password) == True:
    print('You are in!Welcome!')
else:
    print('Access denied!')


db_custom(username, password)

