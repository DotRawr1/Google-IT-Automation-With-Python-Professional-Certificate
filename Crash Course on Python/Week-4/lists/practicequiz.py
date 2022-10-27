filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for filename in filenames:
    old = ".hpp"
    new = ".h"
    if filename.endswith(old):
        x = len(old)
        new_filename = filename[:-x] + new
        newfilenames.append(new_filename)
    else:
        newfilenames.append(filename)
print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  latinlist = []
  for word in words:
    # Create the pig latin word and add it to the list
    latinword = word[1:] + word[0] + "ay"
    latinlist.append(latinword)
    # Turn the list back into a phrase
    say= " ".join(latinlist)
  return say	
print(pig_latin("hello how are you"))
# Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))
# Should be "rogrammingpay niay ythonpay siay unfay"


def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result += "-"
    return result
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


def group_list(group, users):
  members = ""
  if len(group) != 0:
    members += group + ":"
  if len(users) != 0:
    members += " " + users[0]
    for x in users[1:]:
      members += ", " + x
  return members
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


def guest_list(guests):
	name, age, job = guests
	for name, age, job in guests:
		print("{} is {} years old and works as {}".format(name, age, job))
guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""