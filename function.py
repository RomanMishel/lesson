# """def ninja():
#     print('Roman')
#
# counter = 3
#
#
# while counter != 0:
#     ninja()
#     counter -= 1
# """
#
#
#
#
# """
# def com(ar1, ar2):
#     print('Welcome ', ar1,ar2)
#
# com('Roman', 'Mishel')
# """
#
#
#
# """"
# def plus(num1, num2):
#     return num1 + num2
#
# print(plus(1,5))
# """
#
#
# # def plus(num1, num2):
# #     return num1 + num2
# #
# # def minus(num1, num2):
# #     return num1 - num2
# #
# # def math1(num1, num2):
# #     return num1 * num2
# #
# # def math2(num1, num2):
# #     return num1 / num2
# #
# # def main():
# #     num1 = int(input('num1`: '))
# #     action = input('+ - * /')
# #     num2 = int(input('num2: '))
# #
# #
# #     if action == ""+"":
# #         print(plus(num1, num2))
# #
# #     elif action == '-':
# #         print(minus(num1, num2))
# #
# #
# #     elif action == '*':
# #         print(math1(num1, num2))
# #
# #
# #     elif action == '/':
# #         print(math2(num1, num2))
# #
# #
# #     else:
# #         print("error")
# #
# # main()
#
#
#
#
#
#
# """
# def plus(num1, num2):
#     return num1 + num2
#
# def minus(num1, num2):
#     return num1 - num2
#
# def multi(num1, num2):
#     return num1 * num2
#
# def divide(num1, num2):
#     return num1 /num2
#
# def my_sum(sum1):
#     print(f'your sum is {sum1}')
#
# def main():
#     while True:
#         num1 = input('num1: ')
#         action = input('+ - * /')
#         num2 = input('num2: ')
#
#         num1 = int(num1)
#         num2 = int(num2)
#
#         if action == '+':
#             sum1 = plus(num1, num2)
#         elif action == '-':
#             sum1 = minus(num1,num2)
#
#         elif action == '*':
#             sum1 = multi(num1,num2)
#
#         elif action == '/':
#             sum1 = divide(num1,num2)
#
#         else:
#             print('error 101')
#
#         my_sum(sum1)
#         x = input('press q to quit or press any key to continue: ')
#         if x == 'q':
#             break
# main()
# """
#
def auth(user, password):
    db = {
        'Gabriel': '123456',
        'Admin': 'admin',
        'Guest': '12345',
    }
    for key in db:
        if user == db.keys() and password == db.values():
            auth = True
            print('You are in!Welcome!')
            return auth
        else:
            auth = False
            print('Access denied!')
        return auth

user = input('Please Enter your username: ')
password = input('Please Enter you password: ')



auth(user, password)




# def cusname():
#     user_input = ''
#     while user_input != 'exit':
#         user_input = input('Enter a word: ')
#         print(user_input+'ish')
#     print('Bye bye')
#
# cusname()

# def mathcust(a, b):
#     a = 10
#     b = 5
#     mathnum1 = a * 2
#     mathnum2 = b * 2
#     mathnum3 = mathnum1 + mathnum2
#     print(mathnum3)
#
# user_input1 = input(print('Enter a number: '))
# user_input2 = input(print('Enter a number'))
# mathcust(10, 5)
#
# w = 1
