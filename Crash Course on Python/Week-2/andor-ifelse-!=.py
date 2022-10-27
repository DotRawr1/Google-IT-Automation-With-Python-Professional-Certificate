print(1 == 2)
# false

print(1 != 2)
# True

print(5 > 10)
# False

print(5 < 10)
# True

print(2 == 1 and 2 == 2)
# False

print(2 == 1 or 2 == 2)
# True

print(not 1 == 1)
# False

def is_positive2(number):
  if number > 0:
    return True
is_positive(-5)
is_positive(5)
# None
# True

def is_positive2(number):
  if number > 0:
    return True
  else:
    return False
is_positive2(-5)
is_positive2(5)
# False
# True

def is_even(number):
    if number % 2 == 0:
        return True
    return False
is_even(5)
is_even(6)
# False
# True
# % = modulo, operation between ints
# quotient + remainder, returns remainder

#elif because python is dumb
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:    
        print("Valid username")
hint_username("Admin")
# Valid username
hint_username(12345678900000000000)
# Invalid username



def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // 4096
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % 4096
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks*4096) + 4096
    return (full_blocks*4096)

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192




def format_name(first_name, last_name):
	if first_name and last_name:
		print("Name: " + last_name + ", " + first_name)
	elif len(first_name) == 0:
		print("Name: " + last_name)
	elif len(last_name) == 0:
		print("Name: " + first_name)
	elif len(first_name) == 0 and len(last_name) == 0:
		print(" ")

format_name("Ernest", "Hemingway")
# Should return the string "Name: Hemingway, Ernest"

format_name("", "Madonna")
# Should return the string "Name: Madonna"

format_name("Voltaire", "")
# Should return the string "Name: Voltaire"

format_name("", "")
# Should return an empty string