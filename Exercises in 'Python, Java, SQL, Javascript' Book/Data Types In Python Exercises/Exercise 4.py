f = ['apple', 'banana', 'orange', 'peach', 'kiwi']
user = input("What fruit do you like:")
if user.lower() in f:
    print("The fruit is in the list")
if user.lower() not in f:
    print("Your fruit is not in the list")