"""x = ['dana','yossi','ben','or']

for name in x:
    print('welcome ' + name)
"""

"""list1 = []

for friend in range(3):
    userinput = input("Please enter friends name: ")
    list1.append(userinput)
    print(list1)

for name in list1:
    print('you friend is ',name)
"""
""""list1 = []
counter = 0

while True:
    userinput = input('plz enter a name: ')
    list1.append(userinput)
    counter += 1
    if counter == 3:
        break


print(list1)
print('this is the end of the script')
"""
"""num = 0

while num < 5:
    print('hi', num)
    num +=1
"""
"""counter = 0

while counter <= 8:
    print('My counter value is {}'.format(counter))
    counter +=1

print('Im out')
"""

counter = 0

while counter <= 10:
    counter += 1

    if counter == 9:
        print('the counter is 9 - im breaking the loop')
        break

    elif counter == 5:
        print('this is a special print for counter equal 5')
        continue

    else:
        print('the counter is ', counter)





