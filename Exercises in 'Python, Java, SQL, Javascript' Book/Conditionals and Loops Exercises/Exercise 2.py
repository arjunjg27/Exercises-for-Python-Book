string = input("Word:")
vowels = ["a", "e", "i","o","u"]
x = 0
for w in string:
    if w in vowels:
        x = x+1
print("Vowels in word:",+x)
