original = int(input("Price:"))
discount = int(input("Discount:"))
percent = 100 - discount
percent = percent / 100
final = original * percent
print(final)