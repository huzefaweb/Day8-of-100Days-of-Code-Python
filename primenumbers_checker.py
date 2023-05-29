# primenumber checker
n = int(input("Enter a number to check if it is a prime number or not: "))

# user defined function using the modulo for comparison
def prime_checker(num):
  flag = False

  if num == 1:
    print(num, "is not a prime number")
  elif num > 1:
    # check for factors
    for i in range(2, num):
      if (num % i) == 0:
        # if factor is found, set flag to True
        flag = True
        # break out of loop
        break

    # check if flag is True
    if flag:
      print(num, "is not a prime number")
    else:
      print(num, "is a prime number")

# this input gets passed into the function where the
# number is checked
prime_checker(num=n)
