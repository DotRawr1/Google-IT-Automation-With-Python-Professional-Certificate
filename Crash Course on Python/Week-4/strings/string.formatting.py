name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name,number))
# Hello Manny, your lucky number is 15
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name,grade)
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
# 7.5 8.175
print("Base price: ${:.2f}. With tax: ${:.2f}".format(price, with_tax))
# Base price: $7.50. With tax: $8.18


def to_celcius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celcius(x)))
    # :>3 align to right at 3 spaces, :>6.2 align to right at 6 spaces with 2 decimals
#   0 F | -17.78 C
#  10 F | -12.22 C
#  20 F |  -6.67 C
#  30 F |  -1.11 C
#  40 F |   4.44 C
#  50 F |  10.00 C
#  60 F |  15.56 C
#  70 F |  21.11 C
#  80 F |  26.67 C
#  90 F |  32.22 C
# 100 F |  37.78 C