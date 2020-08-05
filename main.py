num, b, c, count = int(input('Enter a number: ')), '  ', '   ', 0
for i in range(0, num+1):
    if i > 9:
        b = b + str(i) + '   '
        c = c + str(i) + '|'
    else:
        b = b + str(i) + '    '
        c = c + str(i) + ' |'
    for a in range(0, num+1):
        d = str(a*i)
        for letter in d:
            count += 1
        c = c + str(a*i) + ' '*(5-count)
        count = 0
    c = c + '\n   '

print((' ')*4 + b)
print((' ')*6 + ('-'+ '    ')*num)
print(c)

# something interesting