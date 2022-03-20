from copyreg import add_extension


'''
balance = 100

money = int(input('deposit amount: '))
def add(money):
    global balance
    balance = balance + money


add(money)
print(balance)
'''

c = 10

def outer():
    c = 20
    b = 4
    def inner():
        nonlocal c
        cc = 22
        print('enclosing c: ', c)
        b = 22
        print('inner b:', b)
    inner()
    print('outer: ', c)
    print('outer: ', b)


outer()
print('golobal c: ', c)