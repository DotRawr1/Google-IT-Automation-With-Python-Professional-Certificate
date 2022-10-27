# "base string with {} placeholders".format(variables)

from email.quoprimime import header_check


example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""


# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""


# "{var1} {var2}".format(var1=value1, var2=value2)
value1 = "heck"
value2 = "frick"
"{:exp1} {:exp2}".format(value1, value2)

# {:d} integer value
'{:d}'.format(10.5) == '10'


# {:d}
# integer value

# {:.2f}
# floating point with that many decimals

# {:.2s}
# string with that many characters

# {:<6s}
# string aligned to the left that many spaces

# {:>6s}
# string aligned to the right that many spaces

# {:^6s}
# string centered in that many spaces