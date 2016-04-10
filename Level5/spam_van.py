import orders_module

def read_dollar_menu():
	dollar_spam = open('dollar_menu.txt', 'r')
	
	dollar_menu = []
	for line in dollar_spam:
		line = line.strip()
		dollar_menu.append(line)
	
	print(dollar_menu)
	dollar_spam.close()

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
	orders_module.print_menu(menu)
	orders = orders_module.get_order(menu)
	total = orders_module.bill_total(orders, menu)
	write_sales_log(orders)
	print("You ordered:",orders,
			"Your total is: $", format(total, '.2f'), sep='')
			
main()