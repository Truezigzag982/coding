def f(n):
    if n in (1, 2):
        return 1
    else:
        #a = n
        #n == n - 1 + a - 2
        #return n
        return f(n-1) + f(n-2)
    
n = int(input('Enter a fibonacci number: '))
for i in range(1, n+1):
    print(f(i), end=',')