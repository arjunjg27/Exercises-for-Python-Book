import random
x = random.randint(1,100)
y = 0
print(x)
user = int(input("What do you think the number is?"))
if user != x:
    while user is not x:
        if user < x:
            print("Too low")
            user = int(input("What do you think the number is?"))
            y += 1
        if user > x:
            print("Too high")
            user = int(input("What do you think the number is?"))
            y +=1
        if user ==x:
            print("good job")
            print("Tries:", + y)
elif user == x:
    y+=1
    print("Good Job")
    if y == 1:
        print("Wow first try")
    print("Tries:", + y)
            