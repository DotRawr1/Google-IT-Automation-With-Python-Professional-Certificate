'''
variables that have different values for different instances of the same
class are called instance variables

 class ClassName:
    def method_name(self, other_parameters):
        body_of_method
'''

class Piglet:
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))
    years = 0
    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()


piggy = Piglet()
piggy.years = 2
print(piggy.pig_years())


class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())