def multiplication_creator():
    x = int(input('please, enter a first number for multiplication table: '))
    y = int(input('please, enter a second number for multiplication table: '))
    multiplication(x, y)


def multiplication(x, y):
    for i in range(x + 1):
        for j in range(y + 1):
            if j == 0:
                print(i, end='\t')
                continue
            if i == 0:
                print(j, end='\t')
                continue
            else:
                print(i * j, sep='', end='\t')
        print('')


if __name__ == '__main__':
    multiplication_creator()
