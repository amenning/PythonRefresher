#Determine Average Price
total = 0
prices = [2.50, 3.50, 4.50]

for price in prices:
	print('Price is', price)
	total = total + price
	print('total is', total)
	
average = total/len(prices)
print('avg is', average)