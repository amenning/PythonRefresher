#Example while loop
x = 1

while x != 3:
	print('x is', x)
	x = x + 1
	
#Ordering Interface
slang = ['Knackered', 'Pip pip', 'Squidgy', 'Smashing']

menu = []

for word in slang:
	menu.append(word + ' Spam')
	
print(menu)

menu_prices = {}
price = 0.50
for item in menu:
	menu_prices[item] = price
	price = price + 1

orders = []

# while (order.upper() != 'Q'):
while(True):
	#See if the customer wants to order anything else
	order = input("Can I take your order? (Q to Quit)")
	if order == 'Cheeky Spam':
		print("Sorry, we're all out of that!")
		continue
	
	if order.upper() == 'Q':
		break
	#Find the order and add it to the list if it exists
	found = menu_prices.get(order)
	if found:
		orders.append(order)
	else:
		print("Menu item doesn't exist")
	
print(orders)