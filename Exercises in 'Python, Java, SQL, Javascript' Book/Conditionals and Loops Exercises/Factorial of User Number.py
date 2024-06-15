n = int(input("Number:")) 
number_list = [i for i in range(n + 1) if i != 0]
total = sum(number_list)
print(total)
