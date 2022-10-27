def factorial(n):
    result = 1
    for x in range(1,n):
        result = x * result
    return result

for n in range(0,10):
    print(n, factorial(n+1))



for x in range(1,11):
  cube = x ** 3
  print(cube)



for x in range(0,101,7):
    print(x)



def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)