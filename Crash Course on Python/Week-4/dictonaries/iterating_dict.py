file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)
# prints extension per line
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount,ext))
# you know what this is gonna print im not typing it out
file_counts.keys()
# dict_keys([keys, duh])
file_counts.values()
# dict_values([values lmao])
for value in file_counts.values():
    print(value)
# 10
# 14
# etc


cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for key, value in cool_beasts.items():
    print("{} have {}".format(key, value))
# octopuses have tentacles
# dolphins have fins
# rhinos have horns


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    print(result)
count_letters("aaaaa")
# {"a": 5}
count_letters("tenant")
# {"t": 2}, {"e": 1}, {"n": 2}, {"a": 1}

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for key, value in groceries.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += value
	# Limit the return value to 2 decimal places
	return round(total, 2)  
groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
print(add_prices(groceries)) # Should print 28.44