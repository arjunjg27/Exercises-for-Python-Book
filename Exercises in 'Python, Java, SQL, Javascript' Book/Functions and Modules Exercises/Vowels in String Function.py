
def vowels_count(string):
    x = 0
    num = 0
    vowels = ["a", "e" , "i", "o", "u"]
    for i in string.lower():
        num += 1
        if i in vowels:
            x += 1
        if num == len(string):
            print("Amount of vowels in num:", x)
x = input("Your word:")
vowels_count(x)

