import random

#Random.random will produce a random number between 0 and 1
print('random.random()')
r1 = random.random()
print(r1)

#Random.choice will product a random result from a list
print('random.choice([1,2,3,4,5])')
r2 = random.choice([1,2,3,4,5])
print(r2)

#Random.ranint will product a random integer between two numbers
print('random.randint(1,1000)')
r3 = random.randint(1,1000)
print(r3)

print('Winning Ticket Numbers')
for i in range(10):
	ticket = random.randint(1,1000)
	print(ticket)
	
print('Years circus was held in Orlando, FL since 2005 until 2016')	
for i in range(2005, 2016, 2):
	print(i)