# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw
class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me): 
#We're going to have Martin and Johanna exchange ALL their apples with
#one another.
    tempApples = you.apples
    you.apples = me.apples
    me.apples = tempApples
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    totalIdeas = 0
    totalIdeas += you.ideas
    totalIdeas += me.ideas
    you.ideas = totalIdeas
    me.ideas = totalIdeas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(
    johanna.apples, martin.apples))
# Johanna has 2 apples and Martin has 1 apples
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(
    johanna.ideas, martin.ideas))
# Johanna has 2 ideas and Martin has 2 ideas




# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold our answer
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	if city1.population > min_population:
		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	if city2.population > min_population and city2.elevation > return_city.population:
		return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	if city3.population > min_population and city3.elevation > return_city.population:
		return_city = city3
	#Format the return string
	if return_city.name:
		return ("{}, {}".format(return_city.name, return_city.country))
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""




class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"