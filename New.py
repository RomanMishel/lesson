tuple1 = ("Roman", "Or", "Eyal")
print(tuple1[0], "\n", tuple1[1], "\n", tuple1[2], "\n")
print(tuple1, "\n", type(tuple1))
list1 = ['red', 'green', 'blue', 'white']

list1.append('purple')
list1.remove('blue')
print(list1)

list2 = ['red', 'green', 'blue', 'white', 'black']
print(list2)
input1 = input("Choose your color: ")
list2.remove(input1)
print('the new list is {}'.format(list2))
