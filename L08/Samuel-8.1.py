balance = 100

money = int(input('deposit amount: '))
def add(money):
    global balance
    balance = balance + money


add(money)
print(balance)