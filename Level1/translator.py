#slang = ['cheerio','pip pip', 'smashing', 'yonks', 'knackered']
#translation = ['goodbye', 'goodbye', 'terrific', 'ages', 'tired']

#del slang[0]
#del translation[0]

#print(slang)
#print(translation)

#Create Dictionary
#slang = {'cheerio':'goodbye', 'knackered':'tired', 'yonks':'ages'}
#print(slang['cheerio'])


#Can create an empty dictionary
slang={}
slang['knackered'] = 'tired'
slang['smashing'] = 'terrific'
slang['cheerio'] = 'goodbye' 
print(slang)
slang['smashing'] = 'awesome'
print(slang['smashing'])

del slang['cheerio']
print(slang)

#Trying to access a key that doesn't exist will cause an error
#If you want to check if a word is in the dictionary, use get()
#It will return the value if it exists, otherwise 'None' will be returned
#'None' evaluates to false in conditionals
result = slang.get('bloody')

if result:
	print(result)
else:
	print("Key doesn't exist")
	
#Translate a sentence
slang['mate'] = 'buddy'
slang['cheeky'] = 'offensive'
sentence = 'Sorry, my ' + 'mate' + "'s a bit " + 'cheeky' + '!'
translation = 'Sorry, my ' + slang.get('mate') + "'s a bit " + slang.get('cheeky') + '!'
print(sentence)
print(translation)