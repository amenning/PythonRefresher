slang = ['Knackered', 'Pip pip', 'Squidy', 'Smashing']

menu = []

for word in slang:
	menu.append(word + ' Spam')
	
print(menu)

menu_prices = {}
price = 0.50
for item in menu:
	menu_prices[item] = price
	price = price + 1
	
print(menu_prices)

for name, price in menu_prices.items():
	print(name, ': $', format(price, '.2f'), sep='')