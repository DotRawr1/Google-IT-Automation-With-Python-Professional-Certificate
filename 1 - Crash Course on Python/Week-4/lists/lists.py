x = ["Now", "we", "are", "cooking!"]
type(x)
# <class 'list'>
print(x)
# ["Now", "we", "are", "cooking!"]
len(x)
# 4
"are" in x
# True
"Today" in x
# False
print(x[0])
# Now
print(x[3])
# cooking!
x[1:3]
["we", "are"]
x[:2]
["are", "cooking!"]


def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")
print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing