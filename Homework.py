# import random
#
# number = 0
# counter = 0
#
# random1 = random.randrange(0, 20)
# print(random1)
#
# def randomizer():
#
#     while True:
#         x = number + random1
#         y = int(input('Guess number: '))
#
#         if x > y:
#             print('Too low')
#         elif x < y:
#             print('Too high')
#
#         else:
#             x == y
#             print('You won')
#
#             return
#
# randomizer()

# try:
#
#     a = 10
#     b = 0
#     x = a / b
#     print(x)
# except Exception as error:
#     print(f'The following error occured {error}')
#
# myfile = open(r"C:\Users\Roman\Desktop\Newfile.txt", "r")
# print(myfile.read())
# myfile.close()

# newtuple = ('Roman', 'Vasya', 'Dysa')
# print('\n',newtuple[0],'\n',newtuple[1],'\n',newtuple[2])

# counter = 0

# while counter !=8:
#     print(f'My counter value is: {counter}')
#     counter +=1
#     if counter == 8:
#         print('Im done')
#         break

# carlist = []
# for car in range(4):
#     name = input('Name car: ')
#     carlist.append(name)
#     print(carlist)


# def fibn_s(n):
#     x = 0
#     y = 1
#
#     if n == 1:
#         print(x)
#
#     else:
#         print(x)
#         print(y)
#
#         for i in range(n - 2):
#             num1 = x + y
#             x = y
#             y = num1
#             print(num1)
#
#
# fibn_s(10)

# year_now = 2022
# name = input('Enter your name: ')
# print(name)
# age = int(input('Enter your age: '))
# print(age)
#
# print(type(year_now),type(age))
#
# yearwhen = year_now - age + 100
#
# print(f'You are {name} and you will turn 100 in {yearwhen} year')

#
# a = int(input('Enter a number: '))
# b = a % 2
#
#
# if b == 0:
#   print('Even')
#
# else:
#     print('Odd')

# a = [1,1,2,3,5,8,13,55,89]
# i = int()
# for i in a:
#     if i < 5:
#         print(i)
#     else:
#         break

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = int(input('Enter number: '))
# list2 = []
# for i in list1:
#
#     num1 = a / i
#
#
#     if round(num1) != num1:
#         print('Cant divide by ', (i))
#     else:
#         print("Can divide by ", (i))



def math():

    list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    newlist = []
    counter = 0

    while counter != 90:
        if counter in list1 and counter in list2:
            newlist.append(counter)

        counter += 1
    return newlist

a = math()
print(a)







