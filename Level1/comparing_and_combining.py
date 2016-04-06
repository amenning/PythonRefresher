#Comparing lists requires all elements to be in the same order and equal
my_list = [1,2,3,4]
your_list = [4,3,2,1]
his_list = [1,2,3,4]

print(my_list == your_list)

print(my_list == his_list)

#Comparing dictionaries are equal if they contain all the same key:value pairs, regardless of order
my_dict = {1:1, 2:2, 3:3, 4:4}
your_dict = {4:4, 3:3, 2:2, 1:1}

print(my_dict == your_dict)


#Combining lists
breakfast = ['Spam n Eggs', 'Spam n Jam', 'Spam n Ham']
lunch = ['SLT (Spam-Lettuce-Tomato)', 'PB&S (PB&Spam)']
dinner = ['Spalad', 'Spamghetti', 'Spam noodle soup']

#menus = [breakfast, lunch, dinner]
#print('Breakfast Menu:\t', menus[0])
#print('Lunch Menu:\t', menus[1])
#print('Dinner Menu:\t', menus[2])

#Accessing inner lists
#print(menus[0][1])

#A Dictionary of Lists
menus = {'Breakfast': breakfast, 'Lunch': lunch, 'Dinner': dinner}
print('Breakfast Menu:\t', menus['Breakfast'])
print('Lunch Menu:\t', menus['Lunch'])
print('Dinner Menu:\t', menus['Dinner'])