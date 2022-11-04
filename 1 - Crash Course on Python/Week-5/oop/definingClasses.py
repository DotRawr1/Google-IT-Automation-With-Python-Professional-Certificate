class Apple:
    color = ""
    flavor = ""

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
# Dot notation - lets you access abilities an object might have, called methods, or
# information it might store, called attributes
## print(jonagold.color.upper()) # RED

golden = Apple()
golden.color = "yellow"
golden.flavor = "soft"

class Flower:
  color = 'unknown'
rose = Flower()
rose.color = "red"
violet = Flower()
violet.color = "blue"
this_pun_is_for_you = "this poem rhymes, \nthat's definetly true"
print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)