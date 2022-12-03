class People(object):

    def __init__(self, nameo, ageo):
        self.name = nameo
        self.age = ageo


def main():
    name = input('what is his/her name: ')
    age = input('How old is him/her: ')

    people = People(name, age)

    print(name, 'is working.')

if __name__ == '__main__':
    main()