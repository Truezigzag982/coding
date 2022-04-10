def factorial(n):
        if n in (0, 1):
            return 1
        else:
            return n*factorial(n-1)

def factorial_sum(n):
    result = 0
    expression = ""
    for i in range (n+1):
        result += factorial(i)
        if i > 0:
            expression += '+'
        expression += f'{i}!'
    print (f'{expression}={result}')




n = int(input('A number: '))
factorial_sum(n)
#print(f'{n}!={factorial(n)}')