products = {}

item_number = int(input('Enter number of items: '))
totalprice = 0

for i in range(item_number) :
   product_name = input('Name product: ')
   price = int(input('Price: '))
   products[product_name] = price
   totalprice += price

   print(totalprice)
   print(products)









