n = int(input("Number of Fibonacci numbers wanted:"))
f = [0,1]
t = 0
for i in range(n):
    fib = f[t]+f[t+1]
    f.append(fib)
    t += 1 
    if t == n:
        print(*f)
        break