c = ["red" , "blue", "green"]
color = input("Input a color:")
if color in c:
    print("Your color is in the list")
else:
    c.append(color)
    print(*c)