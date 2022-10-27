def print_seconds(hours, minutes, seconds):
    print((hours*3600)+(minutes*60)+seconds)
print_seconds(1,2,3)
#3723



def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds
amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
sum = amount_a + amount_b
print(str(sum))
#11715



def month_days(month,days):
    print(month + " has " + str(days) + " days.")
month_days("June",30)
month_days("July",31)
#June has 30 days.
#July has 31 days.


def rectangle_area(base, height):
	area = base*height  # the area is base*height
	print("The area is " + str(area))
rectangle_area(5,6)
#The area is 30


# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km
my_trip_miles = 55
# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)
# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))
# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
round_trip_km = my_trip_km * 2
print("The round-trip in kilometers is " + str(round_trip_km))
# The distance in kilometers is 88.0
# The round-trip in kilometers is 176.0



# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1
# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)
# 99 100



def lucky_number(name):
  number = len(name) * 9
  lucky_number_greeting = "Hello " + name + ". Your lucky number is " + str(number)
  return lucky_number_greeting
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
# Hello Kay. Your lucky number is 27
# Hello Cameron. Your lucky number is 63