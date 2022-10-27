answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

" yes ".strip()
# "yes"
"  yes  ".lstrip()
# "yes "
"  yes  ".rstrip()
# " yes"

"The number of times e occurs in this string is 4".count("e")
# 4

"Forest".endswith("rest")
# True

"Forest".isnumeric()
# False
"12345".isnumeric()
# True

"hello".isupper()
# False
"hello".upper()
# HELLO

int("12345") + int("54321")
# 66666

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
# "This is a phrase joined by spaces"
"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])
# "This...is...a...phrase...joined...by...triple...dots"

"This is an other example".split()
["this", "is", "another", "example"]



def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS