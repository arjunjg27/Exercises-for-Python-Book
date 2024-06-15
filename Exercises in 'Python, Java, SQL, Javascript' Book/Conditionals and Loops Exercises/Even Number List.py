numb = []
def n_even_numbers(n):
    count = 0
    num = 0
    while count < n:
        if num % 2==0:
            numb.append(num)
            count += 1
        num += 1
n = int(input("Amount of even numbers wanted:"))
n_even_numbers(n)
print(*numb)

