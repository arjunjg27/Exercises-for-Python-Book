def num_check(number):
    if number == 0:
        print("Number is 0")
    elif number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
x = int(input("Your Number:"))
num_check(x)