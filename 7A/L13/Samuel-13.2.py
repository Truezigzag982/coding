def hanoi(n, a, b, c):
    if n == 1:
        print(f'{a} ——> {c}')
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)



def main():
    n = int(input('number of layers: '))
    hanoi(n, 'A', 'B', 'C')


if __name__ == '__main__':
    main()