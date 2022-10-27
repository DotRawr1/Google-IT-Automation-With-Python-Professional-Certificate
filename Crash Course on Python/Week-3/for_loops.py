from math import prod


for x in range(5):
    print(x)


def square(n):
    return n*n
def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum
print(sum_squares(10)) # Should be 285


friends = ['Rem', 'Oozy', 'Delta', 'Lux']
for friend in friends:
    print("Hi " + friend)


values = [ 23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("Total sum: " + str(sum) + " - Average: " + str(sum/length))


product = 1
for n in range(1,10):
    product = product * n
print(product) # 362880


def factorial(n):
    result = 1
    for i in range(n+1):
        if i > 0:
            result = i * result
    return result
print(factorial(4)) # should return 24
print(factorial(5)) # should return 120


def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print(x, to_celsius(x))


# range function
# 1 parameter = 1 by 1 starting from 0 until 1 less
# ie range(5) = 0, 1, 2, 3, 4
# 2 parameter = 1 by 1 from first pmtr until 1 less than 2nd pmtr
# ie range(5, 10) = 5, 6, 7, 8, 9
# 3 parameter = starts at 1st pmtr, goes to 1 less than 2nd pmtr by 3rd pmtr
# ie range(0, 51, 10) = 0, 10, 20, 30, 40, 50