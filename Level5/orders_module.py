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
