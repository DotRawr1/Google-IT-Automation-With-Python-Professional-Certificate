name = "Sasha"
color = 'gold'
pet = ""
pet = "looooooooooooooooooooooooooooooooooooooong cat"
print("Name: " + name + ", Favorite color: " + color)
"example" * 3
len(pet)

def double_word(word):
    if word == "":
        return str(0)
    else:
        dw = (word*2)
        dwl = len(dw)
        return (str(dw) + str(dwl))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0


name = "Jayden"
print(name[1]) # a
print(name[0]) # J
print(name[5]) # n

text = "Random string with a lot of characters"
print(text[-2]) # r
print(text[-4]) # t


def first_and_last(message):
    if message == "":
        return True
    elif message[0] == message[-1]:
        return True
    else:
        return False
print(first_and_last("else")) # True
print(first_and_last("tree")) # False
print(first_and_last("")) # True


color = "Orange"
color[1:4] # ran

fruit = "Pineapple"
print(fruit[:4]) # Pine
print(fruit[4:]) # apple

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message) # A long string with a silly typo

pets = "Cats & Dogs"
pets.index("&") # 5
pets.index("C") # 0
pets.index("Dog") # 7
pets.index("s") # 3
"Dragons" in pets # False
"Cats" in pets # True


def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
    return new_email