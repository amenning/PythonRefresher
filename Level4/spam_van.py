def read_dollar_menu():
	dollar_spam = open('dollar_menu.txt', 'r')
	
	dollar_menu = []
	for line in dollar_spam:
		line = line.strip()
		dollar_menu.append(line)
	
	print(dollar_menu)
	dollar_spam.close()

def print_menu(menu):
	for name, price in menu.items():
		print(name, ': $', format(price, '.2f'), sep='')
		
def get_order(menu):
	orders = {}
	order = input("What would you like to order? (Q to Quit)")
	
	while (order.upper() != 'Q'):
		# find the order
		found = menu.get(order)
		if found:
			orders[order]=found
		else:
			print("Menu item doesn't exist")
			
		order = input("Anything else? (Q to Quit)")
	
	return orders

def bill_total(orders, menu):
	total = 0
	
	for order in orders:
		total += menu[order]
		
	return total

def write_sales_log(order):
	# open the file
	file = open('sales.txt', 'a')
	
	total = 0
	# write each item to the file
	for item, price in order.items():
		file.write(item + ' ' + format(price, '.2f') + '\n')
		total += price
		
	# write the total to the file
	file.write('total = ' + format(total, '.2f') + '\n\n')
	#close the file
	file.close()
			
def main():
	read_dollar_menu()
	menu = {'Knackered Spam': 4.0, 'Pip pip Spam': 3.0, 'Cheeky Spam':1.0, 'Cheerio Spam': 2.0}
	print_menu(menu)
	orders = get_order(menu)
	total = bill_total(orders, menu)
	write_sales_log(orders)
	print("You ordered:",orders,
			"Your total is: $", format(total, '.2f'), sep='')
			
main()